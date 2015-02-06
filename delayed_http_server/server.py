__author__ = 'Charlie'

from twisted.internet.task import deferLater
from twisted.web import server, resource
from twisted.web.server import NOT_DONE_YET
from twisted.internet import reactor
import random
from insults import get_insult
import uuid


class InsultThem(resource.Resource):
    isLeaf = True

    def _response_and_close(self, request, insult, request_id):
        """replies to the request with an insult and closes the request"""
        request.write(insult)
        request.finish()
        print "{u} : served: insult: {i}".format(u = request_id, i = insult)


    def render_GET(self, request):
        # Choose a time delay to respond and the insult
        delay = random.choice((0,1,2,3,4,5))
        insult = get_insult()

        # Unique identifier
        request_id = uuid.uuid1()

        # Register a callback to write to the request stream and close
        print "{u} : request: delay: {d}, insult: {i}".format(u = request_id, d = delay, i = insult)
        d = deferLater(reactor, delay, lambda: request)
        d.addCallback(self._response_and_close, insult, request_id)

        # Return a token to ask the client to keep polling / keep alive.
        return NOT_DONE_YET


def main():
    site = server.Site(InsultThem())
    reactor.listenTCP(8080, site)
    reactor.run()


if __name__ == "__main__":
    main()