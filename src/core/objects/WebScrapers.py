import requests
from bs4 import BeautifulSoup as bs

class WebscreaperWords:
     def __init__(self,text):
          self.text = WebscreaperWords.WordBigFirstLetter(text)
          self.Cond = True
          self.Scraper()
     
     def Scraper(self):
          Artikels = ['die','das','der']
          Word = self.text
          for artikel in Artikels:
               url = f"https://der-artikel.de/{artikel}/{Word}.html"
               if  requests.get(url).ok:
                    request = requests.get(url)
                    self.Cond = True
                    self.Artikel = artikel
                    self.Html = request.text
                    break
               else:
                    self.Cond = False
     
     def InfoExtractor(self):
          soup = bs(self.Html, 'lxml')
          Meaning = soup.find('h3', class_="mb-5").find('span', class_="").text
          self.Meaning = Meaning.split(' ')[-1]
          ArtikelTable = soup.find('table',class_='table').text.replace("\n"," ").split(" ")
          self.ArtikelTable = [x for x in ArtikelTable if x!='']
          self.ArtikelTable = WebscreaperWords.ArtikelDictionary(self.ArtikelTable)
          
     @staticmethod 
     def WordBigFirstLetter(text):
          if text[0].isupper():
               pass
          else:
               text = text[0].upper() + text[1:]
          return text
     @staticmethod
     def ArtikelDictionary(List:list):
          List.remove('SINGULAR')
          List.remove('PLURAL')
          ArtikelListDictionary = []
          Type = {'Name': '','Plural': '','Singular': ''}
          for item in List:
               
               if item.isupper():
                    Name = item
                    Type['Name'] = Name
                    counter = 0
               else:
                    if item.islower():
                         PlSin = f"{item}"
                    else:
                         PlSin = f"{PlSin} {item}"
                    counter +=1
                    ArtikelListDictionary.append(Type)
          return ArtikelListDictionary
               

                    
          
               
word = WebscreaperWords("Blau")
word.Scraper()
word.InfoExtractor()
print (word.ArtikelTable)
