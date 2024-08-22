import mysql.connector

def hae(icao):
    sql = f"SELECT name, municipality FROM airport where id='{icao}'"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    if cursor.rowcount >0 :
        for row in res:
            print(f"Nimi: {row[0]} Paikkakunta: {row[1]}")
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

icao = input("Syötä ICAO: ")
hae(icao)