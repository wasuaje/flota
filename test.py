from dbdata import *
import sys
from PyQt4 import QtCore, QtGui, QtSql

db=QDbdata()
db.open()

sql='select * from cf_banco'
rs = QSqlQuery(sql,db.db)

print dir(rs)
for i in range(0,rs.numRowsAffected()):
	rs.next()	
	print rs.value(0).toString(), rs.value(1).toString()

datos={}	
datos=['venezolanso',4]
print datos
sql2 = "update cf_banco set nombre='{0[0]}' where id = {0[1]}".format(datos)
print sql2
#nombre='Venezola3nos' where id = 4"
rs2 = QSqlQuery(sql2,db.db)	
#rs2.exec_(sql2)
print "afectadas  " + str(rs2.numRowsAffected())
#print "ultima insertada  " + str(rs2.lastInsertId().toString())

db.close()
#-1 error
# 0 no hay cambias
#>0 afectadas
