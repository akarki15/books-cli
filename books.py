""" Reads records from input files and outputs the records """
from cmd import Cmd
import sys

class  booksPrompt(Cmd):
    """ Handle command line requests """
    def do_hello(self, args):
        if len(args) == 0:
            name = 'stranger'
        else:
            name = args
        print 'Hello, %s' % name

    def do_quit(self, args):
        print "Quitting"
        raise SystemExit

    def default(self, line):
        print 'Hola'

def get_files():
    """ Returns the list of files to be read """
    return ['csv', 'pipe', 'slash']

def return_records():
    """ Reads in the input files and returns as a list """
    records = []
    separator = {'csv' : ',', 'pipe' : '|', 'slash':'/'}
    for txt_file in get_files():
        for line in  open(txt_file, 'r'):
            records.append(line.split(separator[txt_file]))
    return records

if __name__ == "__main__":
    # for item in return_records():
    #    print item
    
    booksPrompt().onecmd(' '.join(sys.argv[1:]))
