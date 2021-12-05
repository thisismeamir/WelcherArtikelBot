from database import database as db

################################################################
# Students Databases

Students = db.database('AllStudents',True,'Students\\')
Students.CreateTable("AllStudentsTable",[
    {'name': 'id',        'type': 'text'},
    {'name': 'Name',      'type': 'text'},
    {'name': 'ClassCode', 'type': 'text'},
    {'name': 'level',     'type': 'text'}
])