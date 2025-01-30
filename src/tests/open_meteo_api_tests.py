import requests
import pytest

# Open-Meteo API base URL
BASE_URL = "https://api.open-meteo.com/v1/forecast"

# Test locations (latitude, longitude)
TEST_LOCATIONS = [
    (51.5074, -0.1278, "London"),
    (40.7128, -74.0060, "New York"),
    (32.0853, 34.7818, "Tel Aviv"),
    (35.6895, 139.6917, "Tokyo"),
]

@pytest.mark.parametrize("lat, lon, city", TEST_LOCATIONS)
def test_get_weather_forecast(lat, lon, city):
    """Test fetching weather forecast for different locations."""
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": "true"
    }
    response = requests.get(BASE_URL, params=params)

    # Validate response status
    assert response.status_code == 200, f"Failed for city: {city}"

    # Validate JSON response structure
    data = response.json()
    assert "current_weather" in data, f"Missing 'current_weather' in response for {city}"
    assert "temperature" in data["current_weather"], f"Missing 'temperature' key in response for {city}"
    assert "windspeed" in data["current_weather"], f"Missing 'windspeed' key in response for {city}"

def test_invalid_coordinates():
    """Test API response with invalid latitude and longitude."""
    params = {
        "latitude": 999,  # Invalid latitude
        "longitude": 999,  # Invalid longitude
        "current_weather": "true"
    }
    response = requests.get(BASE_URL, params=params)

    # Validate response (Open-Meteo returns 400 for invalid coordinates)
    assert response.status_code == 400, "API should return 400 for invalid coordinates"

def test_response_time():
    """Test that API responds within 2 seconds."""
    params = {
        "latitude": 51.5074,
        "longitude": -0.1278,
        "current_weather": "true"
    }
    response = requests.get(BASE_URL, params=params)

    # Validate response time
    assert response.elapsed.total_seconds() < 2, "Response took too long!"

def test_temperature_range():
    """Test that temperature is within a reasonable range (-100 to 100°C)."""
    params = {
        "latitude": 51.5074,
        "longitude": -0.1278,
        "current_weather": "true"
    }
    response = requests.get(BASE_URL, params=params)

    # Validate response
    assert response.status_code == 200
    data = response.json()

    temp = data["current_weather"]["temperature"]
    assert -100 <= temp <= 100, f"Temperature {temp}°C is out of expected range"

