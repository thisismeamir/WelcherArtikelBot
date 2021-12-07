# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as bs
from Core import WordBigFirstLetter as Wbfl
from Core import UmlautCorrectors as Uml


class WebScraperWords:
     def __init__(self,text):
          self.text = Wbfl(text) 
          self.Cond = True
          self.Scraper()
          if self.Cond == True:
               self.InfoExtractor()
          
     
     def Scraper(self):
          Artikels = ['die','das','der']
          Word = Uml(self.text)
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
          ArtikelTable = soup.find('table',class_='table').text.replace("\n"," ").split(" ")
          self.ArtikelTable = [x for x in ArtikelTable if x!='']
          self.ArtikelTable = WebScraperWords.ArtikelDictionary(self.ArtikelTable)
          
     @staticmethod
     def ArtikelDictionary(List:list):
          List.remove('SINGULAR')
          List.remove('PLURAL')
          ArtikelListDictionary = []
          Type = {'Name': '','Singular': '','Plural': ''}
          SaveTemp = []
          for item in List:
               if item.isupper():
                    Name = item
                    Type['Name'] = Name
                    counter = 0
               else:
                    if item.islower():
                         word = ''
                         artikel = f"{item}"
                    elif item == "-":
                         counter += 1
                         word = "-"
                    else:
                         word = Uml(f"{artikel} {item}")
                    counter +=1
               if counter == 2 or counter == 4:
                    SaveTemp.append(word)
               if counter == 4:
                    Type['Name']     = Name
                    Type['Singular'] = SaveTemp[0]
                    Type['Plural']   = SaveTemp[1]
                    ArtikelListDictionary.append(Type)
                    Type = {'Name': '','Singular': '','Plural': ''}
                    SaveTemp = []
                    counter = 0
          return ArtikelListDictionary

          # Here we will write the code that detects umlaut correctly and changes it accordingly
          
class WebScraperVerbs:
     pass
                    
          
               
                    
word = WebScraperWords('Obst')
               