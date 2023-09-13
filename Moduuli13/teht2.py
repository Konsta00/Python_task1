import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)

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

def sql_airport(icao):
    cursor = connection.cursor()
    cursor.execute(f"SELECT name, ident, municipality FROM airport WHERE ident = '{icao}';")
    results = cursor.fetchall()
    connection.close()

    # return results from query
    return results

@app.route('/airport/<icao>', methods=['GET'])
def check_airport(icao):
    data = sql_airport(icao)
    print(data)
    # Assing correct values and names for airport
    res_data = {
        'Name': data[0][0],
        'ICAO': data[0][1],
        'Municipality': data[0][2]
    }
    # Return the data in json format
    return jsonify(res_data)

if __name__ == '__main__':
    app.run(debug=True)


