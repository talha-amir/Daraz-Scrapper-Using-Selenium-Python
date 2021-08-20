# Daraz Scrapper Using Selenium Python

## Setup and Installation
#### Clone the repository
```
git clone https://github.com/talha-amir/Daraz-Scrapper-Using-Selenium-Python.git
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
#### Output:
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

#### Chrome Driver:
The current Chrome Driver is supported by Chrome version 92,if you have a different version of Chrome you can refer the following:
- If you are using Chrome version 93, please download 
[ChromeDriver 93.0.4577.15](https://chromedriver.storage.googleapis.com/index.html?path=93.0.4577.15/)
- If you are using Chrome version 92, please download [ChromeDriver 92.0.4515.107](https://chromedriver.storage.googleapis.com/index.html?path=92.0.4515.107/)

- If you are using Chrome version 91, please download [ChromeDriver 91.0.4472.101](https://chromedriver.storage.googleapis.com/index.html?path=91.0.4472.101/)

Python Version : 3.9.6
