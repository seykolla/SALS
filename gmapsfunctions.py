import googlemaps
gmaps = googlemaps.Client(key='AIzaSyDZP67HsK_6GmGq3WaL4IIZOeHIbHgg-hk')
map_data = gmaps.geocode("700 Newport Circle, Redwood City, CA 94065")
location = map_data[0]['geometry']['location']
latitude = location['lat']
longitude = location['lng']