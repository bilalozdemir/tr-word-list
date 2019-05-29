# A Few Turkish Words
`words.json` contains all the **92406 words** in the Turkish Goverment's official online dictionary. Previous version of this file `words_meanings_big.txt` (which contains approximately 48k words) is still being kept in this repository in case of someone would want to practice with a smaller data or a different type of file.

The text file is formatted as shown below:
```
{word}**{meaning 1}\n{meaning 2}\n%%\n
```
The json file is formatted as shown below:
```
[
{'word': <word 1>, 'meanings': [<meaning 1>, <meaning 2>, ...]},
{'word': <word 2>, 'meanings': [<meaning 1>, <meaning 2>, ...]},
...
]
```

Usage of the given script (old version) has been explained in the docstrings of `scraper.py`.

## Intentions on this Work
This work intented to be a little source of most-used Turkish words (and meanings of most of them) for any kind of work requires plenty of words and an example of scraping data from a website.

## Examples of Processed Data
Some of the Data Science practices (or whatever you call them) could be made using the given data are like:

* Words in `words.json` has an **average length of ~10 characters.**

* The longest word with spaces in it is **'bir sıçrarsın çekirge, iki sıçrarsın çekirge, sonunda yakalanırsın çekirge (veya üçüncüsünde avucuma düşersin çekirge)'** and has a **length of 101 characters** (except non-word characters).

* The longest word without spaces in it is **'belirginleştirilebilmek'** and has a **length of 23 characters.**

* **The letter 'K'** is the most used letter as the first letter of the words with **10749 times** and **the letter 'Ğ'** is the least used letter as the first letter of the words with **just once.**

* **The letter 'A'** is the most used letter in the words with **120719 times** and **the letter 'J'** is the least used letter in the words with **970 times.**

* Example graphs:

![Graph of Letters vs. First Letters](/files/graph_1.png)
![Graph of Letters vs. Letters Used](/files/graph_2.png)
![Graph of Lengths vs. Words on the Length](/files/graph_3.png)

### Used
* [Scrapy](https://scrapy.org/) - To scrape the words, took 6 hours and 51 minutes to scrape 92k words (codes not necessary)

* [Matplotlib](https://matplotlib.org/) - To create plot examples

* [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - To scrape couple of websites (previous version)

* [SQLAlchemy](https://www.sqlalchemy.org/) - To build a fancy :bowtie: database and data model (not pushed here)

* And lots of brute-force :innocent:

### Sources
* [Wiktionary - Tr](https://www.wiktionary.org.tr) - 48k words (previous version, with **BS4**)
* [Türk Dil Kurumu](http://sozluk.gov.tr/) - 92406 words (current version, with **Scrapy**)

### Disclaimer (TR)
5846 sayılı Fikir ve Sanat Eserleri kanununun 35. maddesi (İktibas Serbestisi) doğrultusunda yukarıda belirtilen alenileşmiş eserlerden bazı kısımlar derlenerek ticari amaç güdülmeksizin işlenebilir bir kelime veri tabanı oluşturulmuş olup telif hakkı sahiplerinin umuma arz hakları hiçbir şekilde ihlal edilmemiştir.

### LICENSE
You can see the license of the word list [here.](https://creativecommons.org/licenses/by-sa/4.0/)
