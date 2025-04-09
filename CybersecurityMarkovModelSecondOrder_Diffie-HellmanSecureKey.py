#!/usr/bin/env python
# coding: utf-8

# In[ ]:


###############################################
#
# CybersecurityMarkovModelSecondOrder
#
# Name: Cody Thompson
# Project: Markov Model Second Order
# Date: April 9, 2025
# Description: 
# In a Markov model, we assume that:
# The future state depends only on a limited number of past states.
# First-order Markov model: Next state depends only on the current state.
# Second-order Markov model: Next state depends on the two previous states.
# Example text generation:
# Let’s say we want to predict the next word in a sentence using a 
# second-order Markov model. If our last two words were:

# "I am"
# A second-order model might tell us the next word has the following probabilities:

# happy: 0.6
# tired: 0.3
# leaving: 0.1
# These probabilities are learned from training on existing text.
###############################################

import random
from collections import defaultdict

class CyberSecurityMarkov:
    def __init__(self):
        # Initialize two default dicts to store the transitions and probabilities
        # 'transitions' stores how often each event follows a pair of previous events.
        # 'probabilities' stores the computed probabilities based on transition counts.
        self.transitions = defaultdict(lambda: defaultdict(int))  # (prev_event1, prev_event2) -> {next_event: count}
        self.probabilities = defaultdict(lambda: defaultdict(float))  # (prev_event1, prev_event2) -> {next_event: probability}

    def train(self, sequences):
        """Train the model with sequences of cybersecurity events."""
        for seq in sequences:  # Iterate through each sequence of events in the training data
            for i in range(len(seq) - 2):  # Go through the sequence in pairs of two events
                prev_event1, prev_event2, next_event = seq[i], seq[i+1], seq[i+2]
                # For every pair of previous events (prev_event1, prev_event2), record the occurrence of next_event
                self.transitions[(prev_event1, prev_event2)][next_event] += 1

        # After counting transitions, convert the counts to probabilities
        for prev_events, next_events in self.transitions.items():  # For each pair of previous events
            total = sum(next_events.values())  # Total number of transitions from this pair of events
            for event, count in next_events.items():
                # Calculate the probability of each event following the pair of previous events
                self.probabilities[prev_events][event] = count / total  # P(next_event | prev_event1, prev_event2)

    def generate(self, start_events, length=10):
        """Generate a sequence of cybersecurity events."""
        # Check if the provided starting events exist in the model's probabilities
        if start_events not in self.probabilities:
            raise ValueError("Unknown starting events!")  # Raise error if the start events are not found

        sequence = list(start_events)  # Initialize the sequence with the provided starting events

        # Generate a sequence of events with a length of 'length'
        for _ in range(length - 2):  # We already have two events in the sequence, so we generate the remaining
            prev_event1, prev_event2 = sequence[-2], sequence[-1]  # Get the last two events in the current sequence
            next_events = self.probabilities.get((prev_event1, prev_event2), None)  # Get possible next events

            if not next_events:
                break  # Stop generating if no known transition for this pair of events

            # Randomly choose the next event based on the probabilities of each possible next event
            next_event = random.choices(list(next_events.keys()), weights=next_events.values())[0]
            sequence.append(next_event)  # Add the selected next event to the sequence

        return sequence  # Return the generated sequence of events

# Example cybersecurity event logs (sequences of events)
training_data = [
    ["LOGIN_SUCCESS", "ACCESS_GRANTED", "LOGOUT"],  # A simple login access and logout
    ["LOGIN_SUCCESS", "ACCESS_GRANTED", "FILE_OPEN", "FILE_MODIFY", "LOGOUT"],  # Login, access granted, file opened, modified, then logout
    ["LOGIN_SUCCESS", "FAILED_ATTEMPT", "FAILED_ATTEMPT", "LOCKOUT"],  # A failed login attempt followed by lockout
    ["LOGIN_SUCCESS", "ACCESS_GRANTED", "MALWARE_DETECTED", "ISOLATION"],  # Access granted followed by malware detection and isolation
    ["LOGIN_SUCCESS", "ACCESS_GRANTED", "FILE_OPEN", "LOGOUT"],  # Simple login and file access followed by logout
]

# Initialize the CyberSecurityMarkov model and train it with the event sequences
security_markov = CyberSecurityMarkov()
security_markov.train(training_data)  # Train the model with the provided training data

