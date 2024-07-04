# Arduino Image Visualizer

## Introduction
This project provides a web-based interface to visualize images on an Arduino board. It allows you to upload images, convert them into binary formats compatible with Arduino EEPROM, and send them to the board for display.

## Prerequisites
To run this project, you need the following:

- An Arduino board
- Arduino IDE
- Python IDE (e.g., PyCharm)

## Setup Instructions
1. **Upload Arduino Script**:
   - Upload the Arduino script provided (`arduino_file.ino`) to your Arduino board using the Arduino IDE.

2. **Set Up Python Environment**:
   - Create a Python virtual environment using the `requirements.txt` file provided:

     ```bash
     python -m venv venv
     source venv/bin/activate  # For Linux/macOS
     venv\Scripts\activate      # For Windows
     pip install -r requirements.txt
     ```

3. **Start the Server**:
   - Start the Flask server by running the following command:

     ```bash
     flask --app server run --host=0.0.0.0 --debugger --port 4000
     ```

4. **Access the Application**:
   - Open a web browser and navigate to [http://localhost:4000](http://localhost:4000) to access the application.
   - Or access it through other devices with the other link.

## Usage Notes
- **Arduino Operations**: Operations involving the Arduino may take a considerable amount of time. Each operation completion is signaled with an LED blink.
- **LED Functionality**: If you don't have an LED, you can disable the LED function in the Arduino script.
- **File Management**: When deleting or renaming files, ensure you update all related files:
  - `/static/images/drawings/example.png`
  - `/static/binfiles/example.txt`
  - `/static/decfiles/example.txt`

## Troubleshooting
- If the message "An error occurred: [Errno 2] No such file or directory: '../binfiles/drawing.txt'" appears when starting the server, it's not critical but may require investigation.

## Contributions
Contributions and improvements to this project are welcome. Please fork the repository, make your changes, and submit a pull request.
