import sqlite3

cars = []
for x in range(1,10):
	cars.append((bool(1),))

connexion = sqlite3.connect('db.sqlite3')
cursor = connexion.cursor()
cursor.executemany("""
INSERT INTO car_car(disponibility) VALUES(?)""", cars)
connexion.commit()
connexion.close()