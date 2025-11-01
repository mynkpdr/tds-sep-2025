# 7. Find newest GitHub user (0.75 Marks)

## 1. Problem Description

The task is to use the GitHub REST API to find the newest user who joined from a specific city (e.g., "London") and has more than a certain number of followers (e.g., `>50`). The final answer should be the user's account creation date in ISO 8601 format.

This simulates a recruitment task for "CodeConnect," a platform trying to identify emerging tech talent in specific regions.

## 2. Understanding the Requirements

- **Language**: Python.
- **Library**: `requests`.
- **API**: GitHub Search API (`https://api.github.com/search/users`).
- **Input**: A city name and a minimum follower count.
- **Logic**:
  1. Construct a query for the GitHub user search API. The query should combine location and follower filters (e.g., `q=location:London+followers:>50`).
  2. To find the _newest_ user, sort the results by join date in descending order (`sort=joined&order=desc`).
  3. Make a GET request to the API.
  4. The search result provides a list of users, but it contains limited information. The first user in the sorted list is the newest one.
  5. To get the full profile details (including the precise `created_at` date), you need to get the `url` for that user from the search result and make a _second_ API call to that specific user's profile URL.
  6. Parse the JSON from the user profile response and extract the `created_at` value.
- **Output**: The `created_at` timestamp as an ISO 8601 string (e.g., "2024-01-01T00:00:00Z").

## 3. Step-by-Step Solution

### Step 1: Set Up Environment

1. Create a project folder (e.g., `github_search`).
2. Set up and activate a virtual environment.
3. Install the `requests` library: `pip install requests`.
4. Create a Python file (e.g., `find_user.py`).

### Step 2: Write the Python Script

1. **Define Inputs**: Store the target city and follower count in variables.
2. **Search Users (First API Call)**:
   - Construct the URL for the user search API.
   - The query parameter `q` will combine the filters.
   - Add `sort=joined` and `order=desc` to get the newest users first.
   - Make the request. It's good practice to send an `Accept` header.
   - Extract the `url` of the first user from the `items` list in the response.
3. **Get User Profile (Second API Call)**:
   - Use the user's profile `url` obtained in the previous step to make a new GET request.
   - This response will contain the full user details.
4. **Extract Date**: Parse the JSON from the second response and get the value of the `created_at` key.
5. **Print Result**: Print the final date string.

## 4. Code (`find_user.py`)

```python
import requests
import os

def find_newest_github_user(location: str, followers: int) -> str:
    """
    Finds the creation date of the newest GitHub user from a specific location
    with a minimum number of followers.

    Args:
        location (str): The city to search for.
        followers (int): The minimum number of followers.

    Returns:
        str: The user's account creation date in ISO 8601 format.
    """

    # --- Step 1: Search for the user ---
    search_url = "https://api.github.com/search/users"
    query = f"location:{location} followers:>{followers}"
    params = {
        "q": query,
        "sort": "joined",
        "order": "desc"
    }
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }

    # Optional: Use a GitHub token to increase rate limits
    # token = os.getenv("GITHUB_TOKEN")
    # if token:
    #     headers["Authorization"] = f"token {token}"

    print(f"Searching for users with query: '{query}'...")
    search_response = requests.get(search_url, params=params, headers=headers)
    search_response.raise_for_status()
    search_data = search_response.json()

    if not search_data['items']:
        raise ValueError("No users found matching the criteria.")

    # The first item is the newest user
    newest_user_summary = search_data['items'][0]
    user_profile_url = newest_user_summary['url']
    print(f"Newest user found: {newest_user_summary['login']}. Fetching profile...")

    # --- Step 2: Get detailed profile to find the exact creation date ---
    profile_response = requests.get(user_profile_url, headers=headers)
    profile_response.raise_for_status()
    profile_data = profile_response.json()

    creation_date = profile_data.get("created_at")
    if not creation_date:
        raise ValueError("Could not find 'created_at' date in user profile.")

    return creation_date

if __name__ == "__main__":
    # --- Replace these with the values from your question ---
    TARGET_LOCATION = "London"
    MIN_FOLLOWERS = 50
    # ---------------------------------------------------------

    try:
        join_date = find_newest_github_user(TARGET_LOCATION, MIN_FOLLOWERS)
        print("\n--- Result ---")
        print(f"Newest user's join date: {join_date}")
        print("----------------\n")
    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"An error occurred: {e}")

```

## 5. How to Run

1. Save the code as `find_user.py`.
2. Modify the `TARGET_LOCATION` and `MIN_FOLLOWERS` variables to match your question.
3. Run the script from your terminal:

   ```bash
   python find_user.py
   ```

4. The script will print the ISO 8601 date string, which is your answer.

**Note**: The GitHub API has rate limits for unauthenticated requests. If you run into issues, you can create a [Personal Access Token](https://github.com/settings/tokens) and set it as an environment variable named `GITHUB_TOKEN` to increase the limit. The provided script will automatically use it if available.
