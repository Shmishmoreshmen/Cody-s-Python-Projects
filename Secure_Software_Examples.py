#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Secure Password Hashing (Avoid Plaintext Passwords)

import bcrypt  # Import the bcrypt library for secure password hashing

def hash_password(password: str) -> str:
    """
    Hashes a password using bcrypt.
    
    :param password: The plaintext password to hash.
    :return: The hashed password as a string.
    ||||||||||| Why is this secure |||||||||||
    Because, it uses bcrypt, which is a slow, adaptive hashing function (harder to brute-force).
    Salting ensures that even if two users have the same password, their hashes will be different.
    Hashes are one-way (can't be reversed), protecting user passwords even if a database is leaked.
    """
    # The bcrypt.gensalt() function will create a random salt value
    # A salt is a random value added to a password before hashing the value to
    # Make it unique.
    # This will pervent a rainbow table attack (precomputed hash lookups)
    salt = bcrypt.gensalt()  # Generate a unique salt
    
    # Password.encode() converts the inut password (a string) into bytes
    # Since bcrypt works with bytes
    # Bcrypt.hashpw() hashes the password using the generated salt
    hashed = bcrypt.hashpw(password.encode(), salt)  # Hash the password with the salt
    
    # The hashed password is originally in bytes format
    # .decode() converts it into a string, so it can be stored in a database easily
    return hashed.decode()  # Convert bytes to string for storage

def verify_password(password: str, hashed_password: str) -> bool:
    """
    Verifies a password against its hashed version.
    
    :param password: The plaintext password input.
    :param hashed_password: The stored hashed password.
    :return: True if the password matches, False otherwise.
    """
    # Returns a bool (True, or False)
    return bcrypt.checkpw(password.encode(), hashed_password.encode())  # Check if the password matches

# Example usage
hashed_pw = hash_password("SecurePass123!")  # Hash a sample password
print(f"Hashed Password: {hashed_pw}")

# Verify password
print(verify_password("SecurePass123!", hashed_pw))  # Should return True


# In[ ]:


# Prevent SQL Injecton (Uses Paramerterized Queries)

import sqlite3  # Import SQLite database module

def get_user(email: str):
    """
    Fetches user details securely using parameterized queries to prevent SQL injection.
    
    :param email: The email address to search for in the database.
    :return: The user record if found, else None.
    """
    conn = sqlite3.connect("secure.db")  # Connect to the database
    cursor = conn.cursor()
    
    # Secure way: Using parameterized queries
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    # Improper way
    # cursor.execute(f"SELECT * FROM users WHERE email = '{email}'")
    
    user = cursor.fetchone()  # Fetch the first matching user
    conn.close()  # Close the database connection
    
    return user  # Return the user record

# Example usage
email_input = "test@example.com"
user = get_user(email_input)  # Fetch user details safely
print(user)  # Display user info


# In[ ]:


# Validate User Input to Prevent Code Injection

import re  # Import regular expressions module

def validate_username(username: str) -> bool:
    """
    Validates a username to allow only alphanumeric characters and underscores.
    
    :param username: The username to validate.
    :return: True if valid, False otherwise.
    """
    pattern = r"^[a-zA-Z0-9_]{3,20}$"  # Allowed: letters, numbers, underscore (length: 3-20)
    return bool(re.match(pattern, username))  # Check if input matches pattern

# Example usage
print(validate_username("valid_user123"))  # True
print(validate_username("bad-user!"))     # False


# In[ ]:


# Secure File Handling (Avoid Arbitrary File Access)

import os  # Import the OS module for file path operations

def secure_file_access(filename: str):
    """
    Prevents unauthorized file access by restricting file paths.
    
    :param filename: The requested file name.
    :return: The file content if allowed, else raises an error.
    """
    # This code prevents path traversal attacks by ensuring that the file being 
    # accessed is strictly within a predefined safe directory (/secure/path)
    # os.path.basename(filename) removes path components, this will only extract the base
    # name (file.txt) from filename removing any directory componets, 
    # so this (../../ect/passwd) would become passwd
    # os.path.join() creates a full safe path
    # this will combine the safe directory with the sanatized filename
    safe_directory = "/secure/path"  # Define the safe directory
    full_path = os.path.join(safe_directory, os.path.basename(filename))  # Prevent path traversal
    
    # full_path.startswith(safe_directory will double check the path
    # this will ensure that the resulting path is still within safe_directory even if
    # tricks are used like .. to force a file redirect
    # Example: If an attacker somehow manages to construct "../../etc/passwd", 
    # this check would fail, and an exception would be raised.
    if not full_path.startswith(safe_directory):  # Ensure file is within the safe directory
        # If the file is outside safe_directory, the program raises an exception or error
        raise ValueError("Unauthorized file access attempt!")  # Reject access
    
    with open(full_path, "r") as f:  # Open the file securely
        return f.read()  # Read and return file content

