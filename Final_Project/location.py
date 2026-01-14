from geopy.geocoders import Nominatim

def get_coordenates(CityName):

    geolocator = Nominatim(user_agent="Final_Project")


    location = geolocator.geocode(CityName,exactly_one=True, addressdetails=True, timeout=10)

    if not location:
        raise ValueError("Error, city not found")
    
    coordenates = str(location.latitude), str(location.longitude)
    return coordenates
    

if __name__ == '__main__':
    print(get_coordenates("Madrid"))