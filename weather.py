import urllib.request
import json

def get_weather(lat, lon):
    """Fetches and prints the current temperature for given coordinates."""
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    
    try:
        # Call the free Open-Meteo API
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            temp = data['current_weather']['temperature']
            print(f"🌡️ Current temperature is {temp}°C")
    except urllib.error.URLError as e:
        print(f"Network error: Please check your internet connection. ({e})")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("Fetching the weather for Lucknow...")
    # Coordinates for Lucknow, UP
    get_weather(26.8467, 80.9462)