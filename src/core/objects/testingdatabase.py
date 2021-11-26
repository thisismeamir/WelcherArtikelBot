from database import database as db
datas = db("name", True)



datas.InsertTableData(["mydata2"], [
     [
          ('amir',19),
          ('reza',20)
     ]
     ])

items = datas.RecvTableData(["*"], ["mydata2"], ["mydataname == 'rowid==2'"])
print(items)


