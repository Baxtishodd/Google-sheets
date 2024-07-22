import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope of the credentials (we are using the Google Sheets API)
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

# Path to the Service Account JSON file downloaded from the Google API Console
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

# Authorize the client using the credentials
client = gspread.authorize(creds)

# Open the Google Sheet by its title
sheet = client.open('template').sheet1  # Replace with your actual Google Sheet name


# Modify the search_data function to include row number
def search_data(search_query, column_number):
    column_values = sheet.col_values(column_number)
    try:
        index = column_values.index(search_query)
        row_number = index + 1  # +1 because index is 0-based, rows are 1-based
        row_values = sheet.row_values(row_number)
        return row_values, row_number
    except ValueError:
        return None, None  # Return None if search query is not found


# Example usage:
search_query = 'Polo-1'
column_number = 1  # Column A (assuming 1-based indexing)
result = search_data(search_query, column_number)

if result:
    print(f"Found data: {result}")
    print(f"{column_number}")
else:
    print("Data not found.")
