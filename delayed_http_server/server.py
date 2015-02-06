__author__ = 'Charlie'

from twisted.internet.task import deferLater
from twisted.web import server, resource
from twisted.web.server import NOT_DONE_YET
from twisted.internet import reactor
import random

INSULTS = [
    "You are funny lookin!",
    "I don't know what your problem is, but I'll bet it's hard to pronounce.",
    "How about never? Is never good for you?",
    "I see you've set aside this special time to humiliate yourself in public.",
    "I'll try being nicer if you'll try being smarter.",
    "It sounds like English, but I can't understand a word you're saying.",
    "I will always cherish the initial misconceptions I had about you."
    ]

def get_insult():
    """returns a random insult"""
    return random.choice(INSULTS)



class InsultThem(resource.Resource):
    isLeaf = True

    def _response_and_close(self, request, insult):
        """replies to the request with an insult and closes the request"""
        request.write(insult)
        request.finish()
        print "served: insult: {i}".format(i = insult)


    def render_GET(self, request):
        # Choose a time delay to respond and the insult
        delay = random.choice((0,1,2,3,4,5))
        insult = get_insult()

        # Register a callback to write to the request stream and close
        print "request: delay: {d}, insult: {i}".format(d = delay, i = insult)
        d = deferLater(reactor, delay, lambda: request)
        d.addCallback(self._response_and_close, insult)

        # Return a token to ask the client to keep polling / keep alive.
        return NOT_DONE_YET


def main():
    site = server.Site(InsultThem())
    reactor.listenTCP(8080, site)
    reactor.run()


if __name__ == "__main__":
    main()