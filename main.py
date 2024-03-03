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

def store (extracted):
    with open("webscraping/data.txt", "a") as file:
        file.write(extracted + "\n")

def read(extracted):
    with open("webscraping/data.txt", "r") as file:  
        return file.read()  

def send_email():
    print("Email was sent")

if __name__ ==  "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)
    
    content = read(extracted)
    if extracted != "No upcoming tours":
        if extracted not in content:
            store(extracted)
            send_email()
