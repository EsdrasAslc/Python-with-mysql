import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="PASSWORD",
  database="advogados"
)

def delete_on_db(oab):
  mycursor = mydb.cursor()

  sql = ('DELETE FROM registros WHERE oab = %s')

  mycursor.execute(sql, oab)

def search_on_db(oab):

  if oab == '*':

    mycursor = mydb.cursor()

    sql = ('SELECT * FROM registros ')
    
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
      print(x)

    return 0  

  if len(oab) == 10:
    mycursor = mydb.cursor()

    sql = ('SELECT * FROM registros WHERE oab = %s')
    
    mycursor.execute(sql, (oab,))

    myresult = mycursor.fetchall()

    if myresult:
      return myresult[0]
    else: 
      return 'Não existe registro com esse OAB'
    
  else:
    return 'O número da OAB precisa ter 10 caracteres. ex: BA12345678'

def create_on_db(name, address, oab):

  if len(oab) != 10:
    return 'Erro! O número da OAB precisa ter 10 caracteres. ex: BA12345678'
  
  sql = 'INSERT INTO registros (name,address, oab) VALUES (%s, %s, %s)'
  val = (name,address,oab)

  mycursor = mydb.cursor()
  mycursor.execute(sql, val)
  
  mydb.commit()

  return mycursor.rowcount, "record inserted."

def edit_on_db(oab, atribute, value):

  if atribute == 1:
    sql = 'UPDATE registros SET name = %s WHERE oab = %s'
    val = (value, oab)
  elif atribute == 2:
    sql = 'UPDATE registros SET address = %s WHERE oab = %s'
    val = (value, oab)    
  elif atribute == 3:
    sql = 'UPDATE registros SET oab = %s WHERE oab = %s'
    val = (value, oab)  

  mycursor = mydb.cursor()
  mycursor.execute(sql, val)
  
  mydb.commit()

