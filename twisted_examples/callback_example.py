__author__ = 'Charlie'

class Countdown(object):

    def __init__(self, counter):
        self.counter = counter

    def decrement_count(self, decrement):
        if self.counter < 1:
            reactor.stop()
        else:
            print self.counter
            self.counter -= decrement
            reactor.callLater(1, self.decrement_count, decrement)

def main():
    from twisted.internet import reactor
    c = Countdown(10)
    reactor.callWhenRunning(c.decrement_count, 1)

    print "Reactor Starting..."
    reactor.run()
    print "Reactor Stopped!"

if __name__ == "__main__":
    main()