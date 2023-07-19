import selenium
from selenium.webdriver.common.keys import Keys
from googleapiclient.discovery import build
# Create a connection to your Google Sheet.
sheet_service = build('sheets', 'v4', credentials=credentials)
sheet_id = '1234567890'
sheet_name = 'Zillow Data'
# Write the data to your Google Sheet.
results = driver.find_elements_by_class_name("list-card")
for result in results:
    title = result.find_element_by_class_name("list-card-info").text
    price = result.find_element_by_class_name("list-card-price").text
    sheet_service.spreadsheets().values().append(
        sheet_id, sheet_name, values=[title, price],
        major_dimension='ROWS').execute()
