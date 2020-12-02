from openSky import OpenSkyApi
import pyodbc
import schedule
import time

api = OpenSkyApi()
s = api.get_states()
#print(s)
icao24 = []
callsign = []
origin_country = []
time_position = []
last_contact = []
longitude = []
latitude = []
geo_altitude = []
on_ground = []
velocity = []
heading = []
vertical_rate = []
sensors = []
baro_altitude = []
squawk = []
spi = []
position_source = []

for i in s.states:
    latitude.append(i.latitude)
    icao24.append(i.icao24)
    callsign.append(i.callsign)
    origin_country.append(i.origin_country)
    time_position.append(i.time_position)
    last_contact.append(i.last_contact)
    longitude.append(i.longitude)
    geo_altitude.append(i.geo_altitude)
    on_ground.append(i.on_ground)
    velocity.append(i.velocity)
    heading.append(i.heading)
    vertical_rate.append(i.vertical_rate)
    sensors.append(i.sensors)
    baro_altitude.append(i.baro_altitude)
    squawk.append(i.squawk)
    spi.append(i.spi)
    position_source.append(i.position_source)

x = len(baro_altitude)
y = len(spi)
z = len(sensors)
print(x,y,z)
  
server = 'localhost'
database = 'FYP'
cnxn = pyodbc.connect(
Trusted_Connection='Yes',
Driver ='{ODBC Driver 17 for SQL Server}',
Server = server,
Database = database)
cursor = cnxn.cursor()


for i in range(len(baro_altitude)):
    print ('Inserting a new row into table')
    tsql = "INSERT INTO opensky (icao24, callsign, origin_country,time_position,last_contact,longitude,latitude,geo_altitude,on_ground,velocity,heading,vertical_rate,sensors,baro_altitude,squawk,spi,position_source)VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"
    with cursor.execute(tsql,icao24[i],callsign[i],origin_country[i],time_position[i],last_contact[i],longitude[i]
    ,latitude[i],geo_altitude[i],on_ground[i],velocity[i],heading[i],vertical_rate[i],sensors[i],baro_altitude[i],
    squawk[i],spi[i],position_source[i]):
      print ('Successfully Inserted!')
        #change
    















