import requests
import re

def get_coordinates(sector):
    # ✅ Define query
    query = f"sector {sector} gurgaon latitude longitude"
    
    # ✅ Define headers
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9"
    }

    response = requests.get(
        "https://www.google.com/search",
        params={"q": query},
        headers=headers
    )

    html = response.text

    # ✅ Better regex
    match = re.search(r'(\d+\.\d+).*?N.*?(\d+\.\d+).*?E', html)

    if match:
        return float(match.group(1)), float(match.group(2))

    return None, None


# 🔥 Test
lat, lon = get_coordinates(10)
print(lat, lon)