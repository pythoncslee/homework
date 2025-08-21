def scramble(data, key):
    # Shift each byte by key value
    new_bytes_list = []  # Create an empty list to store new byte values

    for byte in data:  # Loop through each byte in the original data
        new_byte = (byte + key) % 256  # Add key and wrap around using modulo 256 to avoid the value out of bound
        new_bytes_list.append(new_byte)  # Add the new byte value to the list

    new_bytes = bytes(new_bytes_list)  # Convert the list of bytes back to a bytes object

    return new_bytes

    #return bytes((byte + key) % 256 for byte in data)

def unscramble(data, key):
    # Reverse shift each byte by key value
    new_bytes_list = []  # Create an empty list to store new byte values

    for byte in data:  # Loop through each byte in the original data
        new_byte = (byte - key) % 256  # Add key and wrap around using modulo 256 to avoid the value out of bound
        new_bytes_list.append(new_byte)  # Add the new byte value to the list

    new_bytes = bytes(new_bytes_list)  # Convert the list of bytes back to a bytes object
    return new_bytes

    #return bytes((byte - key) % 256 for byte in data)

def encrypt_file(input_path, output_path, key):
    with open(input_path, "rb") as f_in:
        data = f_in.read()
    scrambled = scramble(data, key)
    with open(output_path, "wb") as f_out:
        f_out.write(scrambled)
    print(f"File encrypted and saved as {output_path}")

def decrypt_file(input_path, output_path, key):
    with open(input_path, "rb") as f_in:
        data = f_in.read()
    unscrambled = unscramble(data, key)
    with open(output_path, "wb") as f_out:
        f_out.write(unscrambled)
    print(f"File decrypted and saved as {output_path}")

# Example usage:
def main_scramble():
    filepath = "C:\\Hash\\"
    filename = input("Enter the filename: ").strip()
    filename = filepath + filename
    #key = 5  # simple shift key
    key = int(input("Enter key for encryption: "))
    #encrypt_file("original.txt", "encrypted.bin", key)
    #decrypt_file("encrypted.bin", "decrypted.txt", key)

    try:
        encrypt_file(filename, filename + ".bin", key)
        decrypt_file(filename + ".bin", filename + ".txt", key)
    except FileNotFoundError:
        print("File not found.")

#if __name__ == "__main__":
#    main_scramble()