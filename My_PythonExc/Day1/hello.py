import sys

def hello(name):
    print 'hello=>', name, '\n'

def main():
    word = 'Hello'
    print hello(dir(sys))
    #print (help(sys.exit()))
    print 'Hello name => %s and age =%d' %('Alice',32)

if __name__ == '__main__':
    main();