# Example usage
try:
    print(secure_file_access("data.txt"))  # Secure file access
except ValueError as e:
    print(e)  # Print error message if access is denied


# In[ ]:


# Secure API Requests (Avoid Leaking Sensitive Data)

import requests  # Import requests module for API calls
from dotenv import load_dotenv  # Import dotenv to manage environment variables
import os  # Import OS module to fetch environment variables

# Load API keys from a .env file
load_dotenv()  # Load environment variables from .env file

API_KEY = os.getenv("API_SECRET_KEY")  # Get API key securely

def get_secure_data():
    """
    Sends a secure API request using authorization headers.
    
    :return: The API response data in JSON format, or None if failed.
    """
    # This line creates a dictionary called headers that includes an Authorization
    # header.
    # The authorization header is used in API requests that require authentication.
    # Where the value Bearer {API_KEY} means we are using a Bearer Token authentication
    # where API_KEY is a secret key (typically provided by the API provider) to gain
    # access to the API securely
    headers = {"Authorization": f"Bearer {API_KEY}"}  # Use secure authorization headers
    
    # The request.get() function sends an HTTP GET request to https://api.example.com/data,
    # asking the server for data.
    # the headers=headers part ensures that the authorization header is included in the request.
    # the response object stores the servers reply, including the HTTP status code and data
    response = requests.get("https://api.example.com/data", headers=headers)  # Send GET request
    
    # Checking the response status code
    # Every HTTP response comes with a status ode that will indicate the result of the request
    # 200 means OK (the request was successful, and the data was returned)
    # 404 means Not Found (the requested resource was not found or does not exsist)
    # 401 means Unauthorized (the API key might be missing or incorrect)
    # 500 means Internal Server Error (Somethig went wrong on the API server)
    if response.status_code == 200:  # Check if request was successful
        # If the request was successful (status code == 200) then the API usually responds
        # with JSON format
        # response.json() converts the response body (text) into a Python dictionary, 
        # making it easy to work with.
        return response.json()  # Return response data
    else:
        return None  # Return None if request failed

print(get_secure_data())  # Fetch and print secure API data


# In[ ]:


# Prevent Brute Force Attacks (Rate Limiting)

from flask import Flask, request  # Import Flask for web app
from flask_limiter import Limiter  # Import Flask Limiter for rate limiting
from flask_limiter.util import get_remote_address  # Import function to get user IP

# Creates an instance of a flask web application named app
# Core of the web server
app = Flask(__name__)  # Initialize Flask app

# Correct way to initialize Limiter
# Limiter is used to restrict the number of requests a user can make within a time frame
# key_func=get_remote_address ensures that rate limits are applied based on the users
# IP address
limiter = Limiter(key_func=get_remote_address)  # Use built-in function for IP tracking
# limiter.init_app(app) attaches the rate limiter to the Flask app.
limiter.init_app(app)  # Attach to Flask app

# This route listens for POST requests at /login.
@app.route("/login", methods=["POST"])  # Define login route
# The @limiter.limit("5 per minute") decorator enforces a restriction:
# A user can attempt to log in only 5 times per minute.
# If they exceed this limit, they will receive a 429 Too Many Requests response.
@limiter.limit("5 per minute")  # Allow max 5 login attempts per minute
# Simple function to return a message when a request is received
def login():
    return "Login attempt recorded."  # Return response

if __name__ == "__main__":
    app.run(debug=True)  # Run Flask app


# In[ ]:


# Securely Generate Random Data (Avoid random for Security)

import secrets  # Import secrets module for secure random generation

# Generate a 16-byte secure token
secure_token = secrets.token_hex(16)  # Generate a cryptographic random token
print(f"Secure token: {secure_token}")  # Print the generated token


# In[10]:


