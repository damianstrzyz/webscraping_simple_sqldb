import requests
import selectorlib


URL = 'http://programmer100.pythonanywhere.com/tours/'

def scrape(url):
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("webscraping/extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


if __name__ ==  "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)
