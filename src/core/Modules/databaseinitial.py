from database import database as db

################################################################
# Initial Databases and Models

Students = db('AllStudents',True)
Students.CreateTable("AllStudentsTable",[
    {'name': 'id',        'type': 'text'},
    {'name': 'Name',      'type': 'text'},
    {'name': 'ClassCode', 'type': 'text'},
    {'name': 'level',     'type': 'text'}
])
Words = db('AllWords', True)
Words.CreateTable("AllWordsTable",[
    {'name': 'WordTitle',     'type': 'text'},
    {'name': 'Meaning',  'type': 'text'},
    {'name': 'NomSin', 'type': 'text'},
    {'name': 'NomPlu', 'type': 'text'},
    {'name': 'GenSin', 'type': 'text'},
    {'name': 'GenPlu', 'type': 'text'},
    {'name': 'DatSin', 'type': 'text'},
    {'name': 'DatPlu', 'type': 'text'},
    {'name': 'AkkSin', 'type': 'text'},
    {'name': 'AkkPlu', 'type': 'text'}
])
