# Basic Upwork Scraping Script

## Purpose

* Visit upwork.com login page
* submit username
* submit password
* submit verification question if asked
* collect main page HTML
* extract crucial data from main page
* create JSON file of extracted data

## Set it up

Change the name of configTemplate.txt to config.ini and update <placeholders> with real values

## Run it

In a new virtualenv install all your depenedencies

```
pip install -r requirements.txt
```

Run the script in your command line

```
python fetch.py
```