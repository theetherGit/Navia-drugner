

![Django](https://img.shields.io/badge/Framework-Django-yellow)
![Python](https://img.shields.io/badge/Language-Python-yellow)
![Navia](https://img.shields.io/badge/Company-Navia-lightgrey)
![DRF](https://img.shields.io/badge/API-DRF-yellow)
![BioBert](https://img.shields.io/badge/AI-BioBert-yellowgreen)

# Drug NER

A NER system to identify drug name from text.


## Important Note
    1. It's only work for salt name
    2. Medicine name extractor only works on notebook.
    3. Medicine-ner contains code for Medicine Name Extractor
## Run Locally

Clone the project

```bash
  git clone https://github.com/theetherGit/Navia-drugner
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python manage.py runserver
```


## API Reference

#### Get medicine details

```http
  POST localhost:8000/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `text` | `string` | **Provide a string that contain a drug salt**.




## Tech Stack


**Server:** Python, Django, Django Rest Framework

