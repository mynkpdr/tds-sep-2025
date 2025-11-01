# 4. Scrape the BBC Weather API (0.5 Marks)

## 1. Problem Description

The task is to write a Python script that fetches a multi-day weather forecast for a specified city from the BBC Weather API. This involves a two-step process: first, finding the unique `locationId` for the city, and second, using that ID to retrieve the actual forecast data.

This project simulates a data integration task for "AgroTech Insights," a company that needs accurate weather data for agricultural planning.

## 2. Understanding the Requirements

- **Language**: Python.
- **Libraries**: `requests`.
- **API Endpoints**:
  1. **Locator Service**: `https://locator-service.api.bbci.co.uk/locations` (to find the `locationId`).
  2. **Weather Broker**: `https://weather-broker-cdn.api.bbci.co.uk/en/forecast/aggregated/{locationId}` (to get the forecast).
- **Logic**:
  1. Create a function to get the `locationId` for a given city name. This involves making a GET request to the locator service with the city as a search parameter.
  2. Create a second function that takes the `locationId` and makes a GET request to the weather broker API.
  3. Parse the JSON response from the weather broker.
  4. Extract the `localDate` and `enhancedWeatherDescription` for each day in the forecast.
- **Output**: A JSON object where keys are the dates and values are the corresponding weather descriptions.

## 3. Step-by-Step Solution

### Step 1: Set Up Your Environment

1. Create a project folder (e.g., `bbc_weather`).
2. Create and activate a virtual environment.
3. Install the `requests` library:

   ```bash
   pip install requests
   ```

4. Create a Python file for your code (e.g., `get_weather.py`).

### Step 2: Write the Python Script

1. **Get Location ID**: Write a function `get_location_id(city_name)` that constructs the URL for the locator service. The API requires a key, which appears to be public: `AGbFAKx58hyjQScCXIYrxuEwJh2W2cmv`. The function should parse the JSON response and return the `id` of the first search result.
2. **Get Weather Forecast**: Write a function `get_weather_forecast(location_id)` that constructs the URL for the weather broker. It should fetch the data and parse the JSON.
3. **Process Forecast**: Inside `get_weather_forecast`, iterate through the `forecasts` list in the response. For each item, extract `summary.report.localDate` and `summary.report.enhancedWeatherDescription`.
4. **Combine and Print**: In the main part of the script, call the first function to get the ID, pass it to the second function to get the forecast, and then print the final JSON output.

## 4. Code (`get_weather.py`)

```python
import requests
import json

# Publicly visible API key from BBC Weather network traffic
API_KEY = "AGbFAKx58hyjQScCXIYrxuEwJh2W2cmv"

def get_location_id(city_name: str) -> str:
    """
    Fetches the unique location ID for a given city from the BBC Locator Service.
    """
    url = "https://locator-service.api.bbci.co.uk/locations"
    params = {
        "api_key": API_KEY,
        "stack": "aws",
        "s": city_name,
        "a": "true",
        "format": "json"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    try:
        # The ID is in the first result of the response
        location_id = data['response']['results']['results'][0]['id']
        return location_id
    except (IndexError, KeyError):
        raise ValueError(f"Could not find a location ID for '{city_name}'.")


def get_weather_forecast(location_id: str) -> dict:
    """
    Fetches the aggregated weather forecast using a location ID.
    """
    url = f"https://weather-broker-cdn.api.bbci.co.uk/en/forecast/aggregated/{location_id}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    forecast_data = {}

    # Extract the date and description for each day in the forecast
    for forecast in data.get('forecasts', []):
        try:
            report = forecast['summary']['report']
            local_date = report['localDate']
            description = report['enhancedWeatherDescription']
            forecast_data[local_date] = description
        except KeyError:
            continue  # Skip entry if data is missing

    return forecast_data


if __name__ == "__main__":
    TARGET_CITY = "London"  # Change this to your desired city

    try:
        loc_id = get_location_id(TARGET_CITY)
        weather_report = get_weather_forecast(loc_id)

        # Print the final JSON output
        print(json.dumps(weather_report, indent=2, ensure_ascii=False))

    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"An error occurred: {e}")
```

## 5. How to Run

1. Replace the TARGET_CITY variable in the script with your desired city (e.g., "Mumbai").
2. Save the code as `get_weather.py`.
3. Open your terminal and run the script:

   ```bash
   python get_weather.py
   ```

4. The script will print the steps it's taking and finally output the JSON-formatted weather forecast. Copy this JSON to submit as your answer.
