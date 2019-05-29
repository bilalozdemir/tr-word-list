"""
MEANING SCRAPER SCRIPT

    This script scraps meanings of the words out of the given source and
    concatenates them together into a '.txt' file.

    Classes
    -------
        UserError
            Catches user errors, instances defined with their error messages

            Values:
                err: error message

            Functions:
                __str__: returns error message

    Functions
    ---------
        meaning_scraper: adds words to the database

        word_scraper: scraps the data out of a file and put into the database

    USAGE (flags)
    -------------
        '--search <word>'
            looks for meaning(s) of the word on the given url

        '--ml <source txt file> <target txt file>'
            pulls the words from the source file, finds their meanings and puts
            them together in the target file

"""

import re
import sys
from urllib.parse import quote_plus
from urllib.request import HTTPCookieProcessor, build_opener
from bs4 import BeautifulSoup

MEANING_MATCH = re.compile('\"anlam\":\"(.*?)\"')
OPENURL = build_opener(HTTPCookieProcessor()) #Defining our url opener

class UserError(Exception):
    """Catching User Errors"""

    def __init__(self, err):
        super(UserError, self).__init__()
        self.err = err

    def __str__(self):
        return self.err

def meaning_scraper(word):
    """
    Looks and scrapes the meaning of the word

    ...

    Arguments
    ----------
        word: str
            Word wanted to be searched

    Raises
    ------
        UserError:
            When no meaning is found for the given word

    Returns
    -------
        _s: str
            A formatted string that holds word and the meaning(s) of the word
    """
    html = OPENURL.open('http://sozluk.gov.tr/gts?ara={}'.format(quote_plus(word)))
    soup = BeautifulSoup(html, 'lxml', from_encoding="utf-8")
    body = soup.find('body')
    _s = '\n'.join(re.findall(MEANING_MATCH, body.get_text()))

    if not _s:
        err = 'There is no meaning(s) found for the word: {}'.format(word)
        raise UserError(err)

    return _s

def make_list(source, target):
    """
    Looks and scrapes the meaning of the word

    ...

    Arguments
    ----------
        source: str
            path for source text file
        target: str
            path for target text file

    Raises
    ------
        UserError:
            When no meaning is found for the given word in 'meaning_scraper'
    """
    with open(source, 'r') as _s:
        words = _s.read().split('\n')
    with open(target, 'r+') as _t:
        for word in words:
            try:
                _t.write(word + '**' + meaning_scraper(word) + '%%\n')
            except UserError:
                _t.write(word + '**0%%\n')
    print('Done!')


if __name__ == '__main__':
    if '--search' in sys.argv:
        print(meaning_scraper(sys.argv[-1]))
    if '--ml' in sys.argv:
        make_list(sys.argv[-2], sys.argv[-1])
