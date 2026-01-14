from location import get_coordenates
from planets import planets_visible
from moon import moon_phase


from timezonefinder import TimezoneFinder
import pytz
from datetime import datetime, timedelta
import geonamescache


def main():

    city = input("Where are you from? ").title()

    print("-----")
    print(f"Validating city ({city})...")

    validate_city(city)

    print("-----")
    print("Getting coordenates")
    lat, lon = get_coordenates(city)

    print("-----")
    today = (
        input("Do you want to consult today at midnight (00:00)? Y/N: ").upper().strip()
    )

    match today:
        case "Y":
            date = datetime.now()
            date = date.strftime("%Y/%m/%d")
            date = date + " " + "00:00"
        case _:
            print("-----")
            print("You choosed to write the date.")
            print("Please, follow this pattern YYYY/MM/DD HH:MM")
            date = input("Input date: ")
            new_date = set_time_zone(get_time_diff(lat=lat, lon=lon, date=date), date)

    print("-----")
    print("Validating dates")
    print(f"Local time: {date}")
    print("...")
    validate_date(date)
    print(f"UTC+0: {new_date}")
    print("...")
    validate_date(new_date)

    day, hour = str(new_date).split()

    print("-----")
    planets = planets_visible(lat, lon, new_date)
    print(f"List of the planets you can see from {city} on {day} at {hour}h:")
    for planet in planets:
        print(f"- {planet}")

    print("-----")
    print(f"Moon phase in {city} on {day}: {moon_phase(new_date)}")


def validate_city(cityName):
    cityName = cityName.strip()
    gc = geonamescache.GeonamesCache()
    cities = gc.get_cities()

    for city_id in cities:
        if cities[city_id]["name"].lower() == cityName.lower().strip():
            return True

    raise ValueError("There's no city with that name.")


def validate_date(date):
    try:
        datetime.strptime(date, "%Y/%m/%d %H:%M")
        return True
    except Exception:
        raise ValueError("Please, put a real date with this format: YYYY/MM/DD HH:MM")


def get_time_diff(lat, lon, date):
    print("-----")
    print("Getting your time zone...")
    tz_name = TimezoneFinder().timezone_at(lat=lat, lng=lon)
    print(tz_name)
    date = datetime.strptime(date, "%Y/%m/%d %H:%M")

    if not tz_name:
        return "There has been a problem trying to get your time location."

    tz = pytz.timezone(tz_name).localize(date).utcoffset().total_seconds()
    tz = int((tz / 60) / 60) + 0
    print(f"Time zone difference: {tz}")
    return tz


def set_time_zone(timeDif, date):

    date = datetime.strptime(date, "%Y/%m/%d %H:%M")

    diff = timedelta(hours=timeDif)

    utc_td = date - diff

    return utc_td.strftime("%Y/%m/%d %H:%M")


if __name__ == "__main__":
    main()
