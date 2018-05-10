
import urllib.request, json, numpy, math
#
# read In the data from the URL
#
data = urllib.request.urlopen("https://opensky-network.org/api/states/all").read()
#
# decode byte object into json
#
data = data.decode()
#
# convet json into python-like from string and pull out states data
#0	icao24	string	Unique ICAO 24-bit address of the transponder in hex string representation.
#1	callsign	string	Callsign of the vehicle (8 chars). Can be null if no callsign has been received.
#2	origin_country	string	Country name inferred from the ICAO 24-bit address.
#3	time_position	int	Unix timestamp (seconds) for the last position update. Can be null if no position report was received by OpenSky within the past 15s.
#4	last_contact	int	Unix timestamp (seconds) for the last update in general. This field is updated for any new, valid message received from the transponder.
#5	longitude	float	WGS-84 longitude in decimal degrees. Can be null.
#6	latitude	float	WGS-84 latitude in decimal degrees. Can be null.
#7	geo_altitude	float	Geometric altitude in meters. Can be null.
#8	on_ground	boolean	Boolean value which indicates if the position was retrieved from a surface position report.
#9	velocity	float	Velocity over ground in m/s. Can be null.
#10	heading	float	Heading in decimal degrees clockwise from north (i.e. north=0°). Can be null.
#11	vertical_rate	float	Vertical rate in m/s. A positive value indicates that the airplane is climbing, a negative value indicates that it descends. Can be null.
#12	sensors	int[]	IDs of the receivers which contributed to this state vector. Is null if no filtering for sensor was used in the request.
#13	baro_altitude	float	Barometric altitude in meters. Can be null.
#14	squawk	string	The transponder code aka Squawk. Can be null.
#15	spi	boolean	Whether flight status indicates special purpose indicator.
#16	position_source	int	Origin of this state’s position: 0 = ADS-B, 1 = ASTERIX, 2 = MLAT

data = json.loads(data)['states']

#
# get chosen long and lat
#

lat = float(input('input latitude: '))
long = float(input('input longitude: '))

#
# Calculate distance
#
def location( plane, long, lat):

	radiusOfEarth = 6371 #km

	delta_long = math.radians(long - plane[5])


	delta_lat = math.radians(lat - plane[6])
	#
	# Calculate cenrtal angle
	#
	delta_sigma = 2 * numpy.arcsin( numpy.sqrt( ( numpy.sin(delta_lat/2) )**2 + numpy.cos(lat)*numpy.cos(plane[6])*(numpy.sin(delta_long/2))**2))
	#
	# Calculate geodesic distance
	#
	#print(float(radiusOfEarth * delta_sigma))
	return radiusOfEarth * delta_sigma

#
# Find closest plane
#
def closest_func(long, lat):
	closest = float(0.0)
	closestplane = int(0)
	distance = int(0)
	for plane in data:
		#
		# If data from plane isn't fully gather the long/lat/alt is replesented as none. discard data
		#
		if plane[5] == None or plane[6] == None or plane[7] == None:
			continue
		else:
			distance = location(plane, long, lat)

		if closest== 0:
			closest = distance
			closestplane = plane
		if distance < closest :
			closest = distance
			closestplane = plane
			#print(closestplane)

	print( 'Geodesic distance: ' + str(closest) + 'km')
	print( 'Callsign: ' + str(closestplane[1]))
	print( 'Lattitude and Longitude: ' + str(closestplane[5]) + ', ' + str(closestplane[6]))
	print( 'Geometric Altitude: ' + str(closestplane[7]))
	print( 'Country of origin: ' + str(closestplane[2]))
	print( 'ICAO24 ID: ' + str(closestplane[0]))


closest_func(long,lat)
