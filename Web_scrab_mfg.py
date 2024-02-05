import requests
import openpyxl

# Define the URL (replace {ip} with the actual IP address)
url = "http://10.42.0.6/mfg/api/v1/workorders/"

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
        "Work Order ID",
        "Work Order Number",
        "Work Order Name",
        "Top Serial Number",
        "Top Part Number",
        "Deviations",
        "Start Time",
        "Start Reference",
        "FA Time",
        "FA Reference",
        "RTV Time",
        "RTV Reference",
        "End Time",
        "End Reference",
        "First Pass",
        "Cycle Time",
        "Runs Count",
        "Status",
        "FA Serial Number",
        "FA Failed Component Serial Number",
        "FA Stage",
        "FA ID",
        "FA Summary",
        "FA Status",
        "FA Owner",
        "RC ID",
        "RC Summary",
        "RC Status",
        "RC Owner",
        "RC Category 1",
        "RC Category 2",
        "RC Hardware Component",
        "RTVs",
        "FA URL",
        "RC URL",
    ]
    
    # Write the headers to the worksheet
    worksheet.append(headers)
    
    # Iterate through the records and process them
    for record in records:
        row = [
            record.get("id", "N/A"),
            record.get("number", "N/A"),
            record.get("name", "N/A"),
            record.get("top_sn", "N/A"),
            record.get("top_pn", "N/A"),
            record.get("deviations", "N/A"),
            record.get("start_time", "N/A"),
            record.get("start_reference", "N/A"),
            record.get("fa_time", "N/A"),
            record.get("fa_reference", "N/A"),
            record.get("rtv_time", "N/A"),
            record.get("rtv_reference", "N/A"),
            record.get("end_time", "N/A"),
            record.get("end_reference", "N/A"),
            record.get("first_pass", "N/A"),
            record.get("cycle_time", "N/A"),
            record.get("runs_count", "N/A"),
            record.get("status", "N/A"),
            record.get("fa_sn", "N/A"),
            record.get("fa_failed_component_sn", "N/A"),
            record.get("fa_stage", "N/A"),
            record.get("fa_id", "N/A"),
            record.get("fa_summary", "N/A"),
            record.get("fa_status", "N/A"),
            record.get("fa_owner", "N/A"),
            record.get("rc_id", "N/A"),
            record.get("rc_summary", "N/A"),
            record.get("rc_status", "N/A"),
            record.get("rc_owner", "N/A"),
            record.get("rc_category1", "N/A"),
            record.get("rc_category2", "N/A"),
            record.get("rc_hw_component", "N/A"),
            record.get("rtvs", "N/A"),
            record.get("fa_url", "N/A"),
            record.get("rc_url", "N/A"),
        ]
        
        # Append the row to the worksheet
        worksheet.append(row)
    
    # Save the workbook to a file
    workbook.save("workorders.xlsx")
    print("Data exported to workorders.xlsx")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
