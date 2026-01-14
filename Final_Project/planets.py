import ephem

def planets_visible(lat,lon, datetime):
    visible_planets_list = []

    observer = ephem.Observer()

    observer.lat = lat
    observer.lon = lon
    observer.date = datetime
    
    planets = {
        "Mercury":ephem.Mercury(),
        "Venus":ephem.Venus(),
        "Mars":ephem.Mars(),
        "Jupiter":ephem.Jupiter(),
        "Saturn":ephem.Saturn(),
        "Uranus":ephem.Uranus(),
        "Neptune":ephem.Neptune()
    }
    for planet_name in planets:
        info_planet = planets[planet_name]
        info_planet.compute(observer)

        if info_planet.alt > 0:
            visible_planets_list.append(planet_name)

    return visible_planets_list

# print(planets_visible("41.3825802","2.177073","2026/01/13 20:22:00"))