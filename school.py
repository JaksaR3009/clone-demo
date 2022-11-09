import sqlite3

# primjer skole

connection = sqlite3.connect("school.db")
# create database school

# kursor za izvrsavanje upita nad bazom
c = connection.cursor()

# # nakon sto je query izvrsen isti zakomentarisan jer se ne moze opet isti pokrenuti
# c.execute('''CREATE TABLE ucenici (ime, prezime, jmbg, datum_rodjenja, razred)''')

# c.execute('''INSERT INTO ucenici values("marko", "markovic", 1001010100101, "2013-11-11", 4)''')
# c.execute('''INSERT INTO ucenici values("petar", "petrovic", 1010013100101, "2013-10-10", 4)''')
# c.execute('''INSERT INTO ucenici values("milos", "milosevic", 0909010100101, "2013-09-09", 4)''')
# c.execute('''INSERT INTO ucenici values("jaksa", "riger", 3009010100101, "2010-09-30", 7)''')
# c.execute('''INSERT INTO ucenici values("mirjana", "riger", 2501009100101, "2009-01-25", 8)''')

# da bi se izvrsio upis u bazu mora se odraditi commit
# connection.commit()

# ucenici = c.execute('''SELECT * FROM ucenici''')

# ucenici = c.execute('''SELECT * FROM ucenici WHERE prezime="markovic"''')

ucenici = c.execute('''SELECT ime, prezime FROM ucenici''')

# samo poziv ka ucenicima vraca objekat SQLite klase, stoga fetchall() metod koji vraca niz tuple-a
print(ucenici.fetchall())