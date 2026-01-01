# File Find and Replace Program

try:
    filename = input("Enter the file name: ")
    
    # Open the file in read mode
    with open(filename, "r") as file:
        content = file.read()

    print("\nFile content loaded successfully.\n")

    old_word = input("Enter the word to replace: ")
    new_word = input("Enter the new word: ")

    # Replace the word
    updated_content = content.replace(old_word, new_word)
  
    # Open the file in write mode
    with open(filename, "w") as file:
        file.write(updated_content)

    print("\nFile updated successfully!")

except FileNotFoundError:
    print("Error: The file does not exist.")

except PermissionError:
    print("Error: You do not have permission to access this file.")

except Exception as e:
    print("An unexpected error occurred:", e)
