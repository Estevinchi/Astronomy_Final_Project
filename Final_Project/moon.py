import ephem

def moon_phase(date):
    date, hour = date.split()
    moon = ephem.Moon(date)
    
    return moon_illumination_phase_name(moon.phase)

def moon_illumination_phase_name(illumination):
    if illumination < 1:
        return "New Moon"
    elif illumination < 48:
        return "Waxing Crescent | Waning Crescent"
    elif illumination < 52:
        
        return "Half Moon"
    elif illumination < 98:
        return "Waxing Gibbous | Waning Gibbous"
    else:
        return "Full Moon"