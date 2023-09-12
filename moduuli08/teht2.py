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
# KYSY KÄYTTÄJÄLTÄ MAA-KOODIA
  maa_input = input('Hae lentokenttien määrät MAA-tunnisteella (esim. FI tai US): ')

  if connection.is_connected():
      print("Connected to the database")
  cursor = connection.cursor()

# SQL QUERY TO GET SUM OF AIRPORTS 
  sql = 'SELECT type, count(*) FROM airport WHERE iso_country = %s AND type = %s GROUP BY type'

  def execute_sql(type):
    cursor.execute(sql, (maa_input, type))
    return cursor.fetchall()

  small_airport_sum = execute_sql('small_airport')
  medium_airport_sum = execute_sql('medium_airport')
  closed_sum = execute_sql('closed')
  heliport_sum = execute_sql('heliport')
  balloonport_sum = execute_sql('balloonport')
  seaplane_sum = execute_sql('seaplane_base')

  # Print the results

  def return_sum(airport_sum):
    for row in airport_sum:
        return row[1]

  print(return_sum(small_airport_sum), 'pientä lentokenttää')
  print(return_sum(medium_airport_sum), 'keskikokoista lentokenttää')
  print(return_sum(closed_sum), 'suljettua lentokenttää')
  print(return_sum(heliport_sum), 'helikopterikenttää')
  print(return_sum(balloonport_sum), ' ilmapallokenttää')
  print(return_sum(seaplane_sum), ' merilentokenttää')
  
  cursor.close()
  connection.close()
  print("Connection closed")
except mysql.connector.Error as e:
  print("Error:", e)