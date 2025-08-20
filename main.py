# Part 1: File Read & Write Challenge
# This program reads content from a file and writes a modified version to a new file.

def process_file(input_filename, output_filename):
    """Reads from an input file, capitalizes each line, and writes to an output file."""
    try:
        # Open the input file for reading
        with open(input_filename, 'r') as infile:
            lines = infile.readlines()

        # Modify the content (e.g., capitalize each line)
        modified_lines = [line.upper() for line in lines]

        # Open the output file for writing
        with open(output_filename, 'w') as outfile:
            for line in modified_lines:
                outfile.write(line)
        
        print(f"Successfully processed '{input_filename}' and saved to '{output_filename}'.")

    except FileNotFoundError:
        # Part 2: Error Handling Lab
        print(f"Error: The file '{input_filename}' was not found.")
    except Exception as e:
        # Handle any other potential errors
        print(f"An unexpected error occurred: {e}")

# Ask the user for a filename
input_file_name = input("Please enter the name of the file to read: ")
output_file_name = "output_" + input_file_name

# Call the function to process the file
process_file(input_file_name, output_file_name)