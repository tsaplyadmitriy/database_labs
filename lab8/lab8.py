from faker import Faker
import psycopg2 as db
import geopy as gp




connection = db.connect(database='dvd_rental_3', user='postgres',password='lnn1337213',host='127.0.0.1',port='5432')
print("Connection established!")

cursor = connection.cursor()


cursor.callproc('generate_longtitude', ())
lat = []
lon = []

table = cursor.fetchall()
print(table)
geolocator = gp.Nominatim(user_agent="user")

cursor.execute("UPDATE address SET lat = " + str(-13.0712346) +
               ",lon=" + str(-55.91418188770646) + " WHERE address.city_id = " + str(
        449) + "RETURNING address.lon,address.lat;")
print("UPDATE address SET lat = " + str(-13.0712346) +
               ",lon=" + str(-55.91418188770646) + " WHERE address.city_id = " + str(
        449) + " RETURNING address.lon,address.lat;")

for row in table:
        if(row is not None):
                print(row)
                location = geolocator.geocode(row[0], timeout=None)

                if( location is not None and row is not None):

                          print(location.raw['lat'])
                          print(location.raw['lon'])
                          print(row[2])
                          cursor.execute("UPDATE address SET lat = " + str(location.raw['lat']) +
                               ",lon="+ str(location.raw['lon']) + " WHERE address.city_id = "+str(row[2])+" RETURNING address.lon,address.lat;")
        else:
                cursor.execute("UPDATE address SET lat = " + str(0.0) +
                               ",lon=" + str(0.0) + " WHERE address.city_id = " + str(
                        row[2]) + " RETURNING address.lon,address.lat;")



connection.commit()



cursor.close()
connection.close()
