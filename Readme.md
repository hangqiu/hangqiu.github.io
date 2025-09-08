Prerequisites
* bibtexparser

Commands

* Edit mypub.bib
```python
python3 ./assets/bib2yml.py --bibtex_fp ./assets/mypub.bib
```

```shell
curl -L https://raw.githubusercontent.com/UCR-CISL/UCR-CISL.github.io/main/_data/news.yml -o _data/lab_news.yml
bundle update 
jekyll build
jekyll serve
``` 

Alternatively, there is a git action that is fetching the lab news automatically every day.

publish the _site folder
