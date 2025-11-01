# 5. Find the bounding box of a city (0.5 Marks)

## 1. Problem Description

The task is to write a Python script that uses the Nominatim API (based on OpenStreetMap data) to find the geographical bounding box for a specific city and country. You then need to extract either the minimum or maximum latitude from this bounding box.

This simulates a task for "UrbanRide," a logistics company that needs precise geographical data to define service zones.

## 2. Understanding the Requirements

- **Language**: Python.
- **Library**: `requests`.
- **API**: Nominatim Search API (`https://nominatim.openstreetmap.org/search`).
- **Input**: A city name, a country name, and whether to find the "minimum latitude" or "maximum latitude".
- **Logic**:
  1. Construct a request to the Nominatim API, passing the city and country as query parameters.
  2. Fetch the data and parse the JSON response. The API can return multiple results; we are interested in the one with `addresstype` of "city".
  3. From the correct result, extract the `boundingbox` array. This array contains four string values: `[min_latitude, max_latitude, min_longitude, max_longitude]`.
  4. Based on the problem's requirement, select the correct value (index 0 for min latitude, index 1 for max latitude).
- **Output**: The final latitude value as a number.

## 3. Step-by-Step Solution

### Step 1: Set Up Environment

1. Create a project folder (e.g., `nominatim_api`).
2. Create and activate a virtual environment.
3. Install the `requests` library: `pip install requests`.
4. Create a Python file (e.g., `find_bbox.py`).

### Step 2: Write the Python Script

1. **Define Inputs**: Store the target city, country, and the required parameter (e.g., "minimum latitude") in variables.
2. **Construct URL**: Create the URL for the Nominatim API. Key parameters are `format=jsonv2`, `city`, and `country`.
3. **Make API Call**: Use `requests.get()` to query the API. It is good practice to include a `User-Agent` header with your application's name or email, as required by Nominatim's usage policy.
4. **Filter and Extract**:
   - Parse the JSON response, which will be a list of results.
   - Iterate through the list to find the first result where `addresstype` is exactly "city". This is the most reliable way to get the primary city data.
   - Once found, access the `boundingbox` key.
   - Extract the required latitude value based on the problem statement (index 0 or 1).
5. **Print Result**: Print the final latitude value.

## 4. Code (`find_bbox.py`)

```python
import requests

def get_city_bounding_box(city: str, country: str, parameter: str):
    """
    Finds the specified bounding box parameter for a city using the Nominatim API.

    Args:
        city (str): The name of the city.
        country (str): The name of the country.
        parameter (str): The parameter to extract ("minimum latitude" or "maximum latitude").

    Returns:
        str: The requested bounding box value.
    """
    base_url = "https://nominatim.openstreetmap.org/search"
    params = {
        "format": "jsonv2",
        "city": city,
        "country": country
    }

    # Nominatim requires a custom User-Agent
    headers = {
        "User-Agent": f"UrbanRide-Data-Analysis-Project (23f3004197@ds.study.iitm.ac.in)"
    }

    print(f"Querying Nominatim for {city}, {country}...")
    response = requests.get(base_url, params=params, headers=headers)
    response.raise_for_status()

    results = response.json()

    if not results:
        raise ValueError("No results found for the specified city and country.")

    # Find the most relevant result (where addresstype is 'city')
    city_data = None
    for result in results:
        if result.get("addresstype") == "city":
            city_data = result
            break

    if not city_data:
        # Fallback to the first result if no exact city type is found
        city_data = results[0]
        print("Warning: Could not find result with addresstype 'city'. Using the first result.")

    bounding_box = city_data.get('boundingbox')
    if not bounding_box or len(bounding_box) != 4:
        raise ValueError("Bounding box data is missing or invalid in the API response.")

    print(f"Found bounding box: {bounding_box}")

    if parameter == "minimum latitude":
        return bounding_box[0]  # Min latitude is the first item
    elif parameter == "maximum latitude":
        return bounding_box[1]  # Max latitude is the second item
    else:
        raise ValueError(f"Invalid parameter specified: {parameter}")


if __name__ == "__main__":
    # --- Replace these with the values from your question ---
    TARGET_CITY = "Shanghai"
    TARGET_COUNTRY = "China"
    PARAMETER_TO_FIND = "minimum latitude" # or "maximum latitude"
    # ---------------------------------------------------------

    try:
        latitude = get_city_bounding_box(TARGET_CITY, TARGET_COUNTRY, PARAMETER_TO_FIND)
        print("\n--- Result ---")
        print(f"The {PARAMETER_TO_FIND} for {TARGET_CITY}, {TARGET_COUNTRY} is: {latitude}")
        print("----------------\n")
    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"An error occurred: {e}")
```

## 5. How to Run

1. Save the code as `find_bbox.py`.
2. Modify the `TARGET_CITY`, `TARGET_COUNTRY`, and `PARAMETER_TO_FIND` variables in the `if __name__ == "__main__":` block to match your specific question.
3. Run the script from your terminal:

   ```bash
   python find_bbox.py
   ```

4. The script will print the final latitude value, which you can submit as the answer.
