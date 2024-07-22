import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
import os

# Define the scope
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

# Authorize the client
client = gspread.authorize(creds)

# Open the Google Sheet
sheet = client.open("template").sheet1

# Define the search term
search_term = "a3"

# Initialize a list to hold search results with row numbers
results_with_row = []

# Get all values from the sheet
all_values = sheet.get_all_values()

# Create a directory to save images
image_dir = "downloaded_images"
os.makedirs(image_dir, exist_ok=True)

# Function to download and save an image
def download_image(url, row_number, col_number):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        file_name = f"{image_dir}/row_{row_number}_col_{col_number}.jpg"
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"Image saved: {file_name}")
    except requests.RequestException as e:
        print(f"Failed to download image from {url}: {e}")

# Iterate through each row to find the search term and images
for row_number, row in enumerate(all_values, start=1):
    if search_term in row:
        results_with_row.append((row_number, row))
        for col_number, cell in enumerate(row, start=1):
            if cell.startswith("http"):  # Simple check to see if cell might contain a URL
                download_image(cell, row_number, col_number)

# Print the results with row numbers and full row data
for row_number, row_data in results_with_row:
    print(f"Row {row_number} contains the search term:")
    print(row_data)
