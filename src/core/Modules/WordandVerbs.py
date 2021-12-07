from database import database as db
from WebScrapers import WebScraperWords as wsw
from WebScrapers import WebScraperVerbs as wsv
from Core import WordBigFirstLetter as Wbfl



class word:
     Artikels = ['der','die','das']
     def __init__(self, text:str):
          self.text = Wbfl(text)
          self.Finder()
               
     def __str__(self):
          finalprint = ''
          for i in self.ArtikelTable:
               pri = f"{i['Name']}: {i['Singular']} -- {i['Plural']} \n"
               finalprint += pri
               finalprint  = finalprint
          return finalprint
     ################################
     # Finder
     def Finder(self):
          items = self.DatabaseSearch()
          if len(items) ==0:
               self.Scraper()
          else:
               items = items[0]
               self.Artikel = items[0].split(" ")[0]
               self.Meaning = "-"  # Next Versions
               self.ArtikelTable =[
                    {'Name': 'NOMINATIV','Singular': items[2],'Plural': items[3]},
                    {'Name': 'GENITIV','Singular': items[4],'Plural': items[5]},
                    {'Name': 'DATIV','Singular': items[6],'Plural': items[7]},
                    {'Name': 'AKKUSATIV','Singular': items[8],'Plural': items[9]}
               ]
   
     ################################
     # Scraper --> WebScrapers.py 
     def Scraper(self):
          self.Scraped = wsw(self.text)
          self.Cond = self.Scraped.Cond
          if self.Cond == True:
               self.Artikel = self.Scraped.Artikel

               self.ArtikelTable = self.Scraped.ArtikelTable

               self.Meaning = "-" # Next Versions
               self.DatabaseSave()
          else:
               self.Artikel = "No Artikel Found"
               self.ArtikelTable = []
               self.Meaning = "Not found"
               print("Web Scraping was not successful")
     ################################
     # Database Search Functions
     def DatabaseSearch(self):
          searchitem = self.text
          SearchThrough = ['WordTitle','Meaning','NomSin','NomPlu','GenSin','GenPlu','DatSin','DatPlu','AkkSin','AkkPlu']
          AllWordDatabase = db('AllWords', True,'Words\\')
          items = []
          for col in SearchThrough:
               items = AllWordDatabase.View('AllWordsTable',['*',"{0} REGEXP 'd[a-z][a-z] {1}'".format(col,searchitem)])
               if len(items)>0:
                    print('found')
                    break
               else: 
                    print('not found')
                    continue
          return items
     
     ################################
     # Save in Database and Initial Connection
     def DatabaseSave(self):
          if self.Cond == True:

               At = self.ArtikelTable
               AllWordDatabase = db('AllWords', True,'Words\\')
               AllWordDatabase.Add(['AllWordsTable'],[[
                    (At[0]['Singular'],"-",At[0]['Singular'],At[0]['Plural'],At[1]['Singular'],At[1]['Plural'],At[2]['Singular'],At[2]['Plural'],At[3]['Singular'],At[3]['Plural'])
               ]])
               
                            
               
     
     ################################
     # Static methods

               
     
     ################################
     
                            
class verb:
     def __init__(self, text:str):
          pass
     

word = word('Gemüse')
print(word)
AllWordDatabase = db('AllWords', True,'Words\\')
items =  AllWordDatabase.View('AllWordsTable',['*','null'])
for i in items:
     print(i)