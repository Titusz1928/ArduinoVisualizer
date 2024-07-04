def split_characters_to_lines(input_file, output_file):
    try:
        # Open the input file in read mode
        with open(input_file, 'r') as infile:
            # Read the content of the file
            content = infile.read()

        # Open the output file in write mode
        with open(output_file, 'w') as outfile:
            # Iterate over each character in the content
            for char in content:
                # Write each character followed by a newline to the output file
                outfile.write(char + '\n')

        print(f"Characters from {input_file} have been written to {output_file} line by line.")
    except Exception as e:
        print(f"An error occurred: {e}")

def split_bits_to_lines(bit_array, current_time):
    try:
        # Generate output file name based on current time
        output_file = f'static/binfiles/new_file_{current_time}.txt'

        # Open the output file in write mode
        with open(output_file, 'w') as outfile:
            # Iterate over each bit in the bit_array
            for bit in bit_array:
                # Write each bit followed by a newline to the output file
                outfile.write(f"{bit}\n")

        print(f"Bits have been written to {output_file} line by line.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Specify the input and output file paths
input_file = '../binfiles/drawing.txt'
output_file = 'output.txt'

# Call the function to split characters to lines
split_characters_to_lines(input_file, output_file)
