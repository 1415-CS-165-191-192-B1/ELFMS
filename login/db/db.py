#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys


person = (
    ('dyosa', 3, 'aaaa'),
    ('mara', 1, 'bbbb'),
    ('rowel', 1, 'cccc'),
    ('denise', 2, 'dddd'),
    ('tricia', 3, 'eeee'),
    ('ryan', 1, 'ffff'),
    ('meya', 2, 'gggg'),
    ('maria', 3, 'hhhh')
)

con = None

try:
     
    con = psycopg2.connect(database='testdb', user='dyosa', password = 'dyosa', host='127.0.0.1', port=5432) 
  
    cur = con.cursor()  
    
    cur.execute("DROP TABLE IF EXISTS person")
    cur.execute("CREATE TABLE person(Name TEXT, Price INT, Password VARCHAR )")
    query = "INSERT INTO person (Name, Price, Password) VALUES (%s, %s, %s)"
    cur.executemany(query, person)
        
    con.commit()
    

except psycopg2.DatabaseError, e:
    
    if con:
        con.rollback()
    
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()
