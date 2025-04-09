#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def print_board(board):
    for row in board:
        print(" | ".join(row))
    print()

# Initialize board
board = [[" " for _ in range(3)] for _ in range(3)]

# Example: Placing a move
board[1][1] = "X"
print_board(board)


# In[ ]:


# -------------------------------------------------------------------
# User Authentication Program
# -------------------------------------------------------------------

# User Number, Last Name, First Name, Login Name, Passcode
userList = [[110,"Cashin","Bonnie","Cae110",7005],
            [101,"Cheruit","Madeleine","Che101",1507],
            [103,"Chanel","Coco","Cho103",7333],
            [107,"Gres","Madame","Gre107",3054],
            [114,"Hamnett","Katharine","Hae114",4807],
            [118,"Herrera","Carolina","Hea118",5567],
            [111,"Hulanicki","Barbara","Hua111",5125],
            [116,"Johnson","Betsey","Joy116",8869],
            [104,"Lanvin","Jeanne","Lae104",8580],
            [109,"McCardell","Claire","Mce109",5991],
            [102,"Paquin","Jeanne","Pae102",6495],
            [112,"Quant","Mary","Quy112",9028],
            [113,"Rykiel","Sonia","Rya113",1177],
            [105,"Schiaparelli","Elsa","Sca105",2980],
            [108,"Schlee","Valentina","Sca108",6801],
            [106,"Vionnet","Madeleine","Vie106",9042],
            [117,"Von Furstenberg","Diane","Voe117",2553],
            [119,"Wang","Vera","Waa119",2004],
            [115,"Westwood","Vivienne","Wee115",7806]]

# -------------------------------------------------------------------
# Function to perform linear search
# -------------------------------------------------------------------
def authenticate_user(login_name, passcode):
    """
    Searches for the login_name and passcode in the user list.
    Stops searching when it finds a login name that should have been after the target.
    """
    for user in userList:
        if user[3] > login_name:  # Stop if we pass the expected position
            break
        if user[3] == login_name and user[4] == passcode:
            return user  # Return the user record if found
    return None  # Return None if not found

# -------------------------------------------------------------------
# Main program execution
# -------------------------------------------------------------------
# Get user input
login_name = input("Enter your login name: ").strip()
passcode = int(input("Enter your four-digit passcode: "))

# Ensure passcode is within range
if 1000 <= passcode <= 9999:
    user = authenticate_user(login_name, passcode)

    # Output result
    if user:
        print(f"Welcome, {user[2]} {user[1]}!")
    else:
        print("Invalid login name or passcode.")
else:
    print("Passcode must be between 1000 and 9999.")


# In[ ]:


# Problem: Write a program that checks if a number is prime.

# Function to check if a number is prime
def is_prime(n):
    # A prime number is greater than 1, so return False if n is less than 2
    if n < 2:
        return False  

    # Loop from 2 up to the square root of n (inclusive)
    # This is because any factors of n greater than its square root would have already been found
    for i in range(2, int(n**0.5) + 1):  
        # If n is divisible by i, it's not a prime number
        if n % i == 0:
            return False  # Found a factor, so return False immediately

    # If no factors were found, the number is prime
    return True

# Prompt the user to enter a number
num = int(input("Enter a number: "))

# Check if the entered number is prime and display the result
if is_prime(num):
    print(f"{num} is a prime number.")  # Output if the number is prime
else:
    print(f"{num} is not a prime number.")  # Output if the number is not prime


# In[ ]:


# Implement the Bubble Sort algorithm to sort a list of numbers.

# Function to perform Bubble Sort on a list
def bubble_sort(arr):
    n = len(arr)  # Get the length of the list
    
    # Outer loop: Controls the number of passes (n iterations)
    for i in range(n):
        
        # Inner loop: Compares adjacent elements and swaps if needed
        # (n - i - 1) ensures we don't check already sorted elements at the end
        for j in range(n - i - 1):
            
            # If the current element is greater than the next one, swap them
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap operation

    # Return the sorted list
    return arr

# List of numbers to be sorted
numbers = [64, 34, 25, 12, 22, 11, 90]

# Call the bubble_sort function and store the sorted list
sorted_numbers = bubble_sort(numbers)

# Print the sorted list
print("Sorted List:", sorted_numbers)


# In[ ]:


# Problem: Convert a word into Pig Latin (Move the first consonant cluster to the end and add "ay").

