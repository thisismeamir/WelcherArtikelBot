# Imports
import sqlite3 as sql
from sqlite3.dbapi2 import connect


# This is the class database,which we will use to talk to our databases 
# without being worried about SQL library itself
# When you create an instance of this class you have to give it a name
# Then you have to run the Initializing method on it
# After That,you just need to use the action method to execute the commands you want
# just pass the method all the commands you want to run in order in a list
class database:


     def __init__(self,name:str, init= False):
          self.Name = name
          if init:
               self.Initializing()
          else:
               pass
          


     ######################################################################
     # Action: Executes the Action given as argument.
     # This method will be separated once the code is bigger.
     def Action(self, ACT:list):
          for action in ACT:
               cursor = self.Connection.cursor()
               cursor.execute(action)
          print(f"{self.Name} has been successfully updated.")
     
     # Action: CREATES TABLE
     def CreateTable(self, tableName:str, columns:list):
          columnWriter = ""
          for column in columns:
               columnWriter = ColumnWriter + ",\n" + column['name'] + " " + column['type']
          self.Action([f""" CREATE TABLE {tableName} (
                      {columnWriter}
                      ) """])
     ######################################################################

     # Initialize the database (creates or connects the database)
     def Initializing(self):
          self.Connection = sql.connect("src\databases\{0}.db".format(self.Name))


     # Commiting db changes

     def CommitChanges(self):

          self.Connection.commit()
          

     # Closing db

     def Closing(self):

          self.Connection.close()

testingdb = database("starting")
testingdb.Initializing()
testingdb.action(["""
                  CREATE TABLE customers (
             first_name  text,
             last_name text,
             email text
                    )
                  """])