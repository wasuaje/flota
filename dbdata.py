#!/usr/bin/python
# -*- encoding: utf-8 -*-

import MySQLdb
from PyQt4.QtSql import *

class Dbdata:
	def __init__(self):
		self.conn = MySQLdb.connect(host='localhost',user='root', passwd='www4214',db='dbnomina')
								
	def check_havedata(self, tabla):
			sql='select count(*) from '+tabla
			c = self.conn.cursor()	
			try:
				#print sql, datos
				c.execute(sql)
			except MySQLdb.Error, e:
				print "Ha habido un Error %d: %s" % (e.args[0], e.args[1])
			for line in c:			
				retorno = line[0]
			if retorno > 0:
				return True
			else:
				return False
				
	def get_data(self, tabla,  id=None ):
			if id == None:				
				#sql='select * from '+tabla+' limit %s'
				sql='select * from '+tabla
			else:
				sql='select * from '+tabla+' where id= %s'
			c = self.conn.cursor()	
			try:
				#print sql
				if id == None:
					c.execute(sql)
				else:
					c.execute(sql, id)
			except MySQLdb.Error, e:
				print "Ha habido un Error %d: %s" % (e.args[0], e.args[1])
			retorno=0
			for line in c:							
					retorno = line
			return retorno
			
	def get_cmb_data(self, tabla,  id=None ):
			if id == None:								
				sql='select * from '+tabla
				#sql='select * from  %u'
			else:
				sql='select * from '+tabla+' where id= %s'
			c = self.conn.cursor()	
			try:
				#print sql
				if id == None:				
					c.execute(sql)
				else:
					c.execute(sql, id)
			except MySQLdb.Error, e:
				print "Ha habido un Error %d: %s" % (e.args[0], e.args[1])
			retorno={}
			for line in c:							
				retorno[line[0]]= [line[1]]					
				#diccionario.update({line[0]:line[1]})

			return retorno					

	def save_empresa(self, datos):
		sql='insert into cf_empresa (nombre,razon_social,rif,nit,email,tlf,fax,ruta_foto) values (%s,%s,%s,%s,%s,%s,%s,%s)'
		c = self.conn.cursor()	
		try:
			#print sql, datos
			c.execute(sql, datos)
		except MySQLdb.Error, e:
			print "Ha habido un Error %d: %s" % (e.args[0], e.args[1])		
		retorno=c.lastrowid
		return retorno
		
	def update_empresa(self, datos):
		sql='update cf_empresa set nombre = %s, razon_social= %s, rif= %s,nit= %s,email= %s,tlf= %s,fax= %s,ruta_foto= %s where id= %s'		
		c = self.conn.cursor()	
		try:
			#print sql, datos
			c.execute(sql, datos)
		except MySQLdb.Error, e:
			print "Ha habido un Error %d: %s" % (e.args[0], e.args[1])
		retorno=c.rowcount
		
	def update_cargo(self, datos):
		sql='update cf_cargo set nombre = %s where id= %s'		
		c = self.conn.cursor()	
		try:
			#print sql, datos
			c.execute(sql, datos)
		except MySQLdb.Error, e:
			print "Ha habido un Error %d: %s" % (e.args[0], e.args[1])
		retorno=c.rowcount

	def save_cargo(self, datos):
		sql='insert into cf_cargo (nombre) values (%s)'
		c = self.conn.cursor()	
		try:
			#print sql, datos
			c.execute(sql, datos)
		except MySQLdb.Error, e:
			print "Ha habido un Error %d: %s" % (e.args[0], e.args[1])
		retorno=c.lastrowid		
		return retorno

	def update_departamento(self, datos):
		sql='update cf_departamento set nombre = %s where id= %s'		
		c = self.conn.cursor()	
		try:
			#print sql, datos
			c.execute(sql, datos)
		except MySQLdb.Error, e:
			print "Ha habido un Error %d: %s" % (e.args[0], e.args[1])
		retorno=c.rowcount

	def save_departamento(self, datos):
		sql='insert into cf_departamento (nombre) values (%s)'
		c = self.conn.cursor()	
		try:
			#print sql, datos
			c.execute(sql, datos)
		except MySQLdb.Error, e:
			print "Ha habido un Error %d: %s" % (e.args[0], e.args[1])
		retorno=c.lastrowid		
		return retorno

	def update_empleado_tipo(self, datos):
		sql='update cf_empleado_tipo set nombre = %s where id= %s'		
		c = self.conn.cursor()	
		try:
			#print sql, datos
			c.execute(sql, datos)
		except MySQLdb.Error, e:
			print "Ha habido un Error %d: %s" % (e.args[0], e.args[1])
		retorno=c.rowcount

	def save_empleado_tipo(self, datos):
		sql='insert into cf_empleado_tipo (nombre) values (%s)'
		c = self.conn.cursor()	
		try:
			#print sql, datos
			c.execute(sql, datos)
		except MySQLdb.Error, e:
			print "Ha habido un Error %d: %s" % (e.args[0], e.args[1])
		retorno=c.lastrowid		
		return retorno

	def update_nomina_tipo(self, datos):
		sql='update cf_nomina_tipo set nombre = %s, dias_pago = %s,nro_periodos = %s  where id= %s'		
		c = self.conn.cursor()	
		try:
			#print sql, datos
			c.execute(sql, datos)
		except MySQLdb.Error, e:
			print "Ha habido un Error %d: %s" % (e.args[0], e.args[1])
		retorno=c.rowcount

	def save_nomina_tipo(self, datos):
		sql='insert into cf_nomina_tipo (nombre,dias_pago,nro_periodos) values (%s,%s,%s)'
		c = self.conn.cursor()	
		try:
			#print sql, datos
			c.execute(sql, datos)
		except MySQLdb.Error, e:
			print "Ha habido un Error %d: %s" % (e.args[0], e.args[1])
		retorno=c.lastrowid		
		return retorno

	def update_banco(self, datos):
		sql='update cf_banco set nombre = %s where id= %s'		
		c = self.conn.cursor()	
		try:
			#print sql, datos
			c.execute(sql, datos)
		except MySQLdb.Error, e:
			print "Ha habido un Error %d: %s" % (e.args[0], e.args[1])
		retorno=c.rowcount

	def save_banco(self, datos):
		sql='insert into cf_banco (nombre) values (%s)'
		c = self.conn.cursor()	
		try:
			#print sql, datos
			c.execute(sql, datos)
		except MySQLdb.Error, e:
			print "Ha habido un Error %d: %s" % (e.args[0], e.args[1])
		retorno=c.lastrowid		
		return retorno
		
	def save_cuenta(self, datos):
		sql='insert into cf_banco_cuenta (nombre,cuenta,cf_banco_id) values (%s,%s,%s)'
		c = self.conn.cursor()	
		try:
			#print sql, datos
			c.execute(sql, datos)
		except MySQLdb.Error, e:
			print "Ha habido un Error %d: %s" % (e.args[0], e.args[1])
		retorno=c.lastrowid		
		return retorno

	def save_empleado(self, datos):
		sql="insert into cf_empleado (codigo,sexo,nombres,apellidos,cedula,rif,tlf_hab,tlf_cel,\
fecha_nacimiento,direccion,direccion2,email,fecha_ingreso,\
cuenta_banco,fecha_registro,fecha_egreso,ruta_foto,cf_cargo_id,\
cf_empleado_tipo_id,cf_departamento_id,cf_nomina_tipo_id,cf_banco_id) \
 VALUES ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s ,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
		c = self.conn.cursor()	
		try:
			#print sql, datos
			c.execute(sql, datos)
		except MySQLdb.Error, e:
			print "Ha habido un Error %d: %s" % (e.args[0], e.args[1])
			#print sql, datos
		retorno=c.lastrowid		
		return retorno		

	def update_empleado(self, datos):
		sql='update cf_empleado set codigo = %s,sexo = %s,nombres = %s ,apellidos = %s,cedula = %s,rif = %s,tlf_hab = %s,tlf_cel = %s,\
fecha_nacimiento = %s,direccion = %s,direccion2 = %s,email = %s,fecha_ingreso = %s, cuenta_banco = %s, fecha_egreso = %s ,\
ruta_foto = %s,cf_cargo_id = %s,cf_empleado_tipo_id = %s,cf_departamento_id = %s,cf_nomina_tipo_id = %s,cf_banco_id = %s \
 where id= %s'		
		c = self.conn.cursor()	
		try:
			#print sql, datos
			c.execute(sql, datos)
		except MySQLdb.Error, e:
			print "Ha habido un Error %d: %s" % (e.args[0], e.args[1])
		retorno=c.rowcount
		return retorno

	def save_sueldo(self, datos):
		sql='insert into cf_sueldo (fecha_desde,mensual,semanal,diario, cf_empleado_id) values (%s,%s,%s,%s,%s)'
		c = self.conn.cursor()	
		try:
			#print sql, datos
			c.execute(sql, datos)
		except MySQLdb.Error, e:
			print "Ha habido un Error %d: %s" % (e.args[0], e.args[1])
		retorno=c.lastrowid		
		return retorno
	


	def delete_record(self, datos):
		#datos=['cf_empresa',id]
		sql="delete from {} where id = {!s} ".format(datos[0], int(datos[1]))
		c = self.conn.cursor()	
		try:
			print sql, datos
			c.execute(sql)
		except MySQLdb.Error, e:
			print "Ha habido un Error %d: %s" % (e.args[0], e.args[1])
		
		return True
			
	def insertar(self, datos, tipo):		
		#tipo nginx,dyn,static						
		if tipo == 'nginx':
			sql='insert delayed into registro ( ip, fecha, metodo, request, cod_retorno, user_agent , resolution, logfile) values (%s,%s,%s,%s,%s,%s,%s,%s)'
		elif tipo == 'dyn': 
			sql='insert delayed into registro ( ip, fecha, metodo, request, cod_retorno, user_agent, logfile) values (%s,%s,%s,%s,%s,%s,%s)'
		elif tipo == 'static': 
			sql='insert delayed into registro ( ip, fecha, metodo, request, cod_retorno, referrer, logfile) values (%s,%s,%s,%s,%s,%s,%s)'			
		else:
			print "no se pudo insertar"
		c = self.conn.cursor()
		try:
			#print sql, datos
			c.execute(sql,datos)
		except MySQLdb.Error, e:
			print "An error occurred:", e.args[0]
			print  "Mientras se insertaba la linea: ",  datos
	
	def bulk_insert(self, filename,tipo,logfile):
		
		if tipo == 'nginx':
			sql="load data local infile '"+filename+"' into table registro fields terminated by '||' ( ip, fecha, metodo, request, cod_retorno, user_agent , resolution, logfile);" 
		elif tipo == 'dyn': 
			sql="load data local infile '"+filename+"' into table registro fields terminated by '||' (ip, fecha, metodo, request, cod_retorno, user_agent, logfile); "
		elif tipo == 'static': 
			sql="load data local infile '"+filename+"' into table registro fields terminated by '||' (ip, fecha, metodo, request, cod_retorno, referrer, logfile);" 
		else:
			print "no se pudo insertar"
		c = self.conn.cursor()
		try:
			#print sql
			c.execute(sql)
		except MySQLdb.Error, e:
			print "Ha habido un Error %d: %s" % (e.args[0], e.args[1])
			#print  "Mientras se insertaba la linea: ",  datos
		
	
	def cerrar(self):
		self.conn.commit()
		self.conn.close()
	
	def vaciar(self):
		c = self.conn.cursor()
		sql='delete from registro'
		c.execute(sql)
		#c.close()
		
	def indices(self, accion):		
		c = self.conn.cursor()
		if accion == 'drop':			
			sql = ['drop index idxregistro_ip on registro', 'drop index idxregistro_fecha on registro', 'drop index idxregistro_logfile on registro']
			#sql = ['drop index if exists idxregistro_ip, idxregistro_fecha, idxregistro_logfile']
		elif accion == 'create':
			sql = ['create index idxregistro_ip on registro (ip)','create index idxregistro_fecha on registro (fecha)', 
			'create index idxregistro_logfile on registro (logfile)']
			#sql=['create index if not exists idxregistro on registro(ip, logfile,  fecha)']
		for i in sql:
			try:
				c.execute(i)
			except MySQLdb.Error, e:
				print "Ha habido un Error %d: %s" % (e.args[0], e.args[1])
		self.conn.commit()
		#self.conn.close()		
		#c.close()

	def get_servers(self):		
		c = self.conn.cursor()
		c.execute('select * from servidor ')  #where id = 1
		diccionario={}
		for line in c:
			diccionario[line[0]]=[line[1], line[2]]
		c.close()
		return diccionario
		
	def get_logfiles(self, srv_id):
		c = self.conn.cursor()
		c.execute('select * from logfile where server = '+ str(srv_id))	#+ ' and id=1 limit 1000'
		diccionario={}
		for line in c:
			#print line
			diccionario[line[0]]= [line[1], line[2]]
		c.close()
		return diccionario
	
	def top_ten(self):
		c = self.conn.cursor()
		sql='SELECT  ip,count(*) from registro group by 1 order by 2 desc limit 10'
		c.execute(sql)
		diccionario={}
		for line in c:
			#print line
			diccionario.update({line[0]:line[1]})
		c.close()
		return diccionario
	
	def max_min_dates(self, ip):
		c = self.conn.cursor()
		#sql="select max(fecha), min(fecha) from registro where ip='"+ip+"'"
		sql="select second(TIMEDIFF(max(fecha),min(fecha))) from registro where ip='"+ip+"'"
		#print sql
		c.execute(sql)
		for line in c:
			c.close()
		#self.conn.close()
		return line
	
	def wierd_agents(self):
		c = self.conn.cursor()
		sql="select ip, count(ip),user_agent from registro where length(user_agent)<20 or  user_agent like '%.com%' and logfile = 1 group by 3 order by 2 desc limit 100"
		#print sql
		c.execute(sql)
		diccionario={}
		for line in c:
			#print line
			diccionario.update({line[0]:[line[1], line[2]] })
		c.close()
		return diccionario


class QDbdata():
	def __init__(self):
		self.db = QSqlDatabase.addDatabase("QMYSQL")
		self.db.setHostName("localhost")
		self.db.setDatabaseName("dbnomina")
		self.db.setUserName("root")
		self.db.setPassword("www4214")
		
	def open(self):
		self.db.open()
	
	def close(self):
		self.db.close()
		self.db.removeDatabase('dbnomina')
		#_database = QSqlDatabase()
		
		
