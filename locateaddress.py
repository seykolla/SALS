import googlemaps
import responses

def address_finder():
    responses.add(
                responses.POST,
                "https://www.googleapis.com/geolocation/v1/geolocate",
                body='{"location": {"lat": 51.0,"lng": -0.1},"accuracy": 1200.4}',
                status=200,
                content_type="application/json",
            )

    client = googlemaps.Client(key='AIzaSyDZP67HsK_6GmGq3WaL4IIZOeHIbHgg-hk')

    location = client.geolocate()['location']
    map_data = client.reverse_geocode(location)
    return map_data[0]['formatted_address']
