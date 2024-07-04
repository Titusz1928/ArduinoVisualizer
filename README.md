Project Requirements
To run this project, you will need the following:

An Arduino board
Arduino IDE
Python IDE (e.g., PyCharm)
Getting Started
Upload Arduino Script:

First, upload the Arduino script to your Arduino board using the Arduino IDE.
Create Python Environment:

Set up the Python environment by installing the required packages listed in requirements.txt.
bash
Copy code
pip install -r requirements.txt
Start the Server:

Launch the Flask server using the following command:
bash
Copy code
flask --app server run --host=0.0.0.0 --debugger --port 4000
Access the Application:

Navigate to the provided URL to access the application.
Helpful Tips
Arduino Operations: Operations involving the Arduino may take some time. You can disable LED notifications if you do not have an LED available.

File Management:

When deleting or renaming files, ensure that you manage all three related files:
/static/images/drawings/example.png
/static/binfiles/example.txt
/static/decfiles/example.txt
Error Handling:

If you see the message "An error occurred: [Errno 2] No such file or directory: '../binfiles/drawing.txt'" when starting the server, it is not a critical issue but may require investigation to resolve.

