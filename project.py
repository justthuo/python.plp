def read_and_modify_file():
    input_filename = input("Enter the name of the file to read: ")

    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
            print("File read successfully.")
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
        return
    except IOError:
        print(f"Error: Could not read the file '{input_filename}'.")
        return

    # Modify content (you can change this logic)
    modified_content = content.upper()

    output_filename = "modified_" + input_filename
    try:
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
            print(f"Modified content written to '{output_filename}'.")
    except IOError:
        print(f"Error: Could not write to the file '{output_filename}'.")

if __name__ == "__main__":
    read_and_modify_file()
