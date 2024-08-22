import mysql.connector

def hae(tunnus):
    sql = f"SELECT type FROM airport where iso_country='{tunnus}'"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    types = {}
    if cursor.rowcount >0 :
        for row in res:
            if row[0] not in types:
                types[row[0]] = 1
            else:
                types[row[0]] = types[row[0]]+1
    for type in types:
        print(f"{type}: {types[type]}")
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

tunnus = input("Syötä maatunnus: ")
hae(tunnus)