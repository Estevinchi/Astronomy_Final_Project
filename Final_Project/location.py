from geopy.geocoders import Nominatim

def get_coordenates(CityName):

    geolocator = Nominatim(user_agent="Final_Project")
    print("...")
    location = geolocator.geocode(CityName,exactly_one=True, addressdetails=True, timeout=10)

    if not location:
        raise ValueError("Error, city not found")
    
    coordenates = str(location.latitude), str(location.longitude)
    return coordenates
    

if __name__ == '__main__':
    get_coordenates("Hanoi")
    # '40.416782', '-3.703507'
    # '38.7077507', '-9.1365919'
    # '40.7127281', '-74.0060152'
    # '21.0283334', '105.854041'