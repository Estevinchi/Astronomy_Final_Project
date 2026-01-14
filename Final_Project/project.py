from location import get_coordenates
from planets import planets_visible
from moon import moon_phase

from datetime import datetime
import geonamescache

def main():

    city = input("Where are you from? ")
    print("----")
    print(f"validating city ({city})...")
    validate_city(city)
    print("Ok")
    print("Select the date you want to consult")
    date = input("(YYYY/MM/DD HH:MM): ")
    print("----")
    print(f"validating date ({date})...")
    validate_date(date)
    print("Ok----")

    print("Getting coordenates----")
    lat, lon = get_coordenates(city)
    
    print("Listing planets...")
    planets = planets_visible(lat,lon,date)
    
    print("-----")
    
    day,hour = date.split()
    
    print(f"List of the planets you can see from {city} on {day} at {hour}h:")
    for planet in planets:
        print(f"- {planet}")

    print(f"Moon phase in {city} on {day}:")
    moon_phase(date)
        



def validate_city(cityName):
    cityName = cityName.strip()
    gc = geonamescache.GeonamesCache()
    cities = gc.get_cities()
    
    for city_id in cities:
        if cities[city_id]['name'].lower() == cityName.lower().strip():
            return True
        
    raise ValueError("There's no city with that name.")


def validate_date(date):
    try:
        dt = datetime.strptime(date,"%Y/%m/%d %H:%M")
        return True
    except Exception:
        raise ValueError("Please, put a real date with this format: YYYY/MM/DD HH:MM")



if __name__=='__main__':
    main()