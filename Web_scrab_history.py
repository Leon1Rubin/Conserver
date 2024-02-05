import requests # import the requests library
import openpyxl # import the openpyxl library
from datetime import datetime # import the datetime library

# Define the URL (replace {ip} with the actual IP address)
url = "http://10.42.0.6/mfg/api/v2/livestatus"

# Make a GET request to retrieve the JSON data
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()
    
    # Extract the "data" field containing the records
    records = data.get("data", [])
    
    # Get the current date and time
    current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Create the Excel file name with the current date and time
    excel_file_name = f"livestatus_{current_datetime}.xlsx"
    
    # Create or load an existing Excel workbook
    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    
    # Add headers to the worksheet
    headers = [
        "Checkpoint", "Deviations", "End Time", "ETC", "Fixture", "Fixture Representation",
        "KWARGS", "Location", "MTIME", "Notes", "Playbook", "Session ID", "Site Code",
        "Start Time", "Status", "SW Release", "SW Version", "PN", "SN", "Work Order No", "FA"
    ]
    worksheet.append(headers)
    
    # Iterate through the records and add them to the worksheet
    for record in records:
        checkpoint = record.get("checkpoint", "N/A")
        deviations = record.get("deviations", "N/A")
        end_time = record.get("end_time", "N/A")
        etc = record.get("etc", "N/A")
        fixture = record.get("fixture", "N/A")
        fixture_repr = record.get("fixture_repr", "N/A")
        kwargs = record.get("kwargs", "N/A")
        location = record.get("location", "N/A")
        mtime = record.get("mtime", "N/A")
        notes = record.get("notes", "N/A")
        playbook = record.get("playbook", "N/A")
        session_id = record.get("session_id", "N/A")
        site_code = record.get("site_code", "N/A")
        start_time = record.get("start_time", "N/A")
        status = record.get("status", "N/A")
        sw_release = record.get("sw_release", "N/A")
        sw_version = record.get("sw_version", "N/A")
        top_pn = record.get("top_pn", "N/A")
        top_sn = record.get("top_sn", "N/A")
        work_order_no = record.get("work_order_no", "N/A")
        fa = str(record.get("fa", {}))  # Convert "fa" dictionary to string
        
        # Append data to the row
        row = [
            checkpoint,
            deviations,
            end_time,
            etc,
            fixture,
            fixture_repr,
            kwargs,
            location,
            mtime,
            notes,
            playbook,
            session_id,
            site_code,
            start_time,
            status,
            sw_release,
            sw_version,
            top_pn,
            top_sn,
            work_order_no,
            fa  # Add the "fa" field as a string
        ]
        
        worksheet.append(row)

    # Save the workbook to a file with the current date and time in the name
    workbook.save(excel_file_name)
    print(f"Excel file '{excel_file_name}' updated successfully.")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")