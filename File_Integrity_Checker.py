"""
File Integrity Checker
Done by Jackson Lee
"""

import hashlib # Import the library with hash function

filepath = "C:\\Hash\\" # Save your target file under the path C:\Hash
hashfile = "example_hash.txt"

# Function to calculate SHA-256 hash
def calculate_hash(filepath):
    sha256 = hashlib.sha256() # Create a new SHA-256 hash object
    try:
# Try to open the file at the designated path: C:/Hash
        with open(filepath, "rb") as f: # Open the file in binary mode
            while chunk := f.read(8192): # Read up to 8192 bytes each time, assign to chunk. The loop ends once end of file reaches
                sha256.update(chunk) # Add the current chunk’s data to the ongoing hash calculation.
        return sha256.hexdigest() # Return the full SHA-256 hash as a hex string
    except FileNotFoundError: # If file does not exist
        print("File not found.")
        return None


# Step 1: Save original hash
def save_hash(filepath, hashfile):
    hash_val = calculate_hash(filepath) # Get the hash value by calculate hash function
    if hash_val:
        with open(hashfile, "w") as f:
            f.write(hash_val) # Save the hash value in a file for future comparison
        print("Hash saved.")

# Step 2: Check integrity by comparing with saved hash
def check_file_integrity(filepath, hashfile):
    current_hash = calculate_hash(filepath) # Calculate the current hash value of the file
    if not current_hash:
        return

    try:
        with open(hashfile, "r") as f: # Open the saved file with the stored hash value if any
            original_hash = f.read().strip()
    except FileNotFoundError:
        print("Hash file not found.")
        return

    if current_hash == original_hash: # Compare the value of current and original hash values, the file integrity maintain if the hash values are equal
        print("File integrity OK.")
    else:
        print("File has been changed!")

# First time: save hash
# save_hash(filepath, hashfile)

# Later: check if file is changed
# check_file_integrity(filepath, hashfile)

# === Main function ===p#
# Main menu function with 1. Compute and save the hash value in a file
#                         2. Check file integrity by comparing the current and stored hash values
def file_integrity():
    filepath = "C:\\Hash\\"

    print("=== File Integrity Checker ===")
    filename = input("Enter the filename: ").strip()
    filepath = filepath + filename  # Define the filename
    hashfile = filepath + ".sha256" # Assign the same filename for storing hash value, with an extension of sha256.

    # Display the main menu
    print("Choose an option:")
    print("1. Save hash")
    print("2. Check integrity")

    # Retrieve the choice from the user
    choice = input("Your choice (1 or 2): ").strip()

    if choice == "1":
        save_hash(filepath, hashfile)
    elif choice == "2":
        check_file_integrity(filepath, hashfile)
    else:
        print("Invalid choice. Please enter 1 or 2.")

# Run main if this script is executed
#if __name__ == "__main__":
#    main()