from WebScrapers import WebScraperWords as wsw
from WebScrapers import WebScraperVerbs as wsv



class word:
     Artikels = ['der','die','das']
     def __init__(self, text:str):
          self.text = text
          self.Scraper()
          
          
          
     ################################
     # Scraper --> WebScrapers.py 
     def Scraper(self):
          self.Scraped = wsw(self.text)
          self.Cond = self.Scraped.Cond
          if self.Cond == True:
               self.Artikel = self.Scraped.Artikel
               self.ArtikelTable = self.Scraped.ArtikelTable
               self.Meaning = self.Scraped.Meaning
          else:
               self.Artikel = "No Artikel Found"
               self.ArtikelTable = "No Acleartikel Found"
               self.Meaning = "No Meaning Found"
               print("Web Scraping was not successful")
     
     ################################
     
     ################################
     # Static methods

               
     
     ################################
     
                            
class verb:
     def __init__(self, text:str):
          pass
     

NewWord2 = word('Österreicher')
print(NewWord2.ArtikelTable)
