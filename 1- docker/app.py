import time
from crate import client
import csv
import random
from datetime import datetime
import os.path as path


def connectCrate():
  time.sleep(10)
  
  # 1- Creamos la conexion
  try:
     connection = client.connect('crate:4200',timeout=5,error_trace=True,backoff_factor=0.2)
     print("CONNECT OK")
  except Exception as err:
     print("CONNECT ERROR: %s" % err)

  # 2- Cogemos el cursor
  cursor = connection.cursor()
  
  # 3- Creamos una tabla llamada peliculas
  try:
     print("CREATE TABLE: create table peliculas(id int, titulo text, ano int)")
     cursor.execute("CREATE TABLE peliculas(id int, titulo text, ano int)")
     print("CREATE TABLE OK")
  except Exception as err:
     print("No se ha podido crear la tabla")
     
  # 4- Añadimos 10 peliculas a la tabla
  try:
     print ("INSERTS:")
     cursor.execute("insert into peliculas values (1, 'Pinocho',1940)")
     print ("\tinsert into peliculas values (1, 'Pinocho',1940)")
     
     cursor.execute("insert into peliculas values (2, 'Dumbo',1941)")
     print("\tinsert into peliculas values (2, 'Dumbo',1941)")
     
     cursor.execute("insert into peliculas values (3, 'Peter Pan',1953)")
     print("\tinsert into peliculas values (3, 'Peter Pan',1953)")
     
     cursor.execute("insert into peliculas values (4, 'La dama y el vagabundo',1955)")
     print("\tinsert into peliculas values (4, 'La dama y el vagabundo',1955)")
     
     cursor.execute("insert into peliculas values (5,'101 dalmatas',1961)")
     print("\tinsert into peliculas values (5,'101 dalmatas',1961)")
     
     cursor.execute("insert into peliculas values (6, 'Mary Poppins',1964)")
     print ("\tinsert into peliculas values (6, 'Mary Poppins',1964)")
     
     cursor.execute("insert into peliculas values (7, 'El libro de la selva',1967)")
     print("\tinsert into peliculas values (7, 'El libro de la selva',1967)")
     
     cursor.execute("insert into peliculas values (8, 'Los tres mosqueteros',1993)")
     print("\tinsert into peliculas values (8, 'Los tres mosqueteros',1993)")
     
     cursor.execute("insert into peliculas values (9, 'El rey leon',1994)")
     print("\tinsert into peliculas values (9, 'El rey leon',1994)")
     
     cursor.execute("insert into peliculas values (10, 'Toy Story',1995)")
     print("\tinsert into peliculas values (10, 'Toy Story',1995)")
     
     print("INSERT OK")
  except Exception as err:
     print("No se ha podido insertar datos en la tabla peliculas")
  
  # 5- Haremos un select para ver que se han añadido bien las 10 peliculas  
  try:
     time.sleep(10)
     print ("SELECT: select * from peliculas order by id")
     cursor.execute("select * from peliculas order by id")
     print("SELECT OK")
     print ("Los elementos añadidos son: ", cursor.fetchall())
  except Exception as err:
     print("No se ha podido realizar la select")
     

if __name__ == "__main__":
    connectCrate()
