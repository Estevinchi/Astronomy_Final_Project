from location import get_coordenates
from planets import planets_visible

import geonamescache

def main():

    city = input("Where are you from? ")
    print("---------")
    validate_city(city)
    print("Select the date you want to consult")
    date = input("(YYYY/MM/DD HH:MM): ")

    lat, lon = get_coordenates(city)

    planets = planets_visible(lat,lon,date)

    print(planets)



def validate_city(cityName):
    cityName = cityName.strip()
    gc = geonamescache.GeonamesCache()
    cities = gc.get_cities()
    
    for city_id in cities:
        if cities[city_id]['name'].lower() == cityName.lower().strip():
            return True
    raise ValueError("There's no city with that name.")


def validate_date(date):
    day, hour = date.split()
    year,month,day = day.split("/")
    print("day:",day,"Hour:",hour)



if __name__=='__main__':
    # main()
    validate_date("22/1/2 20:30")