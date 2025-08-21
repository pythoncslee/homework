# -*- coding: utf-8 -*-
"""
Created on Sat Jun 14 09:43:49 2025

@author: L_CJO

"""

# -------------------------------------------------------------------------
# Program Name: RndomLotto.py
# Author      : Jemal Okutgen
# Date        : 14/07/2024 - Saturday
# Version     : 01 
# As per      : Requirements for Assignment_02 Part_03 Section 3.1
# --------------------------------------------------------------------------

# ----------------------------------------------------
# The following Code complies with the required 
# Programming Skills Checklist
# ----------------------------------------------------
# Items 01 - 03 are used throughout the code 
# ----------------------------------------------------
# ✔ 01. Apply Basic Language Syntax Rules
# ✔ 02. Use Data Types, Operators and Expressions
# ✔ 03. Apply Variables and Scope
# ----------------------------------------------------
# Items 04 - 09 will be identified by comments next to the code 
# ----------------------------------------------------
# ✔ 04. Use Program Library Functions
# ✔ 05. Use Sequence, Structure to Code Logic and Algorithms
# ✔ 06. Use Loop Structures to Code Logic and Algorithms
# ✔ 07. Use Array Data Structures
# ✔ 08. Perform File Handling ( Read and Write ) 
# ✔ 09. Perform String Manipulation
# ----------------------------------------------------



# ----------------------------------------------------
# 04. Use Program Library Functions
# ----------------------------------------------------
import random
import datetime
# ----------------------------------------------------

def generate_lotto_numbers(num_numbers, start_range, end_range):
    """Generates a list of unique random lotto numbers."""
    
    if num_numbers > (end_range - start_range + 1):
        return "Error: Number of requested numbers exceeds the available range"
    return random.sample(range(start_range, end_range + 1), num_numbers)

# ----------------------------------------------------
# 08. Perform File Handling ( Read and Write ) 
# ----------------------------------------------------
def write_to_file(name, numbers, filename="lotto_history.txt"):
    """Writes the generated lotto numbers and name to a file."""
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as file:
        # ----------------------------------------------------
        # 09. Perform String Manipulation
        # ----------------------------------------------------
        file.write(f"Name: {name}, Numbers: {numbers}, Timestamp: {timestamp}\n")
        # ----------------------------------------------------
# ----------------------------------------------------

def main():
    """Main function to handle user input and generate lotto numbers."""
    name = input("Enter your name: ")
    # ----------------------------------------------------
    #    06. Use Loop Structures to Code Logic and Algorithms
    # ----------------------------------------------------
    while True:
        try:
            num_numbers = int(input("How many lotto numbers do you want to generate? "))
            start_range = int(input("Enter the starting number for the range: "))
            end_range = int(input("Enter the ending number for the range: "))
            if num_numbers <= 0 or start_range >= end_range:
                print("Invalid input. Please enter valid number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
    # ---------------------------------------------------
    # ---------------------------------------------------
    # 07. Use Array Data Structures
    # ---------------------------------------------------
    numbers = generate_lotto_numbers(num_numbers, start_range, end_range)
    # ---------------------------------------------------
    
    # ----------------------------------------------------
    # 05. Use Sequence, Structure to Code Logic and Algorithms
    # ----------------------------------------------------
    if isinstance(numbers, str):
        print(numbers)
    else:
        print(f"Your lotto numbers are: {numbers}")
        write_to_file(name, numbers)
        print("Lotto numbers saved to history ( lotto_history.txt) ")
    # ----------------------------------------------------

if __name__ == "__main__":
    main()