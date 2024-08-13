try:
    # File Creation and Writing
    with open("my_file.txt", "w") as file:
        file.write("Hello, this is the first line.\n")
        file.write("This is the second line, including a number: 123.\n")
        file.write("And here is the third line with another number: 456.\n")
    print("File created and initial content written successfully.")

    # File Reading and Display
    with open("my_file.txt", "r") as file:
        content = file.read()
    print("\nReading the contents of 'my_file.txt':")
    print(content)

    # File Appending
    with open("my_file.txt", "a") as file:
        file.write("Appending the fourth line.\n")
        file.write("Fifth line with a number: 789.\n")
        file.write("Sixth line with text and number: Text 101.\n")
    print("Additional content appended successfully.")

    # Reading after appending
    with open("my_file.txt", "r") as file:
        content = file.read()
    print("\nReading the contents of 'my_file.txt' after appending:")
    print(content)

except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: You do not have permission to access this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("\nFile handling operations completed.")
