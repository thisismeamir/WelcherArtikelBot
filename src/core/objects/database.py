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
        self.Tables = []
        if init:
            self.Initializing()
        else:
            pass
          


    ######################################################################
    # Action: Executes the Action given as argument.
    # This method will be separated once the code is bigger.
    def Action(self, ACT:list, INP = []):
        """ This functions is the core function of database jobs, any action it recieves will be done with sqlite 3 """
        assert len(ACT) >= len(INP), "This cannote be possible"
        cursor = self.Connection.cursor()
        if len(INP) == 0:
            for action in ACT:
                cursor.execute(action)
                self.CommitChanges()
        elif len(INP) == len(ACT):
            for id, action in enumerate(ACT):
                cursor.executemany(action, INP[id])
                self.CommitChanges()
        else:
            for id, Input in enumerate(INP):
                cursor.executemany(ACT[id], Input)
                self.CommitChanges()
                lastID = id

            while lastID < len(ACT):
                cursor.execute(ACT[lastID])
                self.CommitChanges()
                lastID += 1
        print("Completed!")

    # Action subMethods: Creates the sqlite3 Table arguments to create a table using Action() 
    def CreateTable (self, TABNAME: str, COLs: list):
        """ Creates a new table given a table name and a list of dictionaries like 'name': '', 'type' '' """
        columnArgument = ""
        for column in COLs:
            columnArgument = columnArgument +  column['name'] + " " + column['type'] + ",\n" 
        columnArgument = columnArgument[:-3]
        
        # ACTArgument: The final argument that we will pass Action() 
        ACTArgument = f""" CREATE TABLE IF NOT EXISTS {TABNAME}(
        {columnArgument})"""
        self.Tables.append(TABNAME)
        print("The Args have been created")
        print(ACTArgument)

        self.Action([ACTArgument])


    # Action subMethods: Recieve Table info
    def TableView (self, TABNAME: str, Ins:str, datas= False):
        assert TABNANE in self.Tables, "There is no such table here."

        ACTArgument = ''
        if Ins == "All" and datas == False:
            
            



   
          
    ######################################################################

    # Initialize the database (creates or connects the database)
    def Initializing(self):
        """ Initializing the database (basically connecting) """
        self.Connection = sql.connect(f"..\..\databases\{self.Name}.db")
        


    # Commiting db changes
    def CommitChanges(self):
        """ Commiting Changes you did in a database """
        self.Connection.commit()
          

    # Closing Database
    def Closing(self):
        """ Closing a database you have used initializing() on """
        self.Connection.close()

    ##################################
    # Static methods
    @staticmethod
    def ValuesNumber(repeate):
        i =  1
        Values = ""
        while i < repeate:
            Values = Values + "?,"
            i += 1
        Values = Values + "?"
        return Values
          
                    
data = database('thenewone2',True)
data.CreateTable("NewTable", [
    {'name': 'name', 'type': 'text'},
    {'name': 'lastename', 'type': 'text'}
    ])

