# Daraz Scrapper Using Selenium

## Setup and Installation
#### Clone the repository
```
git clone https://github.com/talha-amir/Daraz-Scrapper-Using-Selenium-Python.git .
cd Daraz-Scrapper-Using-Selenium-Python
```
#### Setup Virtual Environment (Optional)
```
pip install virtualenv
python -m venv .venv
cd .venv/scripts && activate.bat 
cd ../../
```
#### Installing the Libraries
```
pip install -r requirements.txt
```
#### Usage

```
python daraz.py -h
```
Ouput:
```
usage: daraz.py [-h] [--pages PAGES] [--category CATEGORY]

Scraps product data from Daraz for a s specific category

optional arguments:
  -h, --help           show this help message and exit
  --pages PAGES        Total Number of Pages to Scrap Leave Empty for max pages
  --category CATEGORY  Name of Sub-Category to Scrap Leave Empty for Default
```
Sample Usage:
```
python daraz.py --pages 1
```