"""
Name: Cody Thomspon
Date: April 9, 2025
Project: Cybersecurity Toolkit
Project Description:
This Python cybersecurity toolkit 
provides essential security functionalities 
useful for various applications in need of cybersecurity.

1. Password Security
Hashing Passwords (hash_password, verify_password)
Use Case: Securely storing passwords in databases.
How it Helps: Instead of storing plaintext passwords, the toolkit hashes passwords 
using PBKDF2-HMAC-SHA256 with a salt, making it resistant to dictionary and 
brute-force attacks.
Verification: It allows for password validation without needing to store the original 
password.

2. Encryption & Data Protection
AES-GCM Encryption (encrypt_aes_gcm, decrypt_aes_gcm)
Use Case: Encrypting sensitive information like personally identifiable 
information (PII), financial data, or API keys.
How it Helps: Uses AES-GCM, which provides both encryption and integrity 
protection (via authentication tag), making it secure against tampering.

3. Message Authentication & Integrity
HMAC Generation & Verification (generate_hmac, verify_hmac)
Use Case: Ensuring message authenticity and integrity in communication protocols 
(e.g., API authentication, digital signatures).
How it Helps: Prevents attackers from modifying messages by using a cryptographic 
hash function (SHA-256) with a secret key.

4. Token Generation & Secure Authentication
Generating Secure Tokens (generate_secure_token)
Use Case: Creating secure session tokens, API keys, or unique identifiers in 
authentication mechanisms.
How it Helps: Uses cryptographic randomness to generate tokens that are difficult 
to predict or forge.

5. General Security Applications
Secure Application Development: Implement these security features into web 
applications, APIs, or mobile apps to enhance data protection.
Penetration Testing & Red Teaming: Use the hashing and encryption 
mechanisms to test and improve security implementations.
Secure File Storage: Encrypt files before storing them in databases or 
cloud environments.
Authentication Systems: Combine password hashing and HMAC verification 
for secure user authentication.

A hash in Python is a fixed-size numerical value generated from 
input data using a hash function. Hashing is commonly used for 
data integrity, password storage, digital signatures, and 
cryptography.

A hash-based function takes an input (e.g., a string, file, 
or message) and transforms it into a unique, fixed-length output 
(called a hash or digest). It is one-way, meaning you cannot 
reverse-engineer the original input from the hash.

@staticmethod is a decorator in Python that defines a method inside a 
class that does not depend on the instance (self) or class (cls). It 
behaves like a regular function but is grouped within a class for 
organizational purposes.

In Python, self is a conventionally named parameter that represents 
the instance of a class. It is used to access instance attributes 
and methods inside a class.
"""
# Import Modules
# Provides cryptographic hash functions such as SHA-256, SHA-512, and MD5.
import hashlib 
# Provides access to operating system features, such as generating 
# cryptographically secure random numbers.
import os 
# Provides Base64 encoding and decoding, often used for secure data transmission.
import base64 
# Implements Hash-based Message Authentication Code (HMAC).
import hmac 
# Used for generating cryptographically secure random numbers 
# (better than random for security).
import secrets 
# Imports PBKDF2-HMAC, a key derivation function for securely hashing passwords.
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC 
# Imports hash functions for cryptographic operations. 
# (Supports hash algorithms, SHA-256, SHA-512, and MD5)
from cryptography.hazmat.primitives import hashes 
# A class for encrypting and decrypting data.
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes 

# Start of CyberSecurityToolKit Class
class CyberSecurityToolkit:
    """
    Advanced Cybersecurity Toolkit with encryption, hashing, and 
    authentication utilities.
    """
##################################################################################################################################  
#
# Password Security
#
##################################################################################################################################  
    
    # This method generates a secure random salt of a specified length 
    # (default is 16 bytes).
    @staticmethod
    def generate_salt(length=16):
        """Generate a secure random salt."""
        # os.urandom(length) generates a sequence of random bytes of the given length 
        # (default is 16).
        # A salt is a random value added to the password before hashing, ensuring that 
        # the same 
        # password will have different hashes each time it is hashed 
        # (since the salt will be different).
        return os.urandom(length)  # Generates a random sequence of bytes for salt

    # This method hashes the provided password using PBKDF2-HMAC-SHA256 
    # (a secure hashing algorithm) with the 
    # given salt and a specified number of iterations.
    @staticmethod
    def hash_password(password: str, salt: bytes, iterations=100000):
        """Hash a password using PBKDF2-HMAC-SHA256."""
        # PBKDF2HMAC is a key derivation function that applies HMAC 
        # (Hash-based Message Authentication Code) 
        # with a chosen hashing algorithm (SHA-256 in this case) 
        # how would I how would I multiple times to strengthen the hash.
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),  # Uses SHA-256 as the hashing algorithm
            length=32,  # Generates a 32-byte hash (256 bits)
            # Salt is used to ensure that the hash is unique even for the same password.
            salt=salt,  # Uses the provided salt for added security
            # Iterations define how many times the hashing function is applied, 
            # making it computationally expensive and resistant to brute force attacks.
            iterations=iterations,  # Number of iterations for key derivation (increases security)
        )
        # password.encode() converts the password string into bytes.
        # The kdf.derive() method applies the PBKDF2-HMAC-SHA256 algorithm 
        # to the password and salt.
        # Finally, the resulting hash is base64 encoded to represent 
        # it as a readable string.
        return base64.b64encode(kdf.derive(password.encode()))  # Encodes the derived key in base64

    # This method verifies if the provided password matches the stored (hashed) 
    # password. The method hashes the input password with the stored salt 
    # using the same hash_password function. It compares the newly generated 
    # hash with the stored hashed_password. If they match, the password is correct.
    @staticmethod
    def verify_password(password: str, hashed_password: bytes, salt: bytes):
        """Verify a password against a stored hash."""
        return CyberSecurityToolkit.hash_password(password, salt) == hashed_password
      
