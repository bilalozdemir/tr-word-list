"""
MEANING SCRAPER SCRIPT

This script makes `GET` requests to `BASE_URL` `ITEM_COUNT` times, parses the
response and writes the output dictionaries into `words.json` file.
"""

import logging
import time
import sys
from typing import Union

import httpx
import orjson

BASE_URL = "https://www.sozluk.gov.tr/gts_id"
ITEM_COUNT = 92407

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] :: %(asctime)s :: %(message)s :: Log at func <%(funcName)s>')

def parse_meanings(data: Union[list, dict], index: int) -> Union[dict, None]:
    """Scrape 'item' and 'meanings' of the item from given 'data'.

    :param data:
    :type data: dict
    :return: Return scraped data in dictionary format.
    :rtype: dict
    """
    try:
        _dict_data = data[0]
        item = _dict_data['madde']
        meanings = [meaning['anlam'] for meaning in _dict_data['anlamlarListe']]
    except (KeyError, TypeError) as _e:
        logging.warning(f"Unexpected error occured at index <{index}>! :: {_e}")
        return None
    else:
        logging.critical(f"Uncaught error occured at index <{index}>!")
        return None

    return {'word': item, 'meanings': meanings}

def main() -> None:
    """Create an iterator object over the response items and yield parsed data,
    write the data into 'words.json' and log if successful.
    """
    # TODO: Multi-threaded requests.
    def response_iterator(_n: int):
        for i in range(1, _n + 1):
            _response = httpx.get(BASE_URL, params={'id': i})
            _parsed_data = parse_meanings(_response.json(), i)
            if not _parsed_data:
                continue
            yield _parsed_data

    _iterator = response_iterator(ITEM_COUNT)
    _parsed_count = 0
    with open('words.json', 'w+') as file:
        file.write('[')
        for parsed_data in _iterator:
            _parsed_count += 1
            file.write('\n\t' + orjson.dumps(parsed_data, option=orjson.OPT_INDENT_2).decode('utf-8') + ',')
        file.write('\n]')

    logging.info(f"{_parsed_count}/{ITEM_COUNT} ({100*_parsed_count//ITEM_COUNT}%) items has been written in 'words.json' succesfully.")

if __name__ == '__main__':
    START_TIME = time.time()
    try:
        main()
    except KeyboardInterrupt:
        # TODO: Handle KeyboardInterrupt. Fix broken data.
        # Ending comma (,) should be deleted and Close Square Bracket (]) should
        # be inserted to a new line
        logging.critical("Keyboard Interrupt handling not yet implemented!"\
        " You have to fix the written data manually.")
        sys.exit(0)
    END_TIME = time.time()
    logging.info(f"Time elapsed: {END_TIME - START_TIME:.2f} second(s)")
    sys.exit(0) # Gracefully exit program
