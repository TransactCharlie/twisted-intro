__author__ = 'Charlie'

from twisted.internet.defer import Deferred

def handle_error(error): return "CAUGHT: {e}".format(e = error.getErrorMessage())

def to_upper(s): return s.upper()

def print_foo(foo):
    print foo
    return foo

def main():
    d = Deferred()

    # Add a callback and an errback to fire if something went wrong
    d.addCallback(to_upper)
    d.addErrback(handle_error)

    d.addCallback(print_foo)

    # fire the chain with a integer rather than a string
    d.callback(1)

if __name__ == "__main__":
    main()