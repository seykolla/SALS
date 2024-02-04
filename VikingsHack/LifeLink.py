import googlemaps
import responses
import random
import sys 

class LifeLink:
    def __init__(self, distance, service):
        assert service == "urgent care" or service =="vet"
        assert type(distance)== float or type(distance) == int

        self.client = googlemaps.Client(key= 'AIzaSyDZP67HsK_6GmGq3WaL4IIZOeHIbHgg-hk')
        self.location = self.client.geolocate()['location']
        self.distance = distance * 1.60934 *1000

        if(service == 'vet'):
            self.service = 'veterinary services'
        else:
            self.service = service

    def get_current_location(self):
        return self.location
    
    def get_distance(self):
        return self.distance

    def get_service(self):
        return self.service
    
    
    def get_nearby_places(self):
        nearby_places = self.client.places_nearby(keyword= self.service, location =self.location, radius = self.distance)
        if(nearby_places['results'] is None):
            return None #none found
        else:
            results = []
            for i in nearby_places['results']:
                wait_time = random.randint(1, 180)
                destination = i['geometry']['location']
                distance = self.client.distance_matrix(origins = self.location, destinations = destination)['rows'][0]['elements'][0]['distance']['text']
                print(f"name: {i['name']},address: {i['vicinity']}, 'distance': {distance}, 'wait_time: {wait_time}, open: {i['opening_hours']['open_now']} ")
                print()
                results.append({'name':i['name'], 'address': i['vicinity'], 'distance': {distance}, 'wait_time': wait_time, 'open': i['opening_hours']['open_now']})
            return results







vals =sys.argv[1:]

instance = LifeLink(float(vals[0]), vals[1])
instance.get_nearby_places()

