file_path: str = "../input.txt"
current_floor: int = 0

try:
    file_contents: str

    # Read the entire file contents into a string
    with open(file=file_path, mode="r") as file:
        file_contents = file.read()

    # Iterate through each character in the content string
    for char in file_contents:
        # Go up one floor for each opening parenthesis: `(`
        if char == "(":
            current_floor += 1
        # Go down one floor for each closing parenthesis: `)`
        elif char == ")":
            current_floor -= 1
        # Ignore LF character (line feed)
        elif ord(char) == 10:
            pass
        # Catch any unexpected characters and display an error message; should not occur
        else:
            print(f"Error: An invalid character was found in the input file: {char}")

    # Print the output (resulting floor)
    print(f"The instructions take Santa to floor {current_floor}")

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")

except Exception as e:
    print(f"An error occurred: {e}")
