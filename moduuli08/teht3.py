import mysql.connector
from geopy.distance import geodesic

try:
  connection = mysql.connector.connect(
      host="127.0.0.1",
      port=3306,
      user="root",
      password="root",
      database="flight_game",
      autocommit=True
  )
  if connection.is_connected():
    print("Connected to the database")
    cursor = connection.cursor()

    sql = 'SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s ;'

    print('Ohjelma laskee kahden lentokentän välisen etäisyyden. Syötä ohjelmalle kaksi ICAO-koodia. \n')

    icao_koodi = input('Anna ensimmäinen ICAO-koodi: ')
    cursor.execute(sql, (icao_koodi,))
    lat, long = result = cursor.fetchone()
    airport1_coords = (lat, long)
    # print(f'Airport coordinates: {airport1_coords}')

    icao_koodi = input('Anna toinen ICAO-koodi: ')
    cursor.execute(sql, (icao_koodi,))
    lat, long = result = cursor.fetchone()
    airport2_coords = (lat, long)
    # print(f'Airport coordinates: {airport2_coords}')

    distance = geodesic(airport1_coords, airport2_coords).kilometers

    print(f'Lentokenttien välinen etäisyys {distance} kilometriä')
  
    cursor.close()
    connection.close()
    print("Connection closed")

except mysql.connector.Error as e:
  print("Error:", e)




