__author__ = 'Charlie'

from twisted.internet.defer import Deferred

def to_upper(s):
    return s.upper()

def print_foo(foo):
    print foo
    return foo

def main():
    d = Deferred()

    d.addCallback(print_foo)
    d.addCallback(to_upper)
    d.addCallback(print_foo)

    # fire the chain with a normal result
    d.callback("yo, uppercase me!")

    print "Finished"

if __name__ == "__main__":
    main()