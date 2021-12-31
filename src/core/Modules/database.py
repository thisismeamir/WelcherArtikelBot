# Imports
import sqlite3 as sql
import re
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
        columnArgument = columnArgument[:-2]
        
        # ACTArgument: The final argument that we will pass Action() 
        ACTArgument = f""" CREATE TABLE IF NOT EXISTS {TABNAME}(
        {columnArgument})"""
        self.Tables.append(TABNAME)
        print("The Args have been created")
        print(ACTArgument)

        self.Action([ACTArgument])


    # Action subMethods: Recieve Table info
    def View(self, TABname:str, Ins = [[],[]]):
        """This function is used to view A Tables Data, because this method needs to be fetched after executing
        we didn't use the Action() method in this particular method"""
        assert len(Ins) == 2, "There is no such table here."

        cursor = self.Connection.cursor()

        argument = ""
        if TABname == "All":
            argument = f"SELECT name FROM {self.Name} WHERE type='table'"
            cursor.execute(argument)
            items =  cursor.fetchall()
            return items
        
        else:
            if Ins[1] != "null":
                Where = f"WHERE {Ins[1]}"
            else: 
                Where = ""
            argument = f"SELECT {Ins[0]} FROM {TABname} {Where}"
            print (argument)
            cursor.execute(argument)
            items =  cursor.fetchall()
            return items
        
    
    # Action subMethods: Adds new Data to Table
    def Add(self,TABname:list, Inputs:list ):
        """
        This Method Adds a New Data to the table 
        """
        ActionList = []
        
        for id,table in enumerate(TABname):
            Condition = self.CheckforItem(Inputs[id][0],table)
            if Condition == False:
                
                Values = database.ValuesNumber(len(Inputs[id][0]))
                ACTArgument = f"INSERT INTO {table} VALUES({Values})"
                ActionList.append(ACTArgument)
            else:
                pass

        self.Action(ActionList,Inputs)
    


    # Action subMethods: Updating an existing data in table:
    def Update(self,TABname:list, Set: list, Where:list):
        assert len(TABname) == len(Set) == len(Where), "the three argument shall have the sane length"
        """
        Updates a table
        Set [[
        {'column': 'columnname', 'setto': 'what to set'},...
        ],
        [
        {'column': 'columnname', 'setto': 'what to set'},...
        ]...]
        Where [
        'Where we should set the ith set of dictionaries in Set',
        ...
        ]
        """
        ActionList = []
        for id,table in enumerate(TABname):
            SETArgument = ''
            for Object in Set[id]:
                Objsets = f"'{Object['setto']}'"
                SETArgument = SETArgument +  Object['col'] + " = " + Objsets + ",\n" 
            SETArgument = SETArgument[:-2]

            ACTArgument = f"""
                            UPDATE {table}
                            SET {SETArgument}
                            WHERE {Where[id]}
                           """
            ActionList.append(ACTArgument)
            self.Action(ActionList)
            
    # Action subMethods: Delete an existing data in table:
    def Delete(self, TableWhere: list):
        ActionList = []
        for table in TableWhere:
            ACTArgument = f"DELETE FROM {table['table']} WHERE {table['where']}"
            ActionList.append(ACTArgument)
        self.Action(ActionList)
    
    def CheckforItem(self, Item, Tablename):
        SearchThrough = self.GetColumns(Tablename)
        SearchItem  = Item
        items = []
        for col in SearchThrough:
            for item in SearchItem:
                if item == "-" or item == 0:
                    continue
                else:
                    print(item)
                    item = item.split(" ")
                    item = item[1]
                    print(item)
                    items = self.View(Tablename,['*',"{0} REGEXP 'd[a-z][a-z] {1}'".format(col,item)])
                    if len(items)>0:
                        Condition = True
                        print('found')
                        break
                    else:
                        Condition = False
                        print('not found')
                        continue
        return Condition
            
    def GetColumns(self,Tablename):
        cursor = self.Connection.execute(f'select * from {Tablename}')
        names = list(map(lambda x: x[0], cursor.description))
        return names
        
    ######################################################################

    # Initialize the database (creates or connects the database)
    def Initializing(self):
        """ Initializing the database (basically connecting) """
        self.Connection = sql.connect(f"./databases/{self.Name}.db")
        self.Connection.create_function("REGEXP", 2, database.regexp)
        


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
    @staticmethod
    def regexp(expr, item):
        try:
            reg = re.compile(expr)
            return reg.search(item) is not None
        except:
            return False  
                    
