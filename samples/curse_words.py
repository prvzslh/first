from urllib.request import urlopen
import urllib.request
import urllib.parse

def read_file():
    contents = open("/home/parvez/PycharmProjects/first/samples/cursewords/movie_quotes1.txt")
    quotes = contents.read()
    #print(quotes)
    check_badwords(quotes)


def check_badwords(words_tocheck):
    connection = urlopen("http://www.wdylike.appspot.com/?q=",words_tocheck)
    output = connection.read()
    print(output)

read_file()
check_badwords()