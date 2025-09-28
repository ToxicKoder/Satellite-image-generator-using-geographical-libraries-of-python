from geopy.geocoders import Nominatim
import matplotlib.pyplot as plt
import contextily as ctx
from shapely.geometry import Point
import geopandas as gpd
from functools import lru_cache
import re

# cache geocoding results so repeated searches are instant
@lru_cache(maxsize=100)
def get_coordinates(place_name):
    geolocator = Nominatim(user_agent="osm_satellite_app")
    location = geolocator.geocode(place_name, exactly_one=True, addressdetails=True)
    if location:
        return location.latitude, location.longitude, location.address
    else:
        return None, None, None

def sanitize_filename(name):
    # Remove invalid filename characters
    return re.sub(r'[^a-zA-Z0-9_\-]', '_', name)

def generate_satellite_image(lat, lon, place_name, buffer=1000, zoom=16):
    point = gpd.GeoDataFrame(geometry=[Point(lon, lat)], crs="EPSG:4326")
    point = point.to_crs(epsg=3857)

    fig, ax = plt.subplots(figsize=(8, 8))  # bigger figure for clarity

    # tighter bounds = fewer tiles (faster)
    ax.set_xlim(point.geometry.x[0] - buffer, point.geometry.x[0] + buffer)
    ax.set_ylim(point.geometry.y[0] - buffer, point.geometry.y[0] + buffer)

    # add basemap
    ctx.add_basemap(ax, source=ctx.providers.Esri.WorldImagery, zoom=zoom)

    # lock aspect ratio (no stretching when maximizing window)
    ax.set_aspect("equal")

    plt.title(f"Satellite Image of {place_name}")
    
    # save safely
    filename = sanitize_filename(place_name) + "_satellite.png"
    plt.savefig(filename, dpi=200, bbox_inches="tight")
    plt.show()

    print(f"✅ Satellite image saved as '{filename}'")

# Main Loop 
if __name__ == "__main__":
    while True:
        place = input("\nEnter locality/area name: ").strip()
        lat, lon, address = get_coordinates(place)

        if lat is None or lon is None:
            print("❌ Place not found. Try a different locality.")
        else:
            print(f"📍 {address} -> Latitude={lat}, Longitude={lon}")
            generate_satellite_image(lat, lon, place, buffer=1500, zoom=16)

        choice = input("\nDo you want to continue? (yes/no): ").strip().lower()
        if choice not in ["yes", "y"]:
            print("👋 Exiting program. Goodbye!")
            break