##################################################################################################################################  
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
##################################################################################################################################  
#
# Encryption & Data Protection
#
##################################################################################################################################  
    
    @staticmethod
    def encrypt_aes_gcm(plaintext: str, key: bytes):
        """Encrypt plaintext using AES-GCM.
        (Advanced Encryption Standard - Galois/Counter Mode)
        is a cryptographic encryption algorithm that provides 
        both confidentiality (encryption) and integrity/authentication 
        (via an authentication tag). It is widely used in secure 
        communications and data protection.
        """
        iv = os.urandom(12)  # Generates a 96-bit Initialization Vector (IV) for AES-GCM
        cipher = Cipher(algorithms.AES(key), modes.GCM(iv))  # Initializes AES cipher in GCM mode
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()  # Encrypts data
        return iv + encryptor.tag + ciphertext  # Returns IV, authentication tag, and ciphertext

    @staticmethod
    def decrypt_aes_gcm(ciphertext: bytes, key: bytes):
        """Decrypt ciphertext using AES-GCM."""
        # iv = ciphertext[:12] -> Extracts the first 12 bytes (IV or Initialization Vector).
        # tag = ciphertext[12:28] -> Extracts the next 16 bytes (Authentication Tag).
        # ciphertext = ciphertext[28:] -> Extracts the remaining bytes that 
        # contain the actual encrypted data.
        iv, tag, ciphertext = ciphertext[:12], ciphertext[12:28], ciphertext[28:]  # Extract IV, tag, and ciphertext
        cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag))  # Recreate cipher with the same IV and tag
        decryptor = cipher.decryptor()
        return decryptor.update(ciphertext) + decryptor.finalize()  # Decrypts data
    
####################################################################################################################################
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
####################################################################################################################################  
#
# Message Authentication & Integrity
#
####################################################################################################################################  

    # creates a HMAC (a cryptographic signature) using SHA-256.
    # uses a secret (key) and message (message)
    # converts the messge to bytes 
    # Uses the HMAC-SHA256 to generate a unique signature.
    # Returns the hexadecimal representation of the signature.
    # Ensures message integrity and authentication, commonly used 
    # in APIs and secure communication.
    @staticmethod
    def generate_hmac(key: bytes, message: str):
        """Generate an HMAC signature."""
        return hmac.new(key, message.encode(), hashlib.sha256).hexdigest()  # Creates an HMAC using SHA-256

    # Verifies if the generated HMAC matches the expected one.
    # recomputes the HMAC of message using key
    # compares it securely (using compare_digest, which prevents timing attacks).
    # Helps validate that a message has not been tampered with.
    @staticmethod
    def verify_hmac(key: bytes, message: str, expected_hmac: str):
        """Verify an HMAC signature."""
        return hmac.compare_digest(CyberSecurityToolkit.generate_hmac(key, message), expected_hmac)  # Prevents timing attacks

    # Generates a random secure token (e.g., for authentication or session management).
    # uses Pythons secrets module for cCryptographic randomness
    # Generates a hexadecimal token of length in bytes 
    # Useful for password reset links, API keys, and authentication tokens.
    @staticmethod
    def generate_secure_token(length=32):
        """Generate a cryptographically secure token."""
        return secrets.token_hex(length)  # Generates a secure random hexadecimal token

####################################################################################################################################
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
####################################################################################################################################  
#
# Main For Program Run
#
####################################################################################################################################  

