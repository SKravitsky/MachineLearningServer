import mysql.connector
import sys

config = {
  'user': 'ECE32',
  'password': 'seniordesign',
  'host': 'septa-instance.ctejk6luw06s.us-west-2.rds.amazonaws.com',
  'database': 'septa',
  'raise_on_warnings': True,
}

def get_lineID(name):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor(dictionary=True)
    sql = "SELECT id FROM septa.lines WHERE name = '" + name + "' LIMIT 1"
    cursor.execute(sql)

    line_id = ""

    for row in cursor:
        line_id = row['id']

    cursor.close()
    cnx.close()

    return line_id


def get_alllines():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor(dictionary=True)

    cursor.execute("SELECT * FROM septa.lines")

    lines = {}
    for row in cursor:
        line_id = row['id']
        lines[row['name']] = line_id

    cursor.close()
    cnx.close()

    return lines


def add_station(station):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    add_thing = ("INSERT INTO septa.stations"
                 "(name, address, latitude, longitude, line_id) "
                 "VALUES (%s, %s, %s, %s, %s)")

    data_thing = (station.name, station.address, station.latitude, station.longitude, station.line_id)

    try:
        cursor.execute(add_thing, data_thing)
        cnx.commit()
    except mysql.connector.Error as err:
        print err

    cursor.close()
    cnx.close()


def add_stations(stations):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    add_thing = ("INSERT INTO septa.stations"
                 "(name, address, latitude, longitude, line_id) "
                 "VALUES (%s, %s, %s, %s, %s)")


    try:
        cursor.executemany(add_thing, stations)
        cnx.commit()
        sys.stdout.write("Added to Database")
        sys.stdout.flush()
    except mysql.connector.Error as err:
        print err

    cursor.close()
    cnx.close()


def reset_stations():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    try:
        cursor.execute("TRUNCATE stations")
        cnx.commit()
    except mysql.connector.Error as err:
        print(err)

    cursor.close()
    cnx.close()


def get_all_stations():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor(dictionary=True)

    cursor.execute("SELECT * FROM stations")

    stations = []
    for row in cursor:
        station = row['id_station']
        name = row['name_long']
        address = row['address']
        latitude = row['latitude']
        longitude = row['longitude']
        stations.append(row)

    cursor.close()
    cnx.close()

    return stations

def get_stationID(name):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor(dictionary=True)
    sql = "SELECT name_long, id_station FROM septa.stations WHERE name_long LIKE '%" + name + "%'"

    cursor.execute(sql)
    data = None

    for row in cursor:
        data = row["id_station"]

    cursor.close()
    cnx.close()

    return data

def add_Stop(stops):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    add_thing = ("INSERT INTO septa.stops"
                 "(id_septa_stop, id_station, id_line, id_direction) "
                 "VALUES (%s, %s, %s, %s)")

    try:
        cursor.executemany(add_thing, stops)
        cnx.commit()
        sys.stdout.write("Added to Database")
        sys.stdout.flush()
    except mysql.connector.Error as err:
        print err

    cursor.close()
    cnx.close()

    return


def add_Schedules(schedules):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    add_thing = ("INSERT INTO septa.schedules"
                 "(id_day, id_line, id_train, id_station, num_stop, id_stop, time_departure, id_direction) "
                 "VALUES (%s, %s, %s, %s, %s, %s, STR_TO_DATE(%s, '%h:%i%p' ), %s)")

    try:
        cursor.executemany(add_thing, schedules)
        cnx.commit()
        print ("Added to Database")
    except mysql.connector.Error as err:
        print err

    cursor.close()
    cnx.close()

    return