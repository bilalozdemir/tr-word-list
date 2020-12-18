# A Few Turkish Words
`words.json` contains all the **92407 words** in the Turkish Goverment's official online dictionary. Previous version of this file `words_meanings_big.txt` (which contains approximately 48k words) is still being kept in this repository in case of someone would want to practice with a smaller data or a different type of file.

**BE AWARE BEFORE EXECUTING THE SCRIPT**
It takes **LOTS** of time to execute **92407** request.

The text file is formatted as shown below:
```
{word}**{meaning 1}\n{meaning 2}\n%%\n
```

The json file is formatted as shown below (prettified):
```
[
  {
    'word': <word 1>,
    'meanings': [
      <meaning 1>,
      <meaning 2>,
      ...
    ]
},
  {
    'word': <word 2>,
    'meanings': [
      <meaning 1>,
      <meaning 2>,
      ...
    ]
},
...
]
```

## TODO

  * Multi-threaded Requests will be implemented
  * Handling `KeyboardInterrupt` with fixing data before exit.

## Intentions on this Work
This work intented to be a little source of most-used Turkish words (and meanings of most of them) for any kind of work requires plenty of words and an example of scraping data from a website.

## Examples of Processed Data
Some of the Data Science practices (or whatever you call them) could be made using the given data are like:

* Items in `words.json` has an **average length of ~10 characters.**

* The longest item with spaces is **'bir sıçrarsın çekirge, iki sıçrarsın çekirge, sonunda yakalanırsın çekirge (veya üçüncüsünde avucuma düşersin çekirge)'** and has a **length of 101 characters** (except whitespaces and punctuations).

* The longest item without whitespaces is **'belirginleştirilebilmek'** and has a **length of 23 characters.**

* **The letter 'K'** is the most used letter as the first letter of the items with **10749 times** and **the letter 'Ğ'** is the least used letter as the first letter of the items with **just once.**

* **The letter 'A'** is the most used letter in the items with **120719 times** and **the letter 'J'** is the least used letter in the items with **970 times.**

* Example graphs:

![Graph of Letters vs. First Letters](/files/graph_1.png)
![Graph of Letters vs. Letters Used](/files/graph_2.png)
![Graph of Lengths vs. Words on the Length](/files/graph_3.png)

### Used

  * [`httpx`](https://github.com/encode/httpx/) New generation http library for python
  * [`orjson`](https://github.com/ijl/orjson) A fast json library for python
  * `logging`
  * `time`

### Sources
* [Wiktionary - Tr](https://www.wiktionary.org.tr) - 48k words (previous version, with **BS4**)
* [Türk Dil Kurumu](http://sozluk.gov.tr/) - 92406 words

### Disclaimer (TR)
5846 sayılı Fikir ve Sanat Eserleri kanununun 35. maddesi (İktibas Serbestisi) doğrultusunda yukarıda belirtilen alenileşmiş eserlerden bazı kısımlar derlenerek ticari amaç güdülmeksizin işlenebilir bir kelime veri tabanı oluşturulmuş olup telif hakkı sahiplerinin umuma arz hakları hiçbir şekilde ihlal edilmemiştir.

### LICENSE
You can see the license of the word list [here.](https://creativecommons.org/licenses/by-sa/4.0/)
