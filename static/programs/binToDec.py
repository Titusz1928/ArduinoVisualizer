import os

# def bits_to_bytes(input_file, output_file):
#     try:
#         # Open the input file in read mode
#         with open(input_file, 'r') as infile:
#             # Read all lines from the file and strip any extra whitespace
#             lines = [line.strip() for line in infile.readlines()]
#
#         # Remove the first and last lines
#         if lines:
#             lines = lines[1:-1]  # Remove the first and last lines
#
#         # Check if the number of lines is a multiple of 8
#         if len(lines) % 8 != 0:
#             print("The number of lines in the input file is not a multiple of 8.")
#             return
#
#         # Open the output file in write mode
#         with open(output_file, 'w') as outfile:
#             # Iterate through the lines in chunks of 8
#             for i in range(0, len(lines), 8):
#                 # Get 8 bits
#                 byte_bits = lines[i:i + 8]
#                 # Join the bits to form a binary string
#                 byte_str = ''.join(byte_bits)
#                 # Convert the binary string to a decimal number
#                 byte_value = int(byte_str, 2)
#                 # Write the decimal number to the output file
#                 outfile.write(f"{byte_value}\n")
#
#         print(f"Converted bits from {input_file} have been written to {output_file} as bytes.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

def bits_to_bytes(input_file):
    try:
        print("bits_to_bytes")
        # Get the filename without extension and remove folders
        filename = os.path.basename(input_file)

        output_file = f'static/decfiles/{filename}'
        input_file = f'static/binfiles/{filename}'

        print(output_file, input_file)

        #Open the input file in read mode
        with open(input_file, 'r') as infile:
            # Read all lines from the file and strip any extra whitespace
            lines = [line.strip() for line in infile.readlines()]

            # Remove the first and last lines
            if lines:
                lines = lines[1:-1]  # Remove the first and last lines

            # Check if the number of lines is a multiple of 8
            if len(lines) % 8 != 0:
                print("The number of lines in the input file is not a multiple of 8.")
                return

            # Open the output file in write mode
            with open(output_file, 'w') as outfile:
                # Iterate through the lines in chunks of 8
                for i in range(0, len(lines), 8):
                    # Get 8 bits
                    byte_bits = lines[i:i + 8]
                    # Join the bits to form a binary string
                    byte_str = ''.join(byte_bits)
                    # Convert the binary string to a decimal number
                    byte_value = int(byte_str, 2)
                    # Write the decimal number to the output file
                    outfile.write(f"{byte_value}\n")

            print(f"Converted bits from {input_file} have been written to {output_file} as bytes.")
    except Exception as e:
        print(f"An error occurred: {e}")


# # Specify the input and output file paths
# input_file = 'static/binfiles/dot.txt'
#
# # Call the function to convert bits to bytes
# bits_to_bytes(input_file)
