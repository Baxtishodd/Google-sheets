import gspread
from google.oauth2.service_account import Credentials

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "1RvQv1Mrs0r4UL-mCAMtBb6qJ7YOerOiETB6Z35xPSII"
workbook = client.open_by_key(sheet_id)
# sheet = client.open_by_key(sheet_id)

# val = worksheet.acell('B1').value
# values_list = sheet.sheet1.row_values(2)
# print(values_list)

# sheet.update_cell(1, 1, "Hello world this is changed")
 
sheet = workbook.worksheet("hello world")
value = sheet.acell("A1").value
print(value)

sheet.format("A1", {"textFormat": {"bold": True}})

values = [
    ["Name", "Price", "Quantity"],
    ["Basketball", 29.99, 1],
    ["Jeans", 39.99, 4],
    ["Soap", 7.99, 3]
]



worksheet_list = map(lambda x: x.title, workbook.worksheets())
new_worksheet_name = "Values"

if new_worksheet_name in worksheet_list:
    sheet = workbook.worksheet(new_worksheet_name)
else:
    sheet = workbook.add_worksheet(new_worksheet_name, rows=10, cols=10)


for i, row in enumerate(value):
    for j, value in enumerate(row):
        sheet.update_cell(i+1, j+1, value)


sheet.clear()

sheet.update(f"A1:C{len()}")
