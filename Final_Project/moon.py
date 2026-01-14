import ephem

def moon_phase(date):
    date, hour = date.split()
    
    moon = ephem.Moon(date)
    
    return moon_illumination_phase_name(moon.phase)
    
def moon_illumination_phase_name(illumination):
    
      
    if illumination < 1:
        print(f"New Moon (illumination: {int(illumination)}%")
    elif illumination < 48:
        print(f"Waxing Crescent | Waning Crescent (illumination: {int(illumination)}%)")
    elif illumination < 52:
        print(f"Half Moon (illumination: {int(illumination)}%")
    elif illumination < 98:
        print(f"Waxing Gibbous | Waning Gibbous (illumination: {int(illumination)}%")
    else:
        print(f"Full Moon (illumination: {int(illumination)}%")
    
    