import json
import statistics

# The name of the JSON file provided by the quiz
DATA_FILE = "q-calculate-variance.json"


def calculate_sample_variance(filename):
    """
    Loads data from a JSON file and calculates its sample variance.
    """
    try:
        with open(filename, "r") as f:
            measurements = json.load(f)

        if len(measurements) < 2:
            print(
                "Error: At least two data points are needed to calculate sample variance."
            )
            return

        # The statistics.variance function correctly uses the N-1 denominator
        # for an unbiased estimate of the population variance.
        sample_var = statistics.variance(measurements)

        print(f"Loaded {len(measurements)} measurements.")
        print(f"Sample Variance: {sample_var}")
        print(f"Rounded to 2 decimal places: {sample_var:.2f}")

    except FileNotFoundError:
        print(
            f"Error: Data file '{filename}' not found. Make sure it's in the same directory."
        )
    except json.JSONDecodeError:
        print(
            f"Error: Could not decode JSON from '{filename}'. Please check the file format."
        )
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    calculate_sample_variance(DATA_FILE)
