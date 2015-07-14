from cmd import Cmd

class  booksPrompt(Cmd):

    def do_hello(self, args):
        if len(args) == 0:
            name = 'stranger'
        else:
            name = args
        print 'Hello, %s' % name
    def do_quit(self, args):
        print "Quitting"
        raise SystemExit

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        booksPrompt().onecmd(' '.join(sys.argv[1:]))
    else:
        print "Help"
