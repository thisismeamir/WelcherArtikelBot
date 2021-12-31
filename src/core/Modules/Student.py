from database import database as db
from WordandVerbs import word 

class student: 
     def __init__(self,name:str, id:str, level:str, classcode = 0):
          self.Name = name
          self.Id   = id
          self.Level = level
          self.ClassCode = classcode
          
          
     def DatabaseInitialized(self):
          TableId = f"Std{self.Id}{self.Name}"
          self.Database = db('eachStudentWords', True)
          self.Database.CreateTable(f'{TableId}',[
               {'name': 'WordTitle',     'type': 'text'},
               {'name': 'Meaning',  'type': 'text'},
               {'name': 'NomSin', 'type': 'text'},
               {'name': 'NomPlu', 'type': 'text'},
               {'name': 'GenSin', 'type': 'text'},
               {'name': 'GenPlu', 'type': 'text'},
               {'name': 'DatSin', 'type': 'text'},
               {'name': 'DatPlu', 'type': 'text'},
               {'name': 'AkkSin', 'type': 'text'},
               {'name': 'AkkPlu', 'type': 'text'},
               {'name': 'points', 'type': 'real'}
               ])

     
     def WordAsked(self, NewWord:str):
          self.newword = ''
          self.newword = word(NewWord)
          if self.newword.Cond:
               self.Database = db('eachStudentWords', True)
               TableId = f"Std{self.Id}{self.Name}"
               At = self.newword.ArtikelTable
               self.Database.Add([TableId], [[
                    (At[0]['Singular'],"-",At[0]['Singular'],At[0]['Plural'],At[1]['Singular'],At[1]['Plural'],At[2]['Singular'],At[2]['Plural'],At[3]['Singular'],At[3]['Plural'],0)
               ]])
               items = self.Database.View(TableId,['*','null'])
               return At
               
