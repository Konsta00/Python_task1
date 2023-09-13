import mysql.connector

try:
  connection = mysql.connector.connect(
      host="127.0.0.1",
      port=3306,
      user="root",
      password="root",
      database="flight_game",
      autocommit=True
  )

  icao_input = input('Hae lentokenttää ICAO-koodilla: ')

  if connection.is_connected():
      print("Connected to the database")
  cursor = connection.cursor()


  cursor.execute(f"SELECT * FROM airport WHERE ident = '{icao_input}';")
  results = cursor.fetchall()

  # Print the results
  print(f"Haettu lentokenttä: \n {results}")

  # for row in results:
  #     print(row)
  # cursor.close()

  connection.close()
  print("Connection closed")
except mysql.connector.Error as e:
  print("Error:", e)