# Generate a new sequence of events, starting with ("LOGIN_SUCCESS", "ACCESS_GRANTED")
generated_events = security_markov.generate(("LOGIN_SUCCESS", "ACCESS_GRANTED"), length=6)
print("Generated Security Event Sequence:", generated_events)  # Output the generated sequence


# In[ ]:


##########################################################
#
# Diffie-Hellman secure key exchange between two parties
# Without transmitting the actual key
# Diffie-Hellman is widely used in protocols like TLS/SSL 
# for securing communications over the internet (e.g., in HTTPS).
#
# It forms the basis for other more complex cryptographic protocols 
# such as ECDH (Elliptic Curve Diffie-Hellman), which uses elliptic 
# curve mathematics for better performance and security.
#
# Key Points:
# Security: The security of Diffie-Hellman relies on the discrete 
# logarithm problem, which is difficult to solve. Even if an attacker 
# intercepts the public values and the public keys, they cannot easily 
# compute the shared secret.
# 
# Vulnerability to Man-in-the-Middle (MitM) Attacks: Without additional 
# measures (like authentication), Diffie-Hellman is vulnerable to 
# Man-in-the-Middle (MitM) attacks. An attacker could intercept the public 
# keys and substitute their own, causing both parties to share a secret 
# with the attacker instead of each other.
#
##########################################################

import random

# Function to perform modular exponentiation (g^a mod p)
def mod_exp(base, exp, modulus):
    # This function calculates (base^exp) % modulus efficiently
    # Using Python's built-in pow function with three arguments, which performs modular exponentiation.
    return pow(base, exp, modulus)

# Diffie-Hellman Key Exchange
class DiffieHellman:
    def __init__(self, p, g):
        # Initialize with two public parameters:
        # p: A large prime number
        # g: A generator (primitive root modulo p)
        self.p = p  # Large prime number (public parameter)
        self.g = g  # Generator base (public parameter)

    def generate_private_key(self):
        # Generate a random private key, which is a secret number.
        # The private key is a number between 2 and p-2 (exclusive), where p is the large prime number.
        return random.randint(2, self.p - 2)

    def compute_public_key(self, private_key):
        # Compute the public key by calculating g^private_key mod p
        # The public key is shared openly, but only the corresponding private key can compute the shared secret.
        return mod_exp(self.g, private_key, self.p)

    def compute_shared_secret(self, private_key, other_public_key):
        # Compute the shared secret (key) using the other party's public key and your private key.
        # The shared secret is computed as (other_public_key^private_key) mod p.
        return mod_exp(other_public_key, private_key, self.p)

# Example usage
if __name__ == "__main__":
    # Step 1: Define public parameters
    p = 23  # A small prime number, used as the modulus
    g = 5   # A primitive root modulo p, used as the base for exponentiation

    # Step 2: Initialize DiffieHellman instances for two parties: Alice and Bob
    # These are two instances representing Alice and Bob in the key exchange process.
    alice = DiffieHellman(p, g)  # Alice will use the public parameters p and g
    bob = DiffieHellman(p, g)    # Bob will also use the same public parameters p and g

    # Step 3: Generate private keys for Alice and Bob
    # Each party generates a private key (random secret number). These private keys will never be shared.
    alice_private_key = alice.generate_private_key()
    bob_private_key = bob.generate_private_key()

    # Step 4: Compute public keys for Alice and Bob
    # Alice computes her public key using her private key and the public parameters p and g.
    # Bob computes his public key similarly.
    alice_public_key = alice.compute_public_key(alice_private_key)
    bob_public_key = bob.compute_public_key(bob_private_key)

    # Step 5: Exchange public keys and compute shared secret
    # Alice and Bob exchange their public keys (they can share these openly).
    # They then compute the shared secret using the other party's public key and their own private key.
    alice_shared_secret = alice.compute_shared_secret(alice_private_key, bob_public_key)
    bob_shared_secret = bob.compute_shared_secret(bob_private_key, alice_public_key)

    # Step 6: Verify that both shared secrets match
    # Since both Alice and Bob perform the same calculation using their respective private keys and the other's public key,
    # the resulting shared secret should be the same for both parties.
    print(f"Alice's Shared Secret: {alice_shared_secret}")
    print(f"Bob's Shared Secret: {bob_shared_secret}")

    # Check if both shared secrets match
    if alice_shared_secret == bob_shared_secret:
        print("Shared secrets match! Key exchange successful.")
    else:
        print("Shared secrets do not match.")


# In[ ]:




