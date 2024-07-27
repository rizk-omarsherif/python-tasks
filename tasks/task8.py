"""
Task Number      : 8
Task Description : Write a Python script to fetch Bitcoin rates from an API and save the data to a CSV file.
Task Objective   : This task is an exercise in using the `requests` module to interact with web APIs and `pandas` to handle and store data in a tabular format.

Author  : Omar Rizk
Course  : Python Programming
Diploma : Embedded Linux Diploma (Under Supervision of Eng. Moatasem Elsayed)
"""

import requests
from pprint import pprint
import pandas as pd

# Fetch the Bitcoin rates data
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
json_data = response.json()

# Print the JSON data for debugging purposes
# pprint(json_data)

# Extract the required information
last_updated = json_data["time"]["updated"]
rate_in_euro = json_data["bpi"]["EUR"]["rate"]
rate_in_pounds = json_data["bpi"]["GBP"]["rate"]
rate_in_usd = json_data["bpi"]["USD"]["rate"]

# Create a pandas DataFrame with the extracted data
data = {
    "Currency": ["Euro", "Pounds", "USD"],
    "Rate": [rate_in_euro, rate_in_pounds, rate_in_usd]
}
df = pd.DataFrame(data)

# Add a column for the last updated time
df["Last Updated"] = last_updated

# Print the DataFrame
print(df)

# Write the DataFrame to a CSV file
df.to_csv("bitcoin_rates.csv", index=False)

print(f"Bitcoin rates have been written to 'bitcoin_rates.csv'.")
