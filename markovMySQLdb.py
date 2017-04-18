# coding: utf8
import MySQLdb
import codecs

charactersToKeep  = [32,33,39,44,45,46,48,49,50,51,52,53,54,55,56,57,63]
charactersToKeep += [i for i in range(65,91) ]
charactersToKeep += [i for i in range(97,123)]
with codecs.open('myCorpus.txt', encoding='utf8') as f:
    myString = ''
    for line in f:
        line = ''.join([c for c in line if ord(c) in charactersToKeep])
        myString += ' ' + line
        myString = myString.strip()
    myString = myString.replace('  ', ' ')
document = myString.replace("'", "_")

description = 'aliceInWonderland'

db = MySQLdb.connect("localhost","dondi","","nlpText" )
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS Documents")
db.commit()
db.close()

db = MySQLdb.connect("localhost","dondi","","nlpText" )
cursor = db.cursor()
sql = """CREATE TABLE Documents (
         description  CHAR(255)   NOT NULL,
         document     MEDIUMTEXT  NOT NULL
         )
      """
cursor.execute(sql)
db.commit()
db.close()

db = MySQLdb.connect("localhost","dondi","","nlpText" )
cursor = db.cursor()
sql = "INSERT INTO Documents (description, \
       document) \
       VALUES ('%s', '%s')" % \
       (description, document)
cursor.execute(sql)
db.commit()
db.close()
