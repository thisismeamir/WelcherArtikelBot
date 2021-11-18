import sqlite3 as sql

from sqlite3.dbapi2 import connect


class database:

     def __init__(self,name:str):

          self.Name = name
          
     def __

     # Action: Executes the Action given as argument.
     def action(self, ACT:list):
          for action in ACT:
               cursor = self.Connection.cursor()
               cursor.execute(action)
          print(f"{self.Name} has been successfully updated.")
          

     # Initialize the database (creates or connects the database)

     def initializing(self):
          self.Connection = sql.connect(f"src\databases\{self.Name}.db")

     # Commiting db changes
     def CommitChanges(self):
          self.Connection.commit()
          
     # Closing db
     def closing(self):
          self.Connection.close()
          
testingdb = database("testingdb")