# Function to convert a word into Pig Latin
def pig_latin(word):
    vowels = "aeiou"  # Define vowels for checking

    # Check if the first letter is a vowel
    if word[0] in vowels:
        return word + "ay"  # If it starts with a vowel, just add "ay" at the end

    else:
        # Loop through each letter to find the first vowel
        for i in range(len(word)):
            if word[i] in vowels:  # If a vowel is found
                # Move all letters before the first vowel to the end and add "ay"
                return word[i:] + word[:i] + "ay"

    # If the word has no vowels (e.g., "rhythm"), return the word with "ay" at the end
    return word + "ay"  

# Prompt the user to enter a word and convert it to lowercase
word = input("Enter a word: ").lower()

# Convert the word to Pig Latin and display the result
print("Pig Latin:", pig_latin(word))


# In[ ]:


# For loop examples

# Basic for loop with lists
print("For loop example 1")
fruits = ["apple", "banana", "cherry"]
# Loops through our fruits list
for fruit in fruits: # assigns each element to fruit one by one
    print(fruit) # prints the fruit list on seperate lines

# Using range() to loop a specific number a certain amount of times
print("\nFor loop example 2")
# Using the range() to loop to a specific number based upon the range
for i in range(5): # Range(5) generates numbers:[0, 1, 2, 3, 4]
    # The loop runs 5 times, printing the iteration number
    print("Iteration:", i)

# Using range(start, stop, step)    
print("\nFor loop example 3")
# Using range(start, stop, step)
for i in range(2, 10, 2):  # Start from 2, go up to 10 (exclusive), increment by 2
    # the loop prints these numbers [2, 4, 6, 8]
    print(i)

# Iterating through a string
print("\nFor loop example 4")
word = "Python"
# Iterates through each letter in "Python"
for letter in word:
    # Prints one letter per iteration
    print(letter)

# Looping through a dictionary
print("\nFor loop example 5")
#.          Key     Value,   Key  Value, Key   Value
student = {"name": "Alice", "age": 17, "grade": "A"}
# .Items() returns key-valued pairs 
for key, value in student.items(): 
    # prints each key and its value ("name:" = key, "Alice" = value)
    print(f"{key}: {value}")

# Using enumerate() to get index and value
print("\nFor loop example 6")
names = ["Alice", "Bob", "Charlie"]
# enumerate() provies both the index and the value
for index, name in enumerate(names):
    print(f"{index}: {name}")

# Nested for loop
print("\nFor loop example 7")
# the outer loop runs 3 times (i = 1,2,3)
for i in range(1, 4):  # Outer loop (1 to 3)
    # inner loop runs 2 times
    for j in range(1, 3):  # Inner loop (1 to 2)
        # total iterations is 3 * 2 = 6
        print(f"i={i}, j={j}")

# List comprehension (shortened for loop)
print("\nFor loop example 8")
numbers = [1, 2, 3, 4, 5]
# [num ** 2 for num in numbers] creates a new list of squared values
squared = [num ** 2 for num in numbers]  # Square each number
print(squared)

# For loop with break and continue
print("\nFor loop example 9")
for num in range(1, 6):
    if num == 3:
        # This will skip number three
        continue  # Skip 3
    if num == 5:
        # break will stop the loop at 5 but wil print out 4 since zero based
        break  # Stop at 5
    print(num)

# Using +1 in range()
print("\nFor loop example 10")
# range(1, 6 + 1) is the same as range(1, 7) meaning it includes 6
# Normally, range(1, 6) stops at 5, so adding +1 ensures it reaches 6
for i in range(1, 6 + 1):  # Loop from 1 to 6
    print(i)

# Using +1 for an accumulated sum
print("\nFor loop example 11")
total = 0
for i in range(1, 5):
    # Adds i+1 instead of i, shifting vales by 1
    total += i + 1  # Adding (i + 1) instead of i
print("Total Sum:", total) # (1+1) + (2+1) + (3+1) + (4+1) = 14

# +1 in finding the square root range 
print("\nFor loop example 12")
n = 36
# int(**0.5) + 1 ensures the loop cheacks all values up to the square root of n
# if n = 36 then it would be int(36**0.5) = 6, so range(2, 6 + 1) ensures 6 is included
for i in range(2, int(n**0.5) + 1):  # Check up to sqrt(n)
    print("Checking:", i)
    
# Using +1 to adjust indexing in lists
print("\nFor loop example 13")
numbers = [10, 20, 30, 40]
# i starts from 0, so i+1 makes inedxing start from 1 instead of zero
for i in range(len(numbers)):
    print(f"Position {i+1}: {numbers[i]}")
    
