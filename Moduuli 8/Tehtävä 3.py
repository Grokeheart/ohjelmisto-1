import mysql.connector
from geopy import distance

def hae(icao):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport where id='{icao}'"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    if cursor.rowcount >0 :
        for row in res:
            return row[0], row[1]
    return

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='username',
         password='password',
         autocommit=True,
         charset='utf8mb4',
         collation='utf8mb4_general_ci'
         )

data = []

for i in range(2):
    icao = input("Syötä ICAO: ")
    data.append(hae(icao))

print(f"Etäisyys: {distance.distance(data[0], data[1]).kilometers} kilometriä")