import os
import time

from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_babel import Babel
from PIL import Image
from datetime import datetime
from static.programs.arduino_operations import readEepromBinary,writeToEeprom
from static.programs.binToDec import bits_to_bytes
from static.programs.lineseparator import split_bits_to_lines

app = Flask(__name__)
# babel = Babel(app)


os.makedirs('static/binfiles', exist_ok=True)
os.makedirs('static/images/drawings', exist_ok=True)

@app.route("/")
def home():
    return render_template('home/index.html')

@app.route("/draw")
def draw():
    return render_template('draw/index.html')

# @app.route("/images")
# def images():
#
#     # current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
#     # filename = f'static/binfiles/new_file_{current_time}.txt'
#     # imagename = f'static/images/drawings/new_file_{current_time}.png'
#     #
#     # readEepromBinary(filename)
#     #
#     # with open(filename, 'r') as file:
#     #     lines = file.readlines()
#     #
#     # # Flatten bits into a single list
#     # bits = ''.join(line.strip() for line in lines)
#     #
#     # # Calculate width and height based on image dimensions
#     # width = 128  # Number of columns
#     # height = 64  # Number of rows
#     #
#     # # Create a new image with mode 'RGB' (3 channels)
#     # create_image(bits, height, imagename, width)
#     #
#     # print('Image saved')
#
#
#     # imagename="images/drawings/drawing.png"
#     #return render_template('image/index.html', image_name=imagename)
#     return render_template('images/index.html')

@app.route("/images")
def images():
    image_name = request.args.get('image_name')
    images_dir = os.path.join(app.static_folder, 'images', 'drawings')
    image_files = []

    for filename in os.listdir(images_dir):
        if os.path.isfile(os.path.join(images_dir, filename)):
            file_path = os.path.join(images_dir, filename)
            modification_time = os.path.getmtime(file_path)
            # Convert modification_time (Unix epoch) to datetime object
            mod_time_datetime = datetime.fromtimestamp(modification_time)
            # Format datetime as string
            formatted_mod_time = mod_time_datetime.strftime('%Y-%m-%d %H:%M:%S')
            image_files.append((filename, formatted_mod_time))  # Append tuple of (filename, formatted datetime)

    # Sort images by modification time (most recent first)
    image_files.sort(key=lambda x: x[1], reverse=True)
    print(image_name)
    if image_name:
        image_name = os.path.basename(image_name)
    print(image_name)
    return render_template('images/index.html', image_name=image_name, image_files=image_files)


@app.route("/load-arduino-image")
def load_arduino_image():
    #imagename = "ps2n.png"
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f'static/binfiles/new_file_{current_time}.txt'
    imagename = f'static/images/drawings/new_file_{current_time}.png'

    try:
        readEepromBinary(filename)
    except Exception as e:
        # Code that runs if the exception occurs
        return redirect(url_for('error'))


    readEepromBinary(filename)

    time.sleep(0.05)

    bits_to_bytes(filename)

    with open(filename, 'r') as file:
        lines = file.readlines()

     # Flatten bits into a single list
    bits = ''.join(line.strip() for line in lines)

    # Calculate width and height based on image dimensions
    width = 128  # Number of columns
    height = 64  # Number of rows

    # Create a new image with mode 'RGB' (3 channels)
    create_image(bits, height, imagename, width)

    print('Image saved')


    # Redirect back to the images page with the new image
    return redirect(url_for('images', image_name=imagename))

@app.route("/save-to-arduino")
def save_to_arduino():
    image_name = request.args.get('image_name')
    print(image_name)

    try:
        writeToEeprom(image_name)
    except Exception as e:
        # Code that runs if the exception occurs
        return redirect(url_for('error'))

    return redirect(url_for('images'))

@app.route('/save-image', methods=['POST'])
def save_image():
    data = request.get_json()
    bit_string = data['bitString']
    bit_array = [int(bit) for bit in bit_string]

    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f'static/binfiles/new_file_{current_time}.txt'
    imagename = f'static/images/drawings/new_file_{current_time}.png'


    bit_array.insert(0, 1)
    bit_array.append(1)

    split_bits_to_lines(bit_array,current_time)

    time.sleep(0.05)
    bits_to_bytes(filename)


    with open(filename, 'r') as file:
        lines = file.readlines()

    if lines:
        lines = lines[1:-1]

    # Flatten bits into a single list
    bits = ''.join(line.strip() for line in lines)


        # Calculate width and height based on image dimensions
    width = 128  # Number of columns
    height = 64  # Number of rows

    # Create a new image with mode 'RGB' (3 channels)
    create_image(bits, height, imagename, width)

    print('Image saved')

    # Respond with a JSON message (optional)
    return jsonify({'message': 'Bitstring received and processed successfully'})


@app.route("/error")
def error():
    return render_template('error/index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('notfound/index.html'), 404

def create_image(bits, height, imagename, width):
    img = Image.new('RGB', (width, height))
    # Create a PixelAccess object to manipulate pixels
    pixels = img.load()
    # Iterate through the bit array and set pixels accordingly
    index = 0
    for row in range(height):
        for col in range(width):
            # Ensure index is within bounds of the flattened bits array
            if index < len(bits):
                # Convert bit value to integer for comparison
                if bits[index] == '1':
                    pixels[col, row] = (0, 0, 0)  # Black color
                else:
                    pixels[col, row] = (255, 255, 255)  # White color
                index += 1
    # Save the image as PNG
    img.save(imagename, quality=95)  # Save to static directory