# Using +1 to prevent zero division 
print("\nFor loop example 14")
# i starts at 0, so i+1 ensures we never divide by zero
for i in range(5):
    print(10 / (i + 1))  # Prevents division by zero


# using +1 to create a countdown
print("\nFor loop example 15")
# 0 - 1 ensures the countdown includes 0
# Without -1, the loop would stop at 1
for i in range(10, 0 - 1, -1):  # Loop from 10 down to 0
    print(i)

# Using +1 in multiplication
print("\nFor loop example 16")
# Each i is multiplied by i+1
# For each value of i, the expression {i+1} gets the next number
# The multiplication i * (i+1) is then calculated 
for i in range(1, 5):
#                  1+1
    print(f"{i} × {i+1} = {i * (i+1)}")
# EX:        1  *  2    =  2

####### Summary #######

# +1 in range() ensures inclusion of the last number.
# +1 can adjust indexing for user-friendly output.
# +1 prevents division by zero.
# +1 helps in mathematical sequences like multiplication.

####### Summary #######


# In[ ]:


# Tic-Tac-Toe board game for GCSE testing examples 

def print_board(board):
    """Function to display the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))  # Print each row with separators
        print("-" * 9)  # Print horizontal line after each row


def check_winner(board, player):
    """Function to check if the player has won."""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):  # If all cells in a row match the player
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):  # Check each column
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):  # Top-left to bottom-right diagonal
        return True
    if all(board[i][2-i] == player for i in range(3)):  # Top-right to bottom-left diagonal
        return True

    return False  # No winner found


def is_full(board):
    """Function to check if the board is full (i.e., a draw)."""
    return all(cell != " " for row in board for cell in row)  # If no empty spaces, return True


def tic_tac_toe():
    """Main function to run the Tic-Tac-Toe game."""
    # Create a 3×3 grid initialized with empty spaces
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    # Define the two players: 'X' and 'O'
    players = ["X", "O"]
    turn = 0  # 0 for Player X, 1 for Player O

    while True:
        print_board(board)  # Display the current state of the board
        player = players[turn]  # Get the current player (X or O)
        
        # Ask for the player's move
        move = input(f"Player {player}, enter a position (1-9): ")

        # Validate that the input is a number between 1 and 9
        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("Invalid input. Enter a number between 1 and 9.")
            continue  # Ask again if input is invalid

        move = int(move) - 1  # Convert 1-9 input into a 0-based index (0-8)
        
        # the divemod() function in Python divides one number by another and returns 
        # both the quotient and remainder as a tuple 
        # move is a number between 0-8 (since the players enter 1-9, we subtract
        # 1 to make it 0-based)
        # divmod(move, 3) returns"
        # Quotient -> row(Which row the move is in)
        # Remainder -> col(Which column the move is in)
        # example: if the player enters in 5(which is converted to move = 4 by subtracting 1)
        # row, col = divmod(4, 3)
        # calculations:
        # 4 / 3 -> Quotiant = 1(row index)
        # 4 % 3 -> Remainder = 1(column index)
        # So the input of 5 from the player corresponds to board[1][1], which is the middle cell
        # of the tic-tac-toe board
        # Mapping of Player Inputs (1-9) to Board Indices (0-based)

        # Player Input:  move = input - 1:   divmod(move, 3) → (row, col)
#            1                  0                (0, 0)
#            2                  1                (0, 1)
#            3                  2                (0, 2)
#            4                  3                (1, 0)
#            5                  4                (1, 1)
#            6                  5                (1, 2)
#            7                  6                (2, 0)
#            8                  7                (2, 1)
#            9                  8                (2, 2)
        row, col = divmod(move, 3)  # Convert index into row & column

        # Check if the selected cell is already occupied
        if board[row][col] != " ":
            print("Invalid move! That space is already taken.")
            continue  # Ask for input again

        board[row][col] = player  # Place the player's mark on the board

        # Check if the current player has won
        if check_winner(board, player):
            print_board(board)  # Show final board state
            print(f"Player {player} wins!")  # Announce winner
            break  # End the game

        # Check if the board is full (a draw)
        if is_full(board):
            print_board(board)  # Show final board state
            print("It's a draw!")  # Announce draw
            break  # End the game

        turn = 1 - turn  # Switch turn between Player X (0) and Player O (1)

tic_tac_toe()  # Run the game

