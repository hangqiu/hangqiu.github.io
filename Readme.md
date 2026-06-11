### Git Actions
- Fetch the _data/lab_news.yml from UCR-CISL.github.io automatically every day.
- Upon push of assets/services.bib, convert to _data/service.yml 


Prerequisites
* bibtexparser

Commands

* Edit mypub.bib
```python
python3 ./assets/bib2yml.py --bibtex_fp ./assets/mypub.bib
```