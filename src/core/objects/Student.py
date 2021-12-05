import database as db

class student: 
     def __init__(self,name:str, id:str, level:str, classcode = 0):
          self.Name = name
          self.Id   = id
          self.Level = level
          self.ClassCode = classcode
          Students.Add(['AllStudentsTable'],[[
          (self.Id,self.Name,self.ClassCode,self.Level)
          ]])
     
student = student('amir','123231','A1','23')
print(Students.View('AllStudentsTable',['name,rowid,id','null']))