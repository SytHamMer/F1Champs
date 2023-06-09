import scrapy
from selenium.webdriver.common.by import By
from selenium import webdriver
import json
DOWNLOAD_DELAY = 3
USER_AGENT = 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'

class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['fr.wikipedia.org']
    start_urls = ['https://fr.wikipedia.org/wiki/Palmar%C3%A8s_du_championnat_du_monde_de_Formule_1']


#Fonction qui récupère sur la page wikipedia officielle de la F1 l'ensemble des noms, années et liens wikipédias
#des différents champions utilisants Scrapy
#Le résultat est enregistré dasn le fichier firstdata.json
    def parse(self, response):
        table = response.xpath('//table[@class="wikitable"]')
        rows = table.xpath('.//tr')

        for row in rows:
            cells = row.xpath(".//td")
            year = cells[0].xpath('string()').get()
            champName = cells[1].xpath('string()').get()
            champURL = cells[1].xpath('.//a[not(@class="image")]/@href').get()
            link = "https://fr.wikipedia.org" + str(champURL)
      
            if champName !='\n':

                yield{
                    "Year": year,
                    "Champion" : champName,
                    "Wiki_Page" : link,
                }

#Cette fonction utilise Selenium afin d'accéder à différentes pages wikipedia.
#On commence par ouvrir le firstdata.json et récupérer tous les liens
#Pour chacun de ces liens on scrap les informations nous permettant d'obtenir la date de naissance
#Et on stock dans un fichier data.json
def get_birthdate(file):
    res = []
    with open(file,'r') as json_file:
        data = json.load(json_file)
    DRIVER_PATH = 'C://Users//mathy//Desktop//Code//chromedriver.exe'
    browser =  webdriver.Chrome(executable_path=DRIVER_PATH)
    for i in data:
        browser.get(i['Wiki_Page'])
        birthdate = browser.find_element(By.CSS_SELECTOR, 'time.nowrap.date-lien.bday').get_attribute('datetime')
        i['birthdate'] = birthdate
        t = browser.find_element(By.ID, 'mw-content-text').find_element(By.CLASS_NAME, 'mw-parser-output')
        pole = t.find_element(By.XPATH, '//div//table[4]//tbody//tr[3]//td').text
        i["pole"] = pole
        res.append(i)
    jsonString = json.dumps(res)
    jsonFile = open('data.json','w')
    jsonFile.write(jsonString)
    jsonFile.close()


if __name__ == "__main__":
    get_birthdate('firstdata.json')