# VSCO Scraper
This is a web scraper built using Selenium that allows users to enter a list of VSCO usernames, and then downloads their 14 most recent photos.

## Prerequisites
* Python 3.7
* Selenium
* Chromedriver

## How To Run

Clone the repository on to your local machine
```bash
git clone https://github.com/krishras23/vsco/
```


Install the necessary packages using pip
```bash
pip3 install -r requirements.txt
```

Download [ChromeDriver](https://chromedriver.chromium.org/downloads) and make sure it is compatible with your chrome browser. Replace line 4 of the code, and modify it using the PATH of your chromedriver. Add the path of ChromeDriver to your system PATH.

Enter the list of usernames seperated ["x", "y" "z"]

Finally, run the scraper. 
```bash
python3 extract.py
```
