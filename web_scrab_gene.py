import requests
import openpyxl

# Define the URL
url = "http://10.42.0.6/genealogy/api/v1/search"

# Make a GET request to retrieve the JSON data
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()
    
    # Extract the "data" field containing the records
    records = data.get("data", [])
    
    # Create a new Excel workbook and add a worksheet
    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    
    # Define the column headers
    headers = [
        "Work Time",
        "Work Order Number",
        "Top Serial Number",
        "Parent Serial Number",
        "Serial Number",
        "Vast Part Number",
        "Type",
        "Vendor",
        "Model Number",
        "PSID",
        "Firmware Version",
        "BIOS Version",
        "BMC Version",
        "Quantity",
        "Work Reference Type",
        "Work Reference ID",
        "Work Name",
        "Location",
        "MFG Part Number",
        "OS Version",
        "MAC 0",
        "MAC 1",
        "MAC 2",
        "MAC 3",
        "MAC 4",
        "Work Location"
    ]
    
    # Write the headers to the worksheet
    worksheet.append(headers)
    
    # Iterate through the records and process them
    for record in records:
        row = [
            record.get("work_time", "N/A"),
            record.get("work_order_no", "N/A"),
            record.get("top_sn", "N/A"),
            record.get("parent_sn", "N/A"),
            record.get("sn", "N/A"),
            record.get("vast_pn", "N/A"),
            record.get("type", "N/A"),
            record.get("vendor", "N/A"),
            record.get("model_number", "N/A"),
            record.get("psid", "N/A"),
            record.get("firmware_version", "N/A"),
            record.get("bios_version", "N/A"),
            record.get("bmc_version", "N/A"),
            record.get("quantity", "N/A"),
            record.get("work_reference_type", "N/A"),
            record.get("work_reference_id", "N/A"),
            record.get("work_name", "N/A"),
            record.get("location", "N/A"),
            record.get("mfg_pn", "N/A"),
            record.get("os_version", "N/A"),
            record.get("mac0", "N/A"),
            record.get("mac1", "N/A"),
            record.get("mac2", "N/A"),
            record.get("mac3", "N/A"),
            record.get("mac4", "N/A"),
            record.get("work_location", "N/A"),
        ]
        
        # Append the row to the worksheet
        worksheet.append(row)
    
    # Save the workbook to a file
    workbook.save("genealogy_data.xlsx")
    print("Data exported to genealogy_data.xlsx")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
