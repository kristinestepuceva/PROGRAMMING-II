import sqlite3

conn=sqlite3.connect('ofice.db')
cur=conn.cursor()

cur.execute('''
CREATE TABLE if NOT EXISTS darbinieks (
    id_darbinieks TEXT PRIMARY KEY,
    vards TEXT,
    uzvards TEXT,
    alga REAL,
    atvalinajums TEXT,
    id_organizacij INTEGER,
    
  
    FOREIGN KEY (id_organizacij) REFERENCES organizacija (id_organizacija)
)
''')

cur.execute('''
CREATE TABLE if NOT EXISTS organizacija (
    id_organizacija Integer PRIMARY KEY autoincrement,
    nosaukums TEXT)
''') 


cur.execute('''INSERT OR IGNORE INTO darbinieks (id_darbinieks, vards, uzvards, atvalinajums) VALUES
     ('121278-11234', 'Janis', 'Berzins', 'N'),
     ('110367-11234', 'Anna', 'Ozola', 'N'),
     ('090997-11234', 'Pēteris', 'Kalniņš', 'Y')
 ''')
cur.execute('''INSERT OR IGNORE INTO organizacija (id_organizacija, nosaukums) VALUES
     ('1', 'apkalpošana'),
     ('2', 'vadišana'),
     ('3', 'gramatvēdiba')
 ''')

#cur.execute('''UPDATE darbinieks SET alga = '850' where id_darbinieks = '110367-11234' or  id_darbinieks = '121278-11234' ''')
#cur.execute('''UPDATE darbinieks SET id_organizacij = '3' where id_darbinieks = '090997-11234' ''')
#cur.execute('''UPDATE darbinieks SET alga = '3000' where id_darbinieks = '090997-11234' ''')

cur.execute("""SELECT darbinieks.vards, darbinieks.alga, organizacija.nosaukums 
            from darbinieks, organizacija
            WHERE darbinieks.id_organizacij = organizacija.id_organizacija
            """)
for row in cur.fetchall():
    print("DARBINIEKS----ALGA----DARBA VEIDS")
    print(row)


#cur.execute('''SELECT * FROM darbinieks WHERE atvalinajums = 'Y' ''')
#rows = cur.fetchall()
#for row in rows:
#    print(row)
conn.commit()
conn.close()