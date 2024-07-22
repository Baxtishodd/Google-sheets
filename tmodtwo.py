import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

# Authorize the client
client = gspread.authorize(creds)

# Open the Google Sheet
sheet = client.open("template").sheet1

# Define the search term
search_term = "6060"

# Initialize a list to hold search results with row numbers
results_with_row = []

# Get all values from the sheet
all_values = sheet.get_all_values()

# Iterate through each row to find the search term
for row_number, row in enumerate(all_values, start=2):
    if search_term in row:
        results_with_row.append((row_number, row))

# Print the results with row numbers and full row data
for row_number, row_data in results_with_row:
    print(f"Row {row_number} contains the search term: {search_term}")
    print(row_data)
    print(row_data[0])
    print(row_data[1])
    print(row_data[2])
    print(row_data[3])
    print(row_data[4])
    print(row_data[5])
    print(row_data[6])
    print(row_data[7])
    print(row_data[8])
    print(row_data[9])
    print(row_data[10])
    print(row_data[11])
    print(row_data[12])
    print(row_data[13])
    print(row_data[14])



# this is best for use