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
Words = db.database('AllWords', True,'Words\\')
Words.CreateTable("AllWordsTable",[
    {'name': 'word',     'type': 'text'},
    {'name': 'Meaning',  'type': 'text'},
    {'name': 'Artikels', 'type': 'text'}
])