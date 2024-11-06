from urllib.request import urlopen
import json
import winrt.windows.devices.geolocation as wdg


async def get_current_location():
    locator = wdg.Geolocator()
    pos = await locator.get_geoposition_async()
    return pos.coordinate

# Tes tes tes tes
async def report():
    coordinate = await get_current_location()
    print(coordinate.latitude, coordinate.longitude)
    
    response = urlopen(f"https://nominatim.openstreetmap.org/reverse?lat={coordinate.latitude}&lon={coordinate.longitude}&format=json")
    result = json.loads(response.read())

    display_name = result["display_name"]
    road = "Tidak ada nama jalan" if result["name"] == "" else result["name"]
    print(f"Nama jalan: {road}")
    print(f"Nama seluruhnya: {display_name}")