# Example usage
if __name__ == "__main__":
    toolkit = CyberSecurityToolkit()
    
    # Hashing a password
    # Salting a hash is a technique used in cryptography 
    # to strengthen password storage and prevent attacks 
    # like rainbow table attacks. A salt is a random value 
    # added to a password before hashing to make the output 
    # unique, even if two users have the same password.
    salt = toolkit.generate_salt()
    password_to_varify = "securepassword"
    hashed_pw = toolkit.hash_password(password_to_varify, salt)
    print(f"Password before salt and hash: {password_to_varify}")
    print(f"Salt: {salt.hex()}")  # Prints the salt in hexadecimal format
    print(f"Hashed Password: {hashed_pw.decode()}")  # Prints the hashed password
    is_valid = toolkit.verify_password(password_to_varify, hashed_pw, salt)
    if is_valid:
        print("Password is valid!")
    else:
        print("Password is not valid")
    
    # Encrypting and decrypting data
    key = os.urandom(32)  # Generates a 256-bit AES key
    encrypted_data = toolkit.encrypt_aes_gcm("Sensitive data", key) # Encrypt the "Sensitive data"
    decrypted_data = toolkit.decrypt_aes_gcm(encrypted_data, key)# Decrypted the "Sensitive data"
    print("\nData before encryption: Sensitive data")
    print(f"Encrypted Data: {encrypted_data}") # Prints the encrypted data 
    print(f"Decrypted Data: {decrypted_data.decode()}")  # Prints the decrypted data
    
    # HMAC authentication
    secret_key = os.urandom(32)  # Generates a random key for HMAC
    message = "Authenticate this message"
    hmac_signature = toolkit.generate_hmac(secret_key, message)
    print(f"\nHMAC Signature: {hmac_signature}")  # Prints the generated HMAC
    
    # Generating secure token
    token = toolkit.generate_secure_token()
    print(f"\nSecure Token: {token}")  # Prints the cryptographically secure token


# In[ ]:


# Decimal to Binary and Binary to decimal

def decimal_to_binary(decimal_num):
    """Convert a decimal number to binary."""
    if decimal_num == 0:
        return "0"
    
    binary = ""
    while decimal_num > 0:
        remainder = decimal_num % 2  # Get remainder when dividing by 2
        binary = str(remainder) + binary  # Add remainder to the front of binary string
        decimal_num //= 2  # Reduce the number by dividing it by 2
    
    return binary


def binary_to_decimal(binary_str):
    """Convert a binary number (as a string) to decimal."""
    decimal = 0
    power = 0  # Keep track of the power of 2

    # Reverse iterate through the binary string
    for digit in reversed(binary_str):
        if digit == '1':
            decimal += 2 ** power  # Add the corresponding power of 2
        power += 1  # Increase the power for the next digit
    
    return decimal


# Test the functions
print("Function tests")
decimal_number = 200
binary_result = decimal_to_binary(decimal_number)
print(f"Decimal {decimal_number} -> Binary {binary_result}")

binary_number = "11001000"
decimal_result = binary_to_decimal(binary_number)
print(f"Binary {binary_number} -> Decimal {decimal_result}")

# Allow user input for decimal to binary conversion
decimal_number = int(input("\nEnter a decimal number to convert to binary: "))
binary_result = decimal_to_binary(decimal_number)
print(f"Decimal {decimal_number} -> Binary {binary_result}")

# Allow user input for binary to decimal conversion
binary_number = input("Enter a binary number to convert to decimal: ")
decimal_result = binary_to_decimal(binary_number)
print(f"Binary {binary_number} -> Decimal {decimal_result}")


# In[ ]:


1. Binary & Data Representation
Q1: Convert the decimal number 200 into binary.
Q2: Convert the binary number 11010110 into decimal.
get_ipython().set_next_input('Q3: How many bits are in a byte');get_ipython().run_line_magic('pinfo', 'byte')
Q4: Explain the difference between lossy and lossless compression.
get_ipython().set_next_input('Q5: What is the purpose of ASCII and Unicode');get_ipython().run_line_magic('pinfo', 'Unicode')

2. Algorithms & Programming
get_ipython().set_next_input('Q6: What is an algorithm');get_ipython().run_line_magic('pinfo', 'algorithm')
Q7: Write a simple pseudocode algorithm that asks the user for a number and prints whether it is even or odd.
get_ipython().set_next_input('Q8: What does the following Python code output');get_ipython().run_line_magic('pinfo', 'output')
for i in range(1, 6):
    print(i * 2)
Q9: Explain the difference between a for loop and a while loop.
get_ipython().set_next_input('Q10: What is the purpose of an if statement in programming');get_ipython().run_line_magic('pinfo', 'programming')

3. Cyber Security & Networks
get_ipython().set_next_input('Q11: What is phishing');get_ipython().run_line_magic('pinfo', 'phishing')
Q12: Describe one method to create a strong password.
get_ipython().set_next_input('Q13: What is the role of a firewall in a computer network');get_ipython().run_line_magic('pinfo', 'network')
Q14: Define the term encryption and explain why it is important.
get_ipython().set_next_input('Q15: What is the difference between a virus, worm, and Trojan horse');get_ipython().run_line_magic('pinfo', 'horse')

