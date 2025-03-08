### Overview
The purpose of this project is to create google calendar events based on a set of google sheet that was already
created. The intended audience of this service can use their computer terminals to manipulate the even entries. 


### How to Use
1. If this is the **BEGINNING** of the semester and there is a new google sheet, please follow these instructions:
    - Please add yvette-developer@events-to-gcal-453100.iam.gserviceaccount.com as a editor on gsheet and gcal
    - Open up terminal on your computer. Copy and paste the following command with the correct field filled in:
        - curl -X POST -d '[sheet_id] [calendar_id]' -H "Content-Type: text/plain" http://127.0.0.1:5000/new-semester
    - To find the sheet_id: open the google sheet and it is located in the url: ".../d/[sheet_id]/#grid...."
    - To find the calc_id: open the google calendar setting, scroll down and there should be a field named google cal
    - No need to include the brackets 
    - If it is successful, you should see a "Success" message and can check the google calendar
    - If there is an error, please screenshot the error message and contact me

2. If this is the **MIDDLE** of the semester, and new events was added to the google sheet, please follow these instructions:
    - Open up terminal on your computer. Copy and paste the following command with the correct field filled in:
        - curl -X POST http://127.0.0.1:5000/update
    - If it is successful, you should see a "Success" message and can check the google calendar
    - If there is an error, please screenshot the error message and contact me



curl -X POST -d '1OFypePvXuJsnKka5Z4P7sFUV1NiKef14UG0HD451FtU kpl.yvette@gmail.com' -H "Content-Type: text/plain" http://127.0.0.1:5000/new-semester