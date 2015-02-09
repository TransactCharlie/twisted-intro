__author__ = 'Charlie'

from twisted.internet import reactor
from twisted.internet.defer import DeferredList
from twisted.web.client import Agent, readBody
from twisted.web.http_headers import Headers
from collections import defaultdict
import time

agent = Agent(reactor)
INSULT_SERVER = "http://localhost:8080"
HEADERS = Headers({'User-Agent': ['Twisted Web Client']})
QUERIES_TO_MAKE = 500

def calculate_stats(insult_list):
    dd = defaultdict(int)
    for i in insult_list:
        dd[i[1]] += 1
    return dict(dd)

def print_stats(stats):
    for k, v in stats.items():
        print k,v
    reactor.stop()

def fetch_and_process_insult():
    """Returns a deferred which will fire with the value returned from server"""
    d = agent.request(
        method="GET",
        uri=INSULT_SERVER,
        headers=HEADERS
        )
    d.addCallback(readBody)
    return d


def main():
    all_insults = DeferredList([fetch_and_process_insult() for i in  range(0,QUERIES_TO_MAKE)])
    all_insults.addCallback(calculate_stats)
    all_insults.addCallback(print_stats)

    now = time.time()
    print "starting Reactor"
    reactor.run()
    print "done: seconds {s}".format(s = time.time() - now)


if __name__ == "__main__":
    main()