4. Computer Systems & Hardware
get_ipython().set_next_input('Q16: What is the purpose of a CPU');get_ipython().run_line_magic('pinfo', 'CPU')
Q17: Explain the difference between RAM and ROM.
get_ipython().set_next_input('Q18: What is virtual memory, and why is it used');get_ipython().run_line_magic('pinfo', 'used')
Q19: Identify two input devices and two output devices.
get_ipython().set_next_input('Q20: What is the difference between secondary storage and primary storage');get_ipython().run_line_magic('pinfo', 'storage')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


# In[ ]:


1. Binary & Data Representation
Q1: 200 in binary is 11001000.
Q2: 11010110 in decimal is 214.
Q3: There are 8 bits in a byte.
Q4:
Lossy compression reduces file size by permanently removing some data (e.g., JPEG, MP3).
Lossless compression reduces file size without losing any data (e.g., PNG, ZIP).

Q5:
ASCII (American Standard Code for Information Interchange) represents characters using 7 or 8 bits, but it only covers English characters.
Unicode supports multiple languages and symbols, using different encoding formats like UTF-8 and UTF-16.

2. Algorithms & Programming
Q6: An algorithm is a step-by-step set of instructions designed to perform a specific task or solve a problem.

Q7: Pseudocode for even or odd check:

BEGIN
    OUTPUT "Enter a number: "
    INPUT number
    IF number MOD 2 = 0 THEN
        OUTPUT "Even"
    ELSE
        OUTPUT "Odd"
    ENDIF
END

Q8: The output of the Python code:

2  
4  
6  
8  
10  

Q9:
A for loop runs a set number of times (e.g., iterating through a range or list).
A while loop runs indefinitely until a condition becomes false.

Q10: An if statement allows a program to make decisions by executing different code blocks based on conditions.

3. Cyber Security & Networks
Q11: Phishing is a cyber attack where criminals trick people into revealing sensitive information (e.g., passwords) via fake emails or websites.

Q12: A strong password should be long, include a mix of uppercase/lowercase letters, numbers, and special characters, and should not use common words or personal information.

Q13: A firewall monitors and controls incoming and outgoing network traffic, blocking unauthorized access to protect the system.

Q14: Encryption is the process of converting data into a secure format using an algorithm, ensuring only authorized users can access it. It protects sensitive data from cyber threats.

Q15:
Virus: A malicious program that attaches itself to files and spreads when executed.
Worm: A self-replicating malware that spreads through networks without user action.
Trojan Horse: A malicious program disguised as legitimate software, tricking users into installing it.

4. Computer Systems & Hardware
Q16: The CPU (Central Processing Unit) is the brain of the computer that executes instructions and processes data.
Q17:

RAM (Random Access Memory) is temporary, volatile memory used for running programs.
ROM (Read-Only Memory) is permanent, non-volatile memory storing essential startup instructions (BIOS).
Q18: Virtual memory is a section of the hard drive used as extra RAM when physical RAM is full. It helps run large programs but is slower than actual RAM.
Q19:
Input devices: Keyboard, Mouse
Output devices: Monitor, Printer
Q20:
Primary storage (e.g., RAM) is fast and temporary.
Secondary storage (e.g., HDD, SSD) is slower but permanent, used for long-term data storage.


# In[ ]:


pip install cryptography


# In[ ]:





# In[ ]:





# In[ ]:


# Q2
# -------------------------------------------------------------------
# Import libraries
# -------------------------------------------------------------------
import turtle  # Import the turtle graphics library

# -------------------------------------------------------------------
# Constants
# -------------------------------------------------------------------
WIDTH = 800
HEIGHT = 600
BIG = 8  # Constant for pen size

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# Setup the turtle environment
# =====> The argument to turtle.mode() is a string ("standard"), which is of type str
turtle.mode("standard")
screen = turtle.Screen()

# =====> Fix the NameError: Correct spelling of HEIGHT
screen.setup(WIDTH, HEIGHT)
turtle.screensize(WIDTH, HEIGHT)

# Prepare the turtle
# =====> Fix the AttributeError: The correct function call is turtle.Turtle() with an uppercase "T"
theTurtle = turtle.Turtle()  # Create a turtle
theTurtle.penup()

# Draw grid lines
theTurtle.setpos(-200, 0)  # Move turtle to start horizontal line
theTurtle.setheading(0)  # Face right

# =====> Fix the TypeError: pendown() does not take arguments, remove (200)
theTurtle.pendown()
theTurtle.forward(400)  # Draw horizontal line
theTurtle.penup()

# =====> Fix the logic error: The vertical axis was too far right, move to (0, 200)
theTurtle.setpos(0, 200)
theTurtle.setheading(270)  # Face downward
theTurtle.pendown()

# =====> Fix the logic error: The vertical axis should be 400, not 100
theTurtle.forward(400)  # Draw vertical line
theTurtle.penup()

# Draw a square
theTurtle.setpos(-200, -200)  # Lower left corner of square

# =====> Fix the logic error: Set heading to 90 (point north) instead of 95
theTurtle.setheading(90)  # Point north
theTurtle.pendown()
for count in range(4):
    theTurtle.forward(400)  # Draw side of square
    theTurtle.right(90)  # Turn right
theTurtle.penup()

# Draw a circle
theTurtle.setpos(100, 0)  # Position turtle at the right edge of the circle
theTurtle.setheading(90)  # Face upwards

# =====> Add a line to set the size of the pen to the constant BIG
theTurtle.pensize(BIG)  

# =====> Add a line to set the colour of the pen to gold
theTurtle.pencolor("gold")  

theTurtle.pendown()
theTurtle.circle(100)  # Draw a circle with radius 100
theTurtle.penup()

# =====> Add a line to hide the turtle
theTurtle.hideturtle()

print("Be sure to close the turtle window.")
turtle.done()


# In[ ]:


# Q3
# -------------------------------------------------------------------
# Import libraries
# -------------------------------------------------------------------
import math  # Import the math library to use mathematical constants and functions

# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
squareArea = 0     # Variable to store the area of the square
excessArea = 0.0   # Variable to store the excess area after cutting out the circle
side = 0           # Variable to store the length of the square's side
radius = 0         # Variable to store the radius of the circle
diameter = 0       # Variable to store the diameter of the circle

# Set the variable with a value of the correct data type
circleArea = 0.0   # Variable to store the area of the circle (float for precision)

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# Prompt the user to enter the length of the square's side and convert it to an integer
side = int(input("Enter the length of a side for the square: "))

# Prompt the user to enter the radius of the circle and convert it to an integer
radius = int(input("Enter the radius of the circle: "))

# Calculate the diameter of the circle (diameter = 2 * radius)
diameter = 2 * radius  

# Check if the circle fits inside the square
# If the diameter of the circle is greater than the side length, it won't fit
if diameter > side:
    print("Invalid input")  # Inform the user that the circle is too large
else:
    # Calculate the area of the square (side * side)
    squareArea = side * side  

    # Calculate the area of the circle using the formula πr²
    circleArea = math.pi * (radius ** 2)  

    # Calculate the excess area (remaining card after cutting out the circle)
    excessArea = squareArea - circleArea  

    # Output the calculated excess area
    print("Excess area is", excessArea)


# In[ ]:


#Q4
# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
layout = "{} is {}" # Format stringused to print the output as "binary is decimal"
binary = "" # A string that will store user's binary output
denary = 0 # An integer that will store the converted decimal value
# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------

# This function converts binary string into a decimal number
def binaryLoop(pBinary):
    """Convert a binary string to decimal (denary)."""
    total = 0 # Stores the final decimal value
    multiplier = 1 # Starts at 1 (representing 2^0), used to multiply each binary digit

    for index in range(len(pBinary) - 1, -1, -1):  # Iterate from right to left
        digit = pBinary[index] # Get the current binary digit 
        value = multiplier * int(digit) # Converts digit to an int and multiplies
        total = total + value # Add total to decimal value
        multiplier = multiplier * 2  # Increase multiplier (powers of 2)

    return total # Returns the final decimal number

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# Gets the users inout for binary number which also starts the loop
binary = input("Enter a binary number (empty to exit): ")

# Repeats until the user enters an empty string
while binary != "":
    denary = binaryLoop(binary)  # Convert binary to decimal
    print(layout.format(binary, denary))  # Print result
    binary = input("Enter a binary number (empty to exit): ") # Ask for new input (loop)


# In[ ]:


# Q5
# define the constances
OUTPUT_FILE = "Q05_OUTPUT.txt" # name of output file
MAX_PER_LINE = 7 # Limits the number of values per line to 7

weightsUsed = [3.79, 4.16, 1.52, 3.66, 2.58, 4.89, 4.37, 2.95, 2.58, 
               4.37, 4.59, 2.61, 6.13, 4.49, 1.66, 2.65, 4.64, 4.72,
               3.59, 4.56, 4.23, 2.15, 4.03, 2.47, 4.61, 4.55, 6.31,
               5.81, 2.63, 3.61, 3.49, 4.49, 3.02, 3.86, 6.23, 3.11,
               1.79, 2.62, 2.23, 2.34, 5.66, 4.58, 3.52, 1.53, 2.07,
               3.89, 3.48, 5.52, 6.38, 3.77, 1.74, 1.78, 3.87, 3.45,
               3.79, 3.36, 1.87, 2.12, 2.09, 2.84, 2.29, 4.46, 3.36]
# Initialize varables
count = 1
outLine = ""

# open the file for writing 
theFile = open (OUTPUT_FILE, "w")

# Loop through th elist weights used
for num in weightsUsed:
    
    # Converts the number to a string and appends it to outLine
    outLine = outLine + str (num)
    
    # checks if MAX_PER_LINE is reached
    if (count == MAX_PER_LINE):
        
        # adda. newline to move to the next line
        outLine = outLine + "\n"
        
        # writes outLine to the file
        theFile.write (outLine)
        
        # Reset outLine and count for the next line
        outLine = ""
        count = 1
    # else is fewer than 7 numbers are in the line, a comma is added
    # then we continue reading the file
    else:
        outLine = outLine + ","
        
        # Increment count to count the lines if 7 was not yet reached
        count = count + 1
        
# Close the file when we are all done       
theFile.close()


# In[ ]:


# Q5 differant sheet
# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------

# Stores all valid words with there point values 
wordTable = [["AA", 2], ["AB", 4], ["AD", 3], ["AE", 2], ["AG", 3],
         ["AH", 5], ["AI", 2], ["AL", 2], ["AM", 4], ["AN", 2],
         ["AR", 2], ["AS", 2], ["AT", 2], ["AW", 5], ["AX", 9],
         ["AY", 5], ["BA", 4], ["BE", 4], ["BI", 4], ["BO", 4],
         ["BY", 7], ["DA", 3], ["DE", 3], ["DO", 3], ["ED", 3],
         ["EF", 5], ["EH", 5], ["EL", 2], ["EM", 4], ["EN", 2],
         ["ER", 2], ["ES", 2], ["ET", 2], ["EW", 5], ["EX", 9],
         ["FA", 5], ["FE", 5], ["GI", 3], ["GO", 3], ["HA", 5],
         ["HE", 5], ["HI", 5], ["HM", 7], ["HO", 5], ["ID", 3],
         ["IF", 5], ["IN", 2], ["IS", 2], ["IT", 2], ["JO", 9],
         ["KA", 6], ["KI", 6], ["LA", 2], ["LI", 2], ["LO", 2],
         ["MA", 4], ["ME", 4], ["MI", 4], ["MM", 6], ["MO", 4],
         ["MU", 4], ["MY", 7], ["NA", 2], ["NE", 2], ["NO", 2],
         ["NU", 2], ["OD", 3], ["OE", 2], ["OF", 5], ["OH", 5],
         ["OI", 2], ["OK", 6], ["OM", 4], ["ON", 2], ["OP", 4],
         ["OR", 2], ["OS", 2], ["OW", 5], ["OX", 9], ["OY", 5],
         ["PA", 4], ["PE", 4], ["PI", 4], ["PO", 4], ["QI", 11],
         ["RE", 2], ["SH", 5], ["SI", 2], ["SO", 2], ["TA", 2],
         ["TE", 2], ["TI", 2], ["TO", 2], ["UH", 5], ["UM", 4],
         ["UN", 2], ["UP", 4], ["US", 2], ["UT", 2], ["WE", 5],
         ["WO", 5], ["XI", 9], ["XU", 9], ["YA", 5], ["YE", 5],
         ["YO", 5], ["ZA", 11]]

# -------------------------------------------------------------------
# Function to search for a word in wordTable
# -------------------------------------------------------------------
def search_word(word):
    word = word.upper()  # Convert input to uppercase
    
    # Iterate through the word table to find the word
    for i in range(len(wordTable)):
        stored_word, points = wordTable[i]
        
        # If the stored word is found prints the word and its score
        if stored_word == word:
            print(f"{word} is valid and scores {points} points.")
            return
        
        # If passing the word then it will suggest the next closest word
        if stored_word > word:  # If we pass where the word should be
            print(f"{word} is not in the list. Did you mean {stored_word} ({points} points)?")
            return
    
    # If we reach the end and do not find the word, it will sugest the last word in thelist
    last_word, last_points = wordTable[-1]
    print(f"{word} is not in the list. The closest word is {last_word} ({last_points} points).")

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# Gets user input for user_input varable
user_input = input("Enter a two-letter word (AA to ZZ): ").strip()

# Function call for search word to check validity
search_word(user_input)


# In[ ]:


pip install dotenv


# In[ ]:




