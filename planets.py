from skyfield.api import load
from datetime import datetime
import pytz

def get_tropical_longitude(date_str, time_str="12:00", planet="sun"):
    jst = pytz.timezone("Asia/Tokyo")
    dt_naive = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
    dt_utc = jst.localize(dt_naive).astimezone(pytz.utc)

    ts = load.timescale()
    t = ts.utc(dt_utc.year, dt_utc.month, dt_utc.day, dt_utc.hour, dt_utc.minute)

    eph = load('de421.bsp')
    earth = eph['earth']

    # 正しく「地球から見た天体」を計算
    planets = {
        "sun": eph["sun"],
        "moon": eph["moon"],
        "mercury": eph["mercury"],
        "venus": eph["venus"],
        "mars": eph["mars"],
        "jupiter": eph["jupiter barycenter"],
        "saturn": eph["saturn barycenter"],
        "uranus": eph["uranus barycenter"],
        "neptune": eph["neptune barycenter"],
        "pluto": eph["pluto barycenter"],
    }

    obj = planets.get(planet.lower())
    if obj is None:
        raise ValueError(f"Planet '{planet}' is not supported.")

    # 💡💡💡 これが正解！earth → obj の順！
    astrometric = earth.at(t).observe(obj).apparent()
    ecl_lon, ecl_lat, distance = astrometric.ecliptic_latlon(epoch=t)

    return ecl_lon.degrees % 360
