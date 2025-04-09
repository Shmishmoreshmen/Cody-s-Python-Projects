#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#####################################
#
# DICE ROLLER GAME
#
# Name: Cody Thompson
# Project: Dice Roller Game
# Date: April 9, 2025
# Project Description:
# This game is a mennu driven program that will give the user
# options 1-7. Options 1-5 qill roll dice according to what menu option 
# the user selects. If the option is 1 then it will role a 4 sided dice.
# There are a totla of 5 dice to roll; 4-sided, 6-sided, 8-sided, 12-sided, and 
# a 20-sided dice. This program also saves the users dice rolls and displays them
# if the user selects option 6 from the menu.
#
#####################################

import random # Import the random module to generate random numbers

# Function to roll a dice with the specified number of sides
def roll_dice(sides):
    """Rolls a dice with the given number of sides."""
    return random.randint(1, sides) # returns random number from 1 to sides (user selected choice)

# Function to display the user's dice rolls
def display_rolls(rolls, name):
    """Display the stored dice rolls for the given user."""
    print(f"\n{name}'s Dice Rolls:")
    if not rolls:  # Check if there are any rolls
        print("No dice rolls recorded yet.")
    else:
        # used to iterate over each element (in this case, the dice rolls) in the rolls list.
        for i, roll in enumerate(rolls, start=1):
            # Prints the saved rolls in the stored value rolls list
            print(f"Roll {i}: {roll}.")

# Main function to run the dice roller program
def main():
    print("Welcome to the Dice Roller!")
    
    # Prompt the user for their name
    name = input("Please enter your name: ")

    rolls = []  # Initialize an empty list to store dice rolls

    while True:  # Infinite loop to keep the program running until the user quits
        # Display the menu of dice options
        print("\nSelect a dice to roll:")
        print("1. d4 (4-sided dice)")
        print("2. d6 (6-sided dice)")
        print("3. d8 (8-sided dice)")
        print("4. d12 (12-sided dice)")
        print("5. d20 (20-sided dice)")
        print("6. View my rolls")
        print("7. Quit")
        
        # Get the user's choice
        choice = input("\nEnter your choice (1-7): ")
        
        # Map menu choices to dice sides (Dictionary dice_map)
        dice_map = {
            "1": 4,   # Option 1 corresponds to a 4-sided dice (d4)
            "2": 6,   # Option 2 corresponds to a 6-sided dice (d6)
            "3": 8,   # Option 3 corresponds to an 8-sided dice (d8)
            "4": 12,  # Option 4 corresponds to a 12-sided dice (d12)
            "5": 20   # Option 5 corresponds to a 20-sided dice (d20)
        }
        
        if choice in dice_map:  # Check if the user's input is a valid choice (1-5)
            sides = dice_map[choice]  # Get the number of sides based on the user's choice
            result = roll_dice(sides)  # Roll the dice using the roll_dice function
            print(f"You rolled a {sides}-sided dice and got: {result}!")  # Display the result
            rolls.append(result)  # Store the roll result in the rolls list
        elif choice == "6":  # Option to view the user's rolls
            display_rolls(rolls, name)  # Display the stored rolls
        elif choice == "7":  # Option to quit the program
            print(f"Goodbye, {name}! Thanks for playing!")
            break  # Exit the loop and end the program
        else:  # Handle invalid input
            print("Invalid choice. Please select a valid option.")

# Ensure the program runs only when executed directly (not imported as a module)
if __name__ == "__main__":
    main()  # Start the program by calling the main function


# In[ ]:


#####################################
#
# TEXT BASED ADVENTURE GAME
#
# Name: Cody Thompson
# Project: Text Based Adventure Game
# Date: April 9, 2025
# Project Description:
# This text based adventure game has mainly text to decide where the user wishes to go 
# or what the user is currenlty seeing. This game is based upon the decisions of the user
# to decide where they should go or what they should do if something happens.
# this game has an invitory system. The game has a treasure room that will randomly decide
# what the user can see or pick up. The game also has a dragon room that handles the dragon
# attack portion. This game also has a inventory checker that makes sure you have the right
# items for the job and if you dont then the game becomes a bit hard to Succeeded at.
#####################################

import time  # Used to add delays for dramatic effect
import random  # Used to create random events
# TODO: future versions 
# Add puzzles that require solving to proceed 
# Introduce an NPC merchant to trade items 
# Implement a health system with multiple battles 
# maybe graphics for the game

# Player inventory to store collected items
inventory = []
# Function to display the intro of the game
def intro():
    # Introduction to the game where the player chooses to enter the cave or leave.
    print("Welcome to the Mysterious Cave Adventure!")
    time.sleep(1) # Delay execution for a given number of seconds.
    print("You find yourself at the entrance of a dark cave.")
    time.sleep(1) # Delay execution for a given number of seconds.    
    # Player choice: enter the cave or leave
    choice = input("Do you enter the cave? (yes/no): ").strip().lower()
    # the .strip().lower() removes leading and trailing whitespace 
    # (extra spaces, newlines, or tabs). Ensures the vlaue enterd is "yes" and not
    # " yes ".
    # Checking users choice 
    if choice == "yes":
        cave_entrance() # Function call for cave_entrance()
    elif choice == "no":
        print("You decide to walk away. Maybe another day...")
        time.sleep(1) # Delay execution for a given number of seconds.
        print("Game over!") # game ends if the user decides not to enter cave
    else:
        print("Invalid choice. Try again!") # User validation
        intro() # Function call intro() (game loop start)
# Function for cave entrance 
def cave_entrance():
    # The first area inside the cave where the player can collect a torch and a sword.
    print("\nYou step inside the cave, and it’s eerily quiet.")
    time.sleep(1) # Delay execution for a given number of seconds.
    print("You see a torch on the wall and a rusty sword on the ground.")    
    # Player chooses which items to take
    choice = input("Do you take something? (torch/sword/both/none): ").strip().lower()   
    # Checking users input for choice
    if "torch" in choice:
        inventory.append("torch") # Appending a item to the list variable inventory[]
        print("You grab the torch. It might be useful!")    
    # Checking users input for choice
    elif "sword" in choice:
        inventory.append("sword") # Appending a item to the list variable inventory[]
        print("You pick up the sword. Just in case...")   
    # Checking users input for choice
    elif "both" in choice:
        inventory.append("sword") # Appending a item to the list variable inventory[]
        inventory.append("torch") # appending a item to the list variable inventory[]
        print("You pick up both, just in case...")        
    elif "none" in choice:
        print("You decide to not grab anything")        
    time.sleep(1) # Delay execution for a given number of seconds.    
    # Player chooses which path to take
    print("\nThere are two paths ahead: Left and Right.")
    choice = input("Which way do you go? (left/right): ").strip().lower()   
    # Checking users input for choice
    if choice == "left":
        dragon_room() # Function call for dragon_room()
    # Checking users input for choice
    elif choice == "right":
        treasure_room() # Function call for treasure_room()
    # User validation
    else:
        print("Confused, you stand still. A bat startles you! Try again.")
        cave_entrance() # Function call for cave_entrance()
# Function for handling the dragon_room()
def dragon_room():
    # Room where the player encounters a sleeping dragon and must make a choice.
    print("\nYou enter a room and see a sleeping dragon!")
    time.sleep(1) # Delay execution for a given number of seconds.   
    if "sword" in inventory:
        print("You feel a little more confident with your sword.")
    # Available choices
    print("You can try to sneak past, fight the dragon, or look around.")    
    choice = input("What do you do? (sneak/fight/look): ").strip().lower()
    if choice == "sneak":
        # Random chance of success
        if random.randint(1, 2) == 1:
            print("\nYou tiptoe carefully...")
            time.sleep(2) # applies a sleep timer to make it feel more realistic
            print("The dragon snores loudly but doesn't wake up. You escape safely! You win!")
        else:
            print("\nYou step on a twig! The dragon wakes up!")
            dragon_attack() # function call for dragon_attack()   
    # Checks user choice for value that == "fight"
    elif choice == "fight":
        dragon_attack() # Function call for dragon_fight()    
    # Checks user choice for value that == "look"
    elif choice == "look":
        # Player finds a hidden shield
        print("\nYou quietly scan the room...")
        time.sleep(1) # Delay execution for a given number of seconds.
        print("You see a **magic shield** in the corner!")
        inventory.append("shield") # appending a item to the list variable inventory[]
        print("You take it and feel protected.")
        dragon_room() # Function call for dragon_room()  
    else:
        print("The dragon stirs as you hesitate! Try again!")
        dragon_room() # Function call for dragon_room()
# Function for dragon attacking
def dragon_attack():
    # Handles the dragon waking up and attacking the player.
    print("\nThe dragon opens its eyes and roars!")
    time.sleep(1) # applies a sleep timer to make it feel more realistic
    # checks the inventory[] to see if sword is there
    if "sword" in inventory:
        print("You grip your sword and prepare for battle!")
        # checks the inventory[] to see if shield is there (nested if statement)
        if "shield" in inventory:
            print("With your shield, you block the dragon’s fire and strike it down! You win!")
        else:
            print("You swing your sword, but the dragon burns you before you can land a hit. Game over!")
    # happens if there is no items in inventory[] to use against dragon
    else:
        print("You have no weapon! The dragon roasts you instantly. Game over!")
# Function used for the treasure room
def treasure_room():
    # Room containing a mysterious treasure chest with random outcomes.
    print("\nYou enter a glowing chamber filled with gold!")
    time.sleep(1) # applies a sleep timer to make it feel more realistic
    print("There is a giant golden chest in the middle.")   
    # Player chooses to open the chest or not
    choice = input("Do you open it? (yes/no): ").strip().lower()
    # User validation 
    if choice == "yes":
        random_event() # Function call for random_event()
    elif choice == "no":
        print("\nYou decide not to open the chest.")
        time.sleep(1) # Delay execution for a given number of seconds.
        print("Instead, you find a small hidden door leading to safety!")
        time.sleep(1) # Delay execution for a given number of seconds.
        print("You escape the cave victorious!")
    else:
        print("The cave trembles as you hesitate! Try again!")
        treasure_room() # Function call to treasure_room()
# Function to handle random events
def random_event():
    # Handles random outcomes when the player opens the treasure chest.
    print("\nYou slowly open the chest...")
    time.sleep(1) # Delay execution for a given number of seconds.   
    # Randomly selects an event
    event = random.choice(["gold", "trap", "monster", "magic"])
   # Checks to see if the random event chosen is gold
    if event == "gold":
        print("You find a pile of gold coins! You're rich!")
        print("You escape the cave victorious with your treasure!")   
    # Checks to see if the random event chosen is trap
    elif event == "trap":
        print("A cloud of poison gas fills the room!")
        if "torch" in inventory: 
            print("You wave your torch, clearing the air. You escape safely!")
        else:
            print("You choke on the gas and collapse. Game over!")  
    # Checks to see if the random event chosen is monster
    elif event == "monster":
        print("A ghostly figure rises from the chest!")
        if "sword" in inventory:
            print("You swing your sword and banish the ghost! You escape safely!")
        else:
            print("The ghost shrieks and drags you into the darkness. Game over!")   
    # Checks to see if the random event chosen is magic
    elif event == "magic":
        print("A glowing **magic amulet** appears inside!")
        inventory.append("amulet")
        print("You feel powerful! You leave the cave, ready for more adventures!")
# Start the game loop
intro()


# In[ ]:


#####################################
#
# SNAKE GAME
#
#
# Name: Cody Thompson
# Project: Snake Game
# Date: April 9, 2025
# Project Description:
# The idea beind this game is that the board will be created upon execution, then
# the user can select the difficulty from the menu that is presented to them at run time.
# Once a difficulty is selected then the game stats by having the snake move in a linear fashion
# then random red squares will appear that represent the food tokens. The user has to 
# move there snake using the arrow keys to pick p the food. Onced picked up the food token then
# turns into a segment of the snake thus extending the snakes body. Dont run into the walls on the
# sides or run into yourself as then the game will be over.
#####################################

# Import Modules
import pygame  # Import the pygame library for game development
import random  # Import random to generate random food positions

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 600, 400  # Set the dimensions of the game window
SQUARE_SIZE = 20  # Size of each block (for both the snake and food)
WHITE, GREEN, RED, BLACK = (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 0)  # Define color constants
FONT = pygame.font.Font(None, 36)  # Set font for Game Over message

# Create Game Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Initialize game window
pygame.display.set_caption("Snake Game")  # Set the title of the game window

# Function to display difficulty menu
def show_difficulty_menu():
    screen.fill(BLACK)  # Clear screen

    # Render difficulty options
    title_text = FONT.render("Select Difficulty:", True, WHITE)
    easy_text = FONT.render("E - Easy", True, WHITE)
    medium_text = FONT.render("M - Medium", True, WHITE)
    hard_text = FONT.render("H - Hard", True, WHITE)

    # Position text
    screen.blit(title_text, (WIDTH // 3, HEIGHT // 4))
    screen.blit(easy_text, (WIDTH // 3, HEIGHT // 3))
    screen.blit(medium_text, (WIDTH // 3, HEIGHT // 3 + 40))
    screen.blit(hard_text, (WIDTH // 3, HEIGHT // 3 + 80))
    
    pygame.display.update()  # Update screen

    # Wait for user input
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    return 5  # Easy FPS
                elif event.key == pygame.K_m:
                    return 10  # Medium FPS
                elif event.key == pygame.K_h:
                    return 15  # Hard FPS

# Get difficulty from user
FPS = show_difficulty_menu()

# Function to display Game Over screen and restart option
def show_game_over():
    screen.fill(BLACK)  # Clear the screen with black background
    game_over_text = FONT.render("Game Over! Play again? (Y/N)", True, WHITE)  # Create Game Over text
    screen.blit(game_over_text, (WIDTH // 6, HEIGHT // 3))  # Draw text on the screen
    pygame.display.update()  # Refresh the screen

    # Wait for user input to restart or quit
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the user closes the window, exit
                return False  # Exit game
            elif event.type == pygame.KEYDOWN:  # Check if a key is pressed
                if event.key == pygame.K_y:  # If 'Y' is pressed, restart
                    return True
                elif event.key == pygame.K_n:  # If 'N' is pressed, exit game
                    return False

# Function to reset the game state when restarting
def reset_game():
    return [(100, 100)], (SQUARE_SIZE, 0), (random.randrange(0, WIDTH, SQUARE_SIZE), random.randrange(0, HEIGHT, SQUARE_SIZE))

# Main game loop
while True:
    # Initialize game state
    snake, direction, food = reset_game()  # Reset snake position, direction, and food position
    clock = pygame.time.Clock()  # Create a clock object to control game speed
    running = True  # Variable to keep track of game state

    while running:
        screen.fill(BLACK)  # Clear the screen with black background

        # Handle user input (keyboard events)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the user closes the window, exit
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:  # If a key is pressed
                if event.key == pygame.K_UP and direction != (0, SQUARE_SIZE):
                    direction = (0, -SQUARE_SIZE)  # Move up
                elif event.key == pygame.K_DOWN and direction != (0, -SQUARE_SIZE):
                    direction = (0, SQUARE_SIZE)  # Move down
                elif event.key == pygame.K_LEFT and direction != (SQUARE_SIZE, 0):
                    direction = (-SQUARE_SIZE, 0)  # Move left
                elif event.key == pygame.K_RIGHT and direction != (-SQUARE_SIZE, 0):
                    direction = (SQUARE_SIZE, 0)  # Move right

        # Move the snake
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])  # Calculate new head position
        snake.insert(0, new_head)  # Insert new head at the front of the snake list

        # Check for collisions with itself or walls
        # new_head in snake[1:] checks if the new head position of the snake 
        # is already present in the snakes body (excluding the head since index [1:])
        # So if new_head exsists in snake[1:] it means the snake collided with
        # itself
        # new_head[0] < 0 or new_head[0] >= WIDTH
        # new_head[0] represents the x=coordinates of the snake's head
        # if its less than 0, the snake has hit the left wall
        # if its greater than or equal to WIDTH, the snake has hit the right wall
        # new_head[1] < 0 or new_head[1] >= HEIGHT
        # new_head[1] represents the y-coordinates of the snakes head.
        # if it is ess than 0, the snake had hit the top wall.
        # if it is greater than or equal to HEIGHT the snake has hit the bottom wall
        # The snake[1:] is list slicing in Python. it returns a new list that contains all elements
        # of snake
        if (new_head in snake[1:] or  # Collision with itself
                new_head[0] < 0 or new_head[0] >= WIDTH or  # Collision with left/right walls
                new_head[1] < 0 or new_head[1] >= HEIGHT):  # Collision with top/bottom walls
            running = False  # End game loop

        # Check if snake eats the food
        if new_head == food:
            # Generate new food at a random location within the grid
            food = (random.randrange(0, WIDTH, SQUARE_SIZE), random.randrange(0, HEIGHT, SQUARE_SIZE))
        else:
            # If food is not eaten, remove the last segment to maintain snake length
            snake.pop()

        # Draw the food on the screen
        pygame.draw.rect(screen, RED, (*food, SQUARE_SIZE, SQUARE_SIZE))

        # Draw the snake
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (*segment, SQUARE_SIZE, SQUARE_SIZE))

        pygame.display.update()  # Refresh the display
        clock.tick(FPS)  # Control game speed (frames per second)

    # Show "Game Over" screen and ask to restart
    if not show_game_over():
        break  # If user doesn't want to play again, exit the main loop

pygame.quit()  # Quit pygame properly when exiting the game
exit()  # Ensure the program fully exits


# In[ ]:


#####################################
#
# CENTIPEDE GAME (WORK IN PROGRESS)
#
# Name: Cody Thompson
# Project: Centipede game
# Date: April 9, 2025
# Project Description:
# This game is still a work in progress but the idea is that it will be somewhat 
# similar to the old arcade game centipede. In being that a centipede will 
# make its way down the screen in serpentine pattern. The user is not supposed to let the 
# cetipede get past them or if the centipede touches them they lose.
#
#####################################

from ursina import *
import random

# Initialize the game engine
app = Ursina()

# Game settings
window.color = color.black

# Player (Turret) Class
class Player(Entity):
    def __init__(self):
        super().__init__(
            model='cube', color=color.green, scale=(1, 1, 1), position=(0, -4, 0)
        )

    def update(self):
        self.x += held_keys['d'] * 0.1 - held_keys['a'] * 0.1  # Move left/right

    def shoot(self):
        Bullet(position=self.position)

# Bullet Class
class Bullet(Entity):
    def __init__(self, position):
        super().__init__(model='sphere', color=color.red, scale=0.3, position=position)
        self.speed = 0.2

    def update(self):
        self.y += self.speed
        if self.y > 5:
            destroy(self)  # Remove bullet when off-screen

# Centipede Segment Class
class CentipedeSegment(Entity):
    def __init__(self, position):
        super().__init__(model='cube', color=color.orange, scale=(1, 1, 1), position=position)
        self.direction = 0.1  # Movement direction

    def update(self):
        self.x += self.direction
        
        # Change direction when hitting boundary
        if self.x > 4 or self.x < -4:
            self.direction *= -1
            self.y -= 1  # Move down

        # Check collision with bullets
        for bullet in scene.entities:
            if isinstance(bullet, Bullet) and self.intersects(bullet).hit:
                destroy(self)
                destroy(bullet)
                break

# Centipede Class
class Centipede():
    def __init__(self):
        self.segments = [CentipedeSegment(position=(x, 3, 0)) for x in range(-3, 4)]

# Instantiate player and centipede
player = Player()
centipede = Centipede()

# Input Handling
def input(key):
    if key == 'space':
        player.shoot()

# Run the game
app.run()


# In[ ]:


#####################################
#
# BATTLESHIP GAME (WORK IN PROGRESS)
#
# Name: Cody Thompson
# Project: Battlteship
# Date: April 9, 2025
# Project Description:
# This game is still a work in progress. But the games idea is built around the classic
# boad game Battleship. This will allow the user to place there ships randomly on a grid.
# the enemy you will take turn guessing where the ships are from a series of turn based 
# guesses that invold firing at certain grid coordinates. If the coordinates match up with
# a ships location then the ship is hit and you have gained insight on the ships location
# and gained a point in doing so.
#####################################

import random

def create_board(size):
    return [['~' for _ in range(size)] for _ in range(size)]

def print_board(board, reveal=False):
    print("  " + " ".join(str(i) for i in range(len(board))))
    for i, row in enumerate(board):
        print(str(i) + " " + " ".join(row))

def place_ships(board, num_ships):
    size = len(board)
    ships = []
    while len(ships) < num_ships:
        x, y = random.randint(0, size - 1), random.randint(0, size - 1)
        if (x, y) not in ships:
            ships.append((x, y))
            board[x][y] = 'S'  # Mark ships (hidden)
    return ships

def get_player_guess():
    while True:
        try:
            x, y = map(int, input("Enter row and column (e.g., 1 2): ").split())
            return x, y
        except ValueError:
            print("Invalid input. Enter two numbers separated by space.")

def play_battleship():
    size = 5  # Grid size
    num_ships = 3  # Number of ships
    board = create_board(size)
    ships = place_ships(board, num_ships)
    guesses = []
    hits = 0
    max_attempts = size * 2
    
    print("Welcome to Battleship!")
    print_board(board)
    
    while hits < num_ships and len(guesses) < max_attempts:
        print("\nYour turn!")
        x, y = get_player_guess()
        
        if (x, y) in guesses:
            print("You already guessed that spot!")
            continue
        
        guesses.append((x, y))
        
        if (x, y) in ships:
            print("Hit!")
            board[x][y] = 'X'
            hits += 1
        else:
            print("Miss!")
            board[x][y] = 'O'
        
        print_board(board)
    
    if hits == num_ships:
        print("Congratulations! You sunk all the ships!")
    else:
        print("Game over! You ran out of attempts.")
        print("The ships were at:", ships)
        
# Run the game
if __name__ == "__main__":
    play_battleship()


# In[ ]:


#####################################
#
# SNAKE GAME (UPDATED VERSION)
#
#
# Name: Cody Thompson
# Project: Snake Game
# Date: April 9, 2025
# Project Description:
# The idea beind this game is that the board will be created upon execution, then
# the user can select the difficulty from the menu that is presented to them at run time.
# Once a difficulty is selected then the game stats by having the snake move in a linear fashion
# then random red squares will appear that represent the food tokens. The user has to 
# move there snake using the arrow keys to pick p the food. Onced picked up the food token then
# turns into a segment of the snake thus extending the snakes body. Dont run into the walls on the
# sides or run into yourself as then the game will be over.
# UPDATES:
# added in a section that saves highscores to a file that is then read to output the highscores
# Added in a way to continue playing if game over is acheived.
#####################################

# Import Modules
import pygame  # Import pygame library for game development
import random  # Import random library for generating random food positions

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 600, 400  # Screen dimensions (width and height of the game window)
SQUARE_SIZE = 20  # Size of each snake segment and the food

# Define Colors (RGB format)
WHITE = (255, 255, 255)  # Text color
GREEN = (0, 255, 0)  # Snake color
RED = (255, 0, 0)  # Food color
BLACK = (0, 0, 0)  # Background color

# Font for displaying text on the screen
FONT = pygame.font.Font(None, 36)

# Create Game Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Set up the game window
pygame.display.set_caption("Snake Game")  # Set the title of the window


# Function: Load High Score from File
def load_high_score():
    """Reads the high score from a file. If the file does not exist, returns 0."""
    try:
        with open("highscore.txt", "r") as f:
            return int(f.read().strip())  # Read and return high score from file
    except (FileNotFoundError, ValueError):  # Handle missing or invalid file
        return 0  # Default high score is 0


# Function: Save High Score to File
def save_high_score(score):
    """Saves the high score to a file."""
    with open("highscore.txt", "w") as f:
        f.write(str(score))  # Write the new high score to the file


# Load the high score when the game starts
high_score = load_high_score()


# Function: Show Difficulty Selection Menu
def show_difficulty_menu():
    """Displays the difficulty selection screen and waits for the player to choose."""
    screen.fill(BLACK)  # Clear the screen with black color

    # Render and display text for difficulty options
    screen.blit(FONT.render("Select Difficulty:", True, WHITE), (WIDTH // 3, HEIGHT // 4))
    screen.blit(FONT.render("E - Easy", True, WHITE), (WIDTH // 3, HEIGHT // 3))
    screen.blit(FONT.render("M - Medium", True, WHITE), (WIDTH // 3, HEIGHT // 3 + 40))
    screen.blit(FONT.render("H - Hard", True, WHITE), (WIDTH // 3, HEIGHT // 3 + 80))

    pygame.display.update()  # Update the screen

    # Wait for the player to press a key
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the user closes the window, exit
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:  # Easy mode
                    return 5
                elif event.key == pygame.K_m:  # Medium mode
                    return 10
                elif event.key == pygame.K_h:  # Hard mode
                    return 15


# Set game speed based on selected difficulty
FPS = show_difficulty_menu()


# Function: Show Game Over Screen
def show_game_over(score):
    """Displays the game over screen and allows the player to restart or exit."""
    global high_score

    # Update high score if the player's score is higher
    if score > high_score:
        high_score = score
        save_high_score(high_score)  # Save new high score to file

    screen.fill(BLACK)  # Clear the screen

    # Display the game over message, score, and high score
    screen.blit(FONT.render(f"Game Over! Score: {score}", True, WHITE), (WIDTH // 6, HEIGHT // 3))
    screen.blit(FONT.render(f"High Score: {high_score}", True, WHITE), (WIDTH // 6, HEIGHT // 3 + 40))
    screen.blit(FONT.render("Play again? (Y/N)", True, WHITE), (WIDTH // 6, HEIGHT // 3 + 80))

    pygame.display.update()  # Update the screen

    # Wait for player input (Y to restart, N to exit)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False  # Exit game
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    return True  # Restart game
                elif event.key == pygame.K_n:
                    return False  # Exit game


# Function: Reset Game State
def reset_game():
    """Initializes the snake, its direction, and the food position."""
    snake = [(100, 100)]  # Snake starts at position (100, 100)
    direction = (SQUARE_SIZE, 0)  # Initial movement to the right
    food = (random.randrange(0, WIDTH, SQUARE_SIZE), random.randrange(0, HEIGHT, SQUARE_SIZE))  # Random food position
    return snake, direction, food


# Main Game Loop
while True:
    snake, direction, food = reset_game()  # Initialize game state
    clock = pygame.time.Clock()  # Create game clock
    running = True  # Game loop control variable
    score = 0  # Initialize score

    while running:
        screen.fill(BLACK)  # Clear screen to black

        # Handle player input (keyboard controls)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the user closes the window, exit
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                # Change movement direction based on arrow key input
                if event.key == pygame.K_UP and direction != (0, SQUARE_SIZE):
                    direction = (0, -SQUARE_SIZE)
                elif event.key == pygame.K_DOWN and direction != (0, -SQUARE_SIZE):
                    direction = (0, SQUARE_SIZE)
                elif event.key == pygame.K_LEFT and direction != (SQUARE_SIZE, 0):
                    direction = (-SQUARE_SIZE, 0)
                elif event.key == pygame.K_RIGHT and direction != (-SQUARE_SIZE, 0):
                    direction = (SQUARE_SIZE, 0)

        # Move the snake by inserting a new head at the front
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake.insert(0, new_head)  # Add the new head to the snake

        # Check for collisions (wall or itself)
        if (new_head in snake[1:] or
            new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT):
            running = False  # End game if collision occurs

        # Check if the snake eats the food
        if new_head == food:
            food = (random.randrange(0, WIDTH, SQUARE_SIZE), random.randrange(0, HEIGHT, SQUARE_SIZE))  # Generate new food position
            score += 10  # Increase score
        else:
            snake.pop()  # Remove the last segment to maintain the length

        # Draw food
        pygame.draw.rect(screen, RED, (*food, SQUARE_SIZE, SQUARE_SIZE))

        # Draw snake
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (*segment, SQUARE_SIZE, SQUARE_SIZE))

        # Display current score and high score
        score_text = FONT.render(f"Score: {score}  High Score: {high_score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.update()  # Refresh the screen
        clock.tick(FPS)  # Control the game speed

    # Show game over screen and check if player wants to restart
    if not show_game_over(score):
        break  # Exit game if player chooses not to restart

# Quit game
pygame.quit()
exit()


# In[ ]:


##########################################################################
#
# HANGMAN GAME
#
#
# Name: Cody Thompson
# Project: Hangman game
# Date: April 9, 2025
# Project Description:
# This game repesents the classic hangman game that ahs theh user guess letters
# intill all correct letters are guessed to spell out a word. If all guesses are wrong
# then the game ends. If a guess is wrong then the board will progress filling in 
# the hanged man
##########################################################################

import random  # Import the random module to select a random word

# List of words to choose from
words = ["python", "loops", "programming", "developer", "hangman", "challenge", "computer", "keyboard"]

# Function to display the Hangman stages
def display_hangman(attempts):
    """Returns the ASCII representation of the Hangman based on remaining attempts."""
    stages = [
        """  # Stage 0 (Full Hangman)
           ------
           |    |
           |    O
           |   \\|/
           |    |
           |   / \\
          ---
        """,
        """  # Stage 1 (One leg removed)
           ------
           |    |
           |    O
           |   \\|/
           |    |
           |   / 
          ---
        """,
        """  # Stage 2 (Both legs removed)
           ------
           |    |
           |    O
           |   \\|/
           |    |
           |    
          ---
        """,
        """  # Stage 3 (One arm removed)
           ------
           |    |
           |    O
           |   \\|
           |    |
           |    
          ---
        """,
        """  # Stage 4 (Arms removed)
           ------
           |    |
           |    O
           |    |
           |    |
           |    
          ---
        """,
        """  # Stage 5 (Only the head remains)
           ------
           |    |
           |    O
           |    
           |    
           |    
          ---
        """,
        """  # Stage 6 (Starting point, empty gallows)
           ------
           |    |
           |    
           |    
           |    
           |    
          ---
        """
    ]
    # If attempt is 0 then the stage 6 board will populate.
    # if the attempt is 1 with a failed guess then stage 5 will populate.
    return stages[attempts]

# Function to play the game
def play_hangman():
    """Main function to play the Hangman game."""
    word = random.choice(words)  # Select a random word from the list
    guessed_letters = set()  # Keep track of guessed letters
    word_letters = set(word)  # Letters in the selected word
    attempts = 6  # Maximum number of incorrect guesses allowed
    guessed_word = ["_"] * len(word)  # Display word as underscores initially

    print("Welcome to Hangman!")  # Start game message
    
    while attempts > 0 and "_" in guessed_word:  # Continue until no more attempts or word is guessed
        print(display_hangman(attempts))  # Show hangman progress
        print("\nWord:", " ".join(guessed_word))  # Display current word progress
        print(f"Incorrect guesses left: {attempts}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

        guess = input("\nGuess a letter: ").lower()  # Ask player for a letter input

        # Input validation: check if the input is a single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.\n")
            continue  # Restart loop to ask for a valid input
        
        # Check if the letter was already guessed
        if guess in guessed_letters:
            print("You already guessed that letter! Try another.\n")
            continue  # Restart loop to avoid duplicate guesses

        guessed_letters.add(guess)  # Add the guessed letter to the set

        # Check if the guessed letter is in the word
        if guess in word_letters:
            print("Good guess!\n")
            for i, letter in enumerate(word):  # Loop through each letter in the word
                if letter == guess:
                    guessed_word[i] = letter  # Reveal the correctly guessed letter in the word
        else:
            print("Wrong guess!\n")
            attempts -= 1  # Reduce attempts for an incorrect guess

    # Game over message: Check if the player won or lost
    if "_" not in guessed_word:
        print("Congratulations! You guessed the word:", word)  # Winning message
    else:
        print(display_hangman(attempts))  # Show final Hangman stage
        print("You lost! The word was:", word)  # Losing message

# Run the game if this file is executed directly
if __name__ == "__main__":
    play_hangman()


# In[ ]:


##########################################################################
#
# CHESS GAME
#
# Name: Cody Thompson
# Project: Chess Game
# Date: April 9, 2025
# Project Description:
# this game creates a board that has two sides, the capatal letters and the 
# lower case letters. The upper case letters represents the Black Pieces and
# the lower case letters represent the White Pieces. The voard is seperated 
# in a checkered layout that has green and white spaces. The user has to 
# click the peice they want to move then click again to where they want to move
# said piece.
#
# NOTE: this game is ment to played with two people
##########################################################################

# Import Modules
import pygame  # Import Pygame for GUI rendering
import chess   # Import python-chess for handling game logic

# Initialize pygame
pygame.init()

# Constants for the chessboard dimensions and colors
WIDTH, HEIGHT = 640, 640  # Chessboard window size in pixels
SQUARE_SIZE = WIDTH // 8  # Size of each square (since board is 8x8)
WHITE = (238, 238, 210)   # Light square color
BLACK = (118, 150, 86)    # Dark square color

# Set up game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Create display window
pygame.display.set_caption("Chess Game")  # Set window title
board = chess.Board()  # Create a new chess board using python-chess

# Dictionary to map chess piece symbols to text representation
piece_letters = {
    'p': 'p', 'r': 'r', 'n': 'n', 'b': 'b', 'q': 'Q', 'k': 'K',  # Black pieces
    'P': 'P', 'R': 'R', 'N': 'N', 'B': 'B', 'Q': 'Q', 'K': 'K'   # White pieces
}

# Initialize font for drawing text-based chess pieces
pygame.font.init()
font = pygame.font.Font(None, 60)  # Set default font with size 60

# Variable to store the currently selected square (None if no selection)
selected_square = None

# Clock to control frame rate
clock = pygame.time.Clock()  

def draw_board():
    """Draws the chessboard by alternating WHITE and BLACK squares."""
    for row in range(8):  # Loop through rows (0 to 7)
        for col in range(8):  # Loop through columns (0 to 7)
            color = WHITE if (row + col) % 2 == 0 else BLACK  # Determine square color
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces():
    """Draws chess pieces as text characters instead of images."""
    for square in chess.SQUARES:  # Loop through all board squares (0-63)
        piece = board.piece_at(square)  # Get piece at current square
        if piece:
            row, col = divmod(square, 8)  # Convert square index to row and column
            text = font.render(piece_letters[piece.symbol()], True, (0, 0, 0))  # Render piece as black text
            text_rect = text.get_rect(center=(col * SQUARE_SIZE + SQUARE_SIZE // 2, 
                                              row * SQUARE_SIZE + SQUARE_SIZE // 2))  # Center text in square
            screen.blit(text, text_rect)  # Draw piece text onto the board

def get_square_under_mouse(pos):
    """Returns the chessboard square index based on the given mouse position."""
    x, y = pos  # Get mouse x and y coordinates
    col, row = x // SQUARE_SIZE, y // SQUARE_SIZE  # Convert pixel position to board coordinates
    return chess.square(col, row)  # Convert coordinates to chess square index (0-63)

# Draw the initial chessboard and pieces once before the game loop starts
draw_board()
draw_pieces()
pygame.display.update()  # Update the display

# Main game loop
running = True
while running:
    clock.tick(30)  # Limit frame rate to 30 FPS to prevent excessive CPU usage

    # Handle events (user inputs)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If the user clicks the close button
            running = False  # Exit the game loop

        if event.type == pygame.MOUSEBUTTONDOWN:  # If the user clicks a square
            square = get_square_under_mouse(event.pos)  # Get the clicked square index
            
            if selected_square is None:  # If no piece is selected yet
                if board.piece_at(square):  # If there's a piece on the clicked square
                    selected_square = square  # Select the piece
            else:
                # Attempt to move the selected piece to the clicked square
                move = chess.Move(selected_square, square)  # Create a move object
                if move in board.legal_moves:  # Check if the move is legal
                    board.push(move)  # Execute the move
                    
                    # Redraw board only after a valid move
                    draw_board()  
                    draw_pieces()
                    pygame.display.update()  # Refresh the display
                
                selected_square = None  # Reset selection after move

# Quit pygame when loop ends
pygame.quit()


# In[ ]:


#############################################################
#
# TOWER DEFENSE GAME(work in progress)
#
# Name: Cody Thompson
# Project: Tower Defence game
# Date: April 9, 2025
# Project Description:
# This game works by first populating a screen for the games run. Then,
# giving the user some option choose from in being the towers they wish to place.
# Once the first tower is placed then the game starts. When an enemy is killed the user
# gets points based upon how much that specified enemy is worth utilizing a dictionary to
# assign there values. If the enemy reaches the home base then the home base is decremented
# by 1. If the home base health reaches zero then the game ends.
#############################################################

# Imports
import pygame
import sys
import math
import random

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 600  # Screen dimensions
WHITE, GREEN, RED, BLUE, BLACK = (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 255), (0, 0, 0)  # Colors

# Create Game Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Defense Game")
clock = pygame.time.Clock()

# Enemy Path (List of waypoints for enemy movement)
PATH = [(50, 50), (200, 50), (200, 200), (400, 200), (400, 400), (600, 400), (600, 550)]
HOME_BASE_POS = PATH[-1]
home_base_health = 20

# Game Variables
#global points  # Player points used to purchase towers
points = 25
#point_total
wave = 1  # Track current wave
game_started = False  # Flag to check if the game has started
selected_tower = "rect"  # Default tower type
towers = []  # List of towers placed by the player

# Enemy Types
enemy_types = ["square", "circle", "cross"]
enemy_health = {"square": 15, "circle": 10, "cross": 20}
enemy_value = {"square": 2, "circle": 3, "cross": 4}

# List to store active enemies
enemies = []

# Function to display wave number and remaining enemies
def draw_wave_info():
    """Displays the wave number and remaining enemies on the screen."""
    font = pygame.font.Font(None, 36)
    wave_text = font.render(f"Wave: {wave}", True, BLACK)
    enemies_text = font.render(f"Enemies Left: {len(enemies)}", True, BLACK)
    
    # Display wave number and remaining enemies at the top left
    screen.blit(wave_text, (10, 10))
    screen.blit(enemies_text, (10, 40))
    
def draw_ui():
    """Draws the UI for selecting towers."""
    font = pygame.font.Font(None, 36)
    text1 = font.render("Press 1 for Rect Tower ($5, 10 DMG)", True, BLACK)
    text2 = font.render("Press 2 for Triangle Tower ($15, 15 DMG)", True, BLACK)
    text3 = font.render("Press 3 for T Tower ($50, 100 DMG)", True, BLACK)
    screen.blit(text1, (10, HEIGHT - 90))
    screen.blit(text2, (10, HEIGHT - 60))
    screen.blit(text3, (10, HEIGHT - 30))

def draw_path():
    """Draw the path of the enemies for visual reference."""
    for i in range(len(PATH) - 1):
        pygame.draw.line(screen, RED, PATH[i], PATH[i+1], 5)

def is_on_path(x, y):
    """Check if the point (x, y) is on the enemy path."""
    for i in range(len(PATH) - 1):
        p1, p2 = PATH[i], PATH[i + 1]
        if (p2[1] - p1[1]) * (x - p1[0]) == (y - p1[1]) * (p2[0] - p1[0]):
            if min(p1[0], p2[0]) <= x <= max(p1[0], p2[0]) and min(p1[1], p2[1]) <= y <= max(p1[1], p2[1]):
                return True
    return False

# Draws the home base
def draw_home_base():
    """Draws the home base at the end of the path."""
    pygame.draw.rect(screen, BLUE, (HOME_BASE_POS[0] - 20, HOME_BASE_POS[1] - 20, 40, 40))
    
# Displayes the points on the screen
def draw_points():
    """Displays the player's points on the screen."""
    font = pygame.font.Font(None, 36)
    points_text = font.render(f"Points: {points}", True, BLACK)
    screen.blit(points_text, (WIDTH - 150, 10))  # Display in top-right corner

# Updated Enemy class: Remove enemy and update count
class Enemy:
    def __init__(self, shape, health, value):
        self.x, self.y = PATH[0]  # Start at first waypoint
        self.speed = 2  # Movement speed
        self.path_index = 0  # Track progress along path
        self.health = health  # Enemy health
        self.alive = True  # Status flag
        self.shape = shape  # Shape of enemy
        self.value = value  # Points rewarded when defeated
        self.reached_base = False  # Flag to track if the enemy has reached the base

    def move(self):
        """Move the enemy along the predefined path."""
        global home_base_health
        
        if self.path_index < len(PATH) - 1:
            target_x, target_y = PATH[self.path_index + 1]
            dx, dy = target_x - self.x, target_y - self.y
            dist = math.sqrt(dx**2 + dy**2)
            
            if dist < self.speed:
                self.path_index += 1  # Move to next waypoint
            else:
                self.x += self.speed * (dx / dist)  # Move proportionally in x
                self.y += self.speed * (dy / dist)  # Move proportionally in y
        else:
            if not self.reached_base:
                # Enemy reached home base
                home_base_health-= 1 #= home_base_health - 1
                self.reached_base = True
                print(f"Home base hit! Health: {home_base_health}")
            
            enemies.remove(self)  # Remove enemy from the game

    def draw(self):
        """Draw the enemy in the appropriate shape."""
        if self.shape == "square":
            pygame.draw.rect(screen, RED, (self.x - 15, self.y - 15, 30, 30))
        elif self.shape == "circle":
            pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), 15)
        elif self.shape == "cross":
            pygame.draw.line(screen, RED, (self.x - 15, self.y - 15), (self.x + 15, self.y + 15), 3)
            pygame.draw.line(screen, RED, (self.x - 15, self.y + 15), (self.x + 15, self.y - 15), 3)
        pygame.draw.rect(screen, RED, (self.x - 20, self.y - 30, 40, 5))  # Health bar
        pygame.draw.rect(screen, GREEN, (self.x - 20, self.y - 30, 40 * (self.health / enemy_health[self.shape]), 5))

class Tower:
    def __init__(self, x, y, damage, cost, shape):
        self.x, self.y = x, y  # Tower position
        self.range = 100  # Attack range
        self.reload_time = 30  # Cooldown before next shot
        self.reload_counter = 1.5  # Countdown timer
        self.damage = damage  # Damage per shot
        self.cost = cost  # Cost of the tower
        self.shape = shape  # Shape of the tower

    def draw(self):
        """Draw a tower based on its shape."""
        if self.shape == "rect":
            pygame.draw.rect(screen, BLACK, (self.x - 20, self.y - 20, 40, 40))
        elif self.shape == "triangle":
            pygame.draw.polygon(screen, BLACK, [(self.x, self.y - 20), (self.x - 20, self.y + 20), (self.x + 20, self.y + 20)])
        elif self.shape == "T":
            pygame.draw.rect(screen, BLACK, (self.x - 30, self.y - 10, 60, 20))
            pygame.draw.rect(screen, BLACK, (self.x - 10, self.y - 30, 20, 30))
            
    def attack(self, enemies):
        """Attack the nearest enemy within range if reload is ready."""
        global points
        
        if self.reload_counter > 0:
            self.reload_counter -= 1
            return  # Tower is still reloading

        target = None
        min_dist = self.range

        # Find the closest enemy in range
        for enemy in enemies:
            dist = math.sqrt((enemy.x - self.x) ** 2 + (enemy.y - self.y) ** 2)
            if dist <= self.range and (target is None or dist < min_dist):
                target = enemy
                min_dist = dist

        if target:
            target.health -= self.damage  # Apply damage
            
            # TESTING HERE
            #print(f"Before: {target.shape} HP = {target.health}")
            #print(f"After: {target.shape} HP = {target.health}")
            #print(f"Tower at ({self.x}, {self.y}) attacks {target.shape} at ({target.x}, {target.y}) for {self.damage} damage")
            #target.health -= self.damage  # Apply damage

            # Draw a line to visualize the attack
            pygame.draw.line(screen, BLACK, (self.x, self.y), (target.x, target.y), 2)
            
            if target.health <= 0:
                points += target.value
                enemies.remove(target)
                return
            
            self.reload_counter = self.reload_time  # Reset reload timer

def spawn_enemy():
    """Spawn enemies based on the wave number."""
    # enemy_shape = enemy_types[wave % len(enemy_types)]
    enemy_shape = enemy_types[wave % len(enemy_types)]  # Cycle through enemy types
    enemy_health_value = enemy_health[enemy_shape]
    enemy_value_value = enemy_value[enemy_shape]
    
    # Increase the number of enemies with each wave
    num_enemies = wave * 2  # Example: 2 enemies per wave, increases with wave number
    
    for _ in range(num_enemies):
        enemy_shape = enemy_types[wave % len(enemy_types)]
        enemy_health_value = enemy_health[enemy_shape]  # Get correct health
        enemy_value_value = enemy_value[enemy_shape]    # Get correct value
        enemies.append(Enemy(enemy_shape, enemy_health_value, enemy_value_value))

# Run Game
running = True
while running:
    screen.fill(WHITE)
    draw_ui()
    draw_path()
    draw_home_base()
    draw_wave_info()
    
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                selected_tower = "rect"
            elif event.key == pygame.K_2:
                selected_tower = "triangle"
            elif event.key == pygame.K_3:
                selected_tower = "T"
        elif event.type == pygame.MOUSEBUTTONDOWN and selected_tower:
            
            # Get mouse position
            x, y = pygame.mouse.get_pos()
            
            # If not on the path, place tower
            if not is_on_path(x, y):
                if selected_tower == "rect" and points >= 5:
                    towers.append(Tower(x, y, 20, 5, "rect"))
                    points -= 5
                elif selected_tower == "triangle" and points >= 15:
                    towers.append(Tower(x, y, 30, 15, "triangle"))
                    points -= 15
                elif selected_tower == "T" and points >= 50:
                    towers.append(Tower(x, y, 100, 50, "T"))
                    points -= 50
    
    # Start game once initial towers are placed
    if len(towers) > 0 and not game_started:
        game_started = True
        spawn_enemy()  # Spawn the first wave of enemies
    
    if game_started:
        #dead_enemies = []
        # Move and draw enemies
        for enemy in list(enemies):
            enemy.draw()
            enemy.move()
            
            # Remove enemy if health drops to zero
            if enemy.health <= 0:
                #points += enemy.value  # Reward player with points
                enemies.remove(enemy)
                #dead_enemies.append(enemy)  # Tracks the enemies to remove
                #pygame.display.update()
                
        # Remove dead enemies after iteration
        for enemy in dead_enemies:
            enemies.remove(enemy)
    
    # Game Over condition
    if home_base_health <= 0:
        print("Game Over! The home base has been destroyed.")
        running = False # End the game loop
    
    # Check if all enemies are gone, start the next wave
    if game_started and not enemies:  # If no enemies remain, spawn the next wave
        wave += 1
        spawn_enemy()

    # Draw all towers
    for tower in towers:
        tower.draw() # Draws the towers
        tower.attack(enemies)  # Make towers attack enemies
    
    draw_points()
    pygame.display.update() # Update the game window
    clock.tick(60) # Game speed (FPS)

pygame.quit() # Quit's the pygame (GUI window)
sys.exit() # ensures the prgram closes properly


# In[ ]:


#############################################################
#
# TOWER DEFENSE GAME
#
#############################################################

# Imports
import pygame
import sys
import math
import random

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 600  # Screen dimensions
WHITE, GREEN, RED, BLUE, BLACK = (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 255), (0, 0, 0)  # Colors

# Create Game Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Defense Game")
clock = pygame.time.Clock()

# Enemy Path (List of waypoints for enemy movement)
PATH = [(50, 50), (200, 50), (200, 200), (400, 200), (400, 400), (600, 400), (600, 550)]
HOME_BASE_POS = PATH[-1]
home_base_health = 20

# Game Variables
#global points  # Player points used to purchase towers
points = 25
#point_total
wave = 1  # Track current wave
game_started = False  # Flag to check if the game has started
selected_tower = "rect"  # Default tower type
towers = []  # List of towers placed by the player

# Enemy Types
enemy_types = ["square", "circle", "cross"]
enemy_health = {"square": 15, "circle": 10, "cross": 20}
enemy_value = {"square": 2, "circle": 3, "cross": 4}

enemy_spawn_timer = 0  # Timer to control enemy spawn interval
enemy_spawn_delay = 60  # Delay (frames) between enemy spawns (1 second if 60 FPS)
enemies_spawned_this_wave = 0  # Track how many enemies have spawned this wave

# List to store active enemies
enemies = []

# Function to display wave number and remaining enemies
def draw_wave_info():
    """Displays the wave number and remaining enemies on the screen."""
    font = pygame.font.Font(None, 36)
    wave_text = font.render(f"Wave: {wave}", True, BLACK)
    enemies_text = font.render(f"Enemies Left: {len(enemies)}", True, BLACK)
    
    # Display wave number and remaining enemies at the top left
    screen.blit(wave_text, (10, 10))
    screen.blit(enemies_text, (10, 40))
    
def draw_ui():
    """Draws the UI for selecting towers."""
    font = pygame.font.Font(None, 36)
    text1 = font.render("Press 1 for Rect Tower ($5, 10 DMG)", True, BLACK)
    text2 = font.render("Press 2 for Triangle Tower ($15, 15 DMG)", True, BLACK)
    text3 = font.render("Press 3 for T Tower ($50, 100 DMG)", True, BLACK)
    screen.blit(text1, (10, HEIGHT - 90))
    screen.blit(text2, (10, HEIGHT - 60))
    screen.blit(text3, (10, HEIGHT - 30))

def draw_path():
    """Draw the path of the enemies for visual reference."""
    for i in range(len(PATH) - 1):
        pygame.draw.line(screen, RED, PATH[i], PATH[i+1], 5)

def is_on_path(x, y):
    """Check if the point (x, y) is on the enemy path."""
    for i in range(len(PATH) - 1):
        p1, p2 = PATH[i], PATH[i + 1]
        if (p2[1] - p1[1]) * (x - p1[0]) == (y - p1[1]) * (p2[0] - p1[0]):
            if min(p1[0], p2[0]) <= x <= max(p1[0], p2[0]) and min(p1[1], p2[1]) <= y <= max(p1[1], p2[1]):
                return True
    return False

# Draws the home base
def draw_home_base():
    """Draws the home base at the end of the path."""
    pygame.draw.rect(screen, BLUE, (HOME_BASE_POS[0] - 20, HOME_BASE_POS[1] - 20, 40, 40))
    
# Displayes the points on the screen
def draw_points():
    """Displays the player's points on the screen."""
    font = pygame.font.Font(None, 36)
    points_text = font.render(f"Points: {points}", True, BLACK)
    screen.blit(points_text, (WIDTH - 150, 10))  # Display in top-right corner

# Updated Enemy class: Remove enemy and update count
class Enemy:
    def __init__(self, shape, health, value):
        self.x, self.y = PATH[0]  # Start at first waypoint
        self.speed = 2  # Movement speed
        self.path_index = 0  # Track progress along path
        self.health = health  # Enemy health
        self.alive = True  # Status flag
        self.shape = shape  # Shape of enemy
        self.value = value  # Points rewarded when defeated
        self.reached_base = False  # Flag to track if the enemy has reached the base

    def move(self):
        """Move the enemy along the predefined path."""
        global home_base_health
        
        if self.path_index < len(PATH) - 1:
            target_x, target_y = PATH[self.path_index + 1]
            dx, dy = target_x - self.x, target_y - self.y
            dist = math.sqrt(dx**2 + dy**2)
            
            if dist < self.speed:
                self.path_index += 1  # Move to next waypoint
            else:
                self.x += self.speed * (dx / dist)  # Move proportionally in x
                self.y += self.speed * (dy / dist)  # Move proportionally in y
        else:
            if not self.reached_base:
                # Enemy reached home base
                home_base_health-= 1 #= home_base_health - 1
                self.reached_base = True
                print(f"Home base hit! Health: {home_base_health}")
            
            enemies.remove(self)  # Remove enemy from the game

    def draw(self):
        """Draw the enemy in the appropriate shape."""
        if self.shape == "square":
            pygame.draw.rect(screen, RED, (self.x - 15, self.y - 15, 30, 30))
        elif self.shape == "circle":
            pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), 15)
        elif self.shape == "cross":
            pygame.draw.line(screen, RED, (self.x - 15, self.y - 15), (self.x + 15, self.y + 15), 3)
            pygame.draw.line(screen, RED, (self.x - 15, self.y + 15), (self.x + 15, self.y - 15), 3)
        pygame.draw.rect(screen, RED, (self.x - 20, self.y - 30, 40, 5))  # Health bar
        pygame.draw.rect(screen, GREEN, (self.x - 20, self.y - 30, 40 * (self.health / enemy_health[self.shape]), 5))

class Tower:
    def __init__(self, x, y, damage, cost, shape):
        self.x, self.y = x, y  # Tower position
        self.range = 100  # Attack range
        self.reload_time = 30  # Cooldown before next shot
        self.reload_counter = 1.5  # Countdown timer
        self.damage = damage  # Damage per shot
        self.cost = cost  # Cost of the tower
        self.shape = shape  # Shape of the tower

    def draw(self):
        """Draw a tower based on its shape."""
        if self.shape == "rect":
            pygame.draw.rect(screen, BLACK, (self.x - 20, self.y - 20, 40, 40))
        elif self.shape == "triangle":
            pygame.draw.polygon(screen, BLACK, [(self.x, self.y - 20), (self.x - 20, self.y + 20), (self.x + 20, self.y + 20)])
        elif self.shape == "T":
            pygame.draw.rect(screen, BLACK, (self.x - 30, self.y - 10, 60, 20))
            pygame.draw.rect(screen, BLACK, (self.x - 10, self.y - 30, 20, 30))
            
    def attack(self, enemies):
        """Attack the nearest enemy within range if reload is ready."""
        global points
        
        if self.reload_counter > 0:
            self.reload_counter -= 1
            return  # Tower is still reloading

        target = None
        min_dist = self.range

        # Find the closest enemy in range
        for enemy in enemies:
            dist = math.sqrt((enemy.x - self.x) ** 2 + (enemy.y - self.y) ** 2)
            if dist <= self.range and (target is None or dist < min_dist):
                target = enemy
                min_dist = dist

        if target:
            target.health -= self.damage  # Apply damage
            
            # TESTING HERE
            #print(f"Before: {target.shape} HP = {target.health}")
            #print(f"After: {target.shape} HP = {target.health}")
            #print(f"Tower at ({self.x}, {self.y}) attacks {target.shape} at ({target.x}, {target.y}) for {self.damage} damage")
            #target.health -= self.damage  # Apply damage

            # Draw a line to visualize the attack
            pygame.draw.line(screen, BLACK, (self.x, self.y), (target.x, target.y), 2)
            
            if target.health <= 0:
                points += target.value
                enemies.remove(target)
                return
            
            self.reload_counter = self.reload_time  # Reset reload timer

def spawn_enemy():
    """Spawn enemies based on the wave number."""
    # enemy_shape = enemy_types[wave % len(enemy_types)]
    enemy_shape = enemy_types[wave % len(enemy_types)]  # Cycle through enemy types
    enemy_health_value = enemy_health[enemy_shape]
    enemy_value_value = enemy_value[enemy_shape]
    
    # Increase the number of enemies with each wave
    num_enemies = wave * 2  # Example: 2 enemies per wave, increases with wave number
    
    for _ in range(num_enemies):
        enemy_shape = enemy_types[wave % len(enemy_types)]
        enemy_health_value = enemy_health[enemy_shape]  # Get correct health
        enemy_value_value = enemy_value[enemy_shape]    # Get correct value
        enemies.append(Enemy(enemy_shape, enemy_health_value, enemy_value_value))

def start_wave():
    """Initialize the wave settings."""
    global enemies_spawned_this_wave, enemy_spawn_timer
    enemies_spawned_this_wave = 0  # Reset enemy spawn count for this wave
    enemy_spawn_timer = 0  # Reset the timer
    
# Run Game
running = True
while running:
    screen.fill(WHITE)
    draw_ui()
    draw_path()
    draw_home_base()
    draw_wave_info()
    
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                selected_tower = "rect"
            elif event.key == pygame.K_2:
                selected_tower = "triangle"
            elif event.key == pygame.K_3:
                selected_tower = "T"
        elif event.type == pygame.MOUSEBUTTONDOWN and selected_tower:
            
            # Get mouse position
            x, y = pygame.mouse.get_pos()
            
            # If not on the path, place tower
            if not is_on_path(x, y):
                if selected_tower == "rect" and points >= 5:
                    towers.append(Tower(x, y, 20, 5, "rect"))
                    points -= 5
                elif selected_tower == "triangle" and points >= 15:
                    towers.append(Tower(x, y, 30, 15, "triangle"))
                    points -= 15
                elif selected_tower == "T" and points >= 50:
                    towers.append(Tower(x, y, 100, 50, "T"))
                    points -= 50
    
    # Start game once initial towers are placed
    if len(towers) > 0 and not game_started:
        game_started = True
        spawn_enemy()  # Spawn the first wave of enemies
    
    if game_started:
        #dead_enemies = []
        # Move and draw enemies
        for enemy in list(enemies):
            enemy.draw()
            enemy.move()
            
            # Remove enemy if health drops to zero
            #if enemy.health <= 0:
                #points = points + enemy.value  # Reward player with points
                #enemies.remove(enemy)
                #dead_enemies.append(enemy)  # Tracks the enemies to remove
                #pygame.display.update()
                
        # Remove dead enemies after iteration
        #for enemy in dead_enemies:
            #enemies.remove(enemy)
    
    # Game Over condition
    if home_base_health <= 0:
        print("Game Over! The home base has been destroyed.")
        running = False # End the game loop
    
    # Check if all enemies are gone, start the next wave
    if game_started and not enemies:  # If no enemies remain, spawn the next wave
        wave += 1
        spawn_enemy()
        
    # Spawn enemies one at a time with delay
    if game_started and enemies_spawned_this_wave < wave:
        enemy_spawn_timer += 1
        if enemy_spawn_timer >= enemy_spawn_delay:
            enemy_spawn_timer = 0  # Reset timer
            enemy_shape = enemy_types[wave % len(enemy_types)]
            enemy_health_value = enemy_health[enemy_shape]
            enemy_value_value = enemy_value[enemy_shape]
            enemies.append(Enemy(enemy_shape, enemy_health_value, enemy_value_value))
            enemies_spawned_this_wave += 1

    # Draw all towers
    for tower in towers:
        tower.draw() # Draws the towers
        tower.attack(enemies)  # Make towers attack enemies
    
    draw_points()
    pygame.display.update() # Update the game window
    clock.tick(60) # Game speed (FPS)

pygame.quit() # Quit's the pygame (GUI window)
sys.exit() # ensures the prgram closes properly


# In[ ]:


#######################################################################
#
# RPG GAME
#
# Name: Cody Thompson
# Project: RPG GAME
# Date: April 9, 2025
# Project Description:
# This game is a simple RPG game that allows the users to select a class to play as.
# Once selected and a name has been given a menu populates on the screen giving the
# users options; [1] Battle Arena\n[2] Shop\n[3] Stats\n[4] Quit
# This projet useds OOP to help Ascertain the player and the ememies.

# CLASSES USED:
# Class Player - holds constructor, level up, use potion, and buy item
# Class Enemy - holds constructor
#######################################################################

# import random  # Importing the random module for generating random numbers
import time  # Importing the time module to add delays (for realism)
import random

# Dictionary defining different character classes and their base attributes:
# - HP (Health Points): Determines how much damage a character can take before dying.
# - Attack: Defines the amount of damage dealt to an enemy.
# - Defense: Reduces incoming damage from enemy attacks.
CHARACTER_CLASSES = {
    "Warrior": {"HP": 100, "Attack": 15, "Defense": 10},
    "Mage": {"HP": 70, "Attack": 20, "Defense": 5},
    "Rogue": {"HP": 80, "Attack": 18, "Defense": 7},
}

# List of enemy types available in the game, each with specific stats.
# - Name: Goblin, HP = 50, Attack = 10, Defense = 5
# - Name: Orc, HP = 80, Attack = 12, Defense = 8
# - Name: Dark Wizard, HP = 60, Attack = 15, Defense = 3
ENEMIES = [
    {"name": "Goblin", "HP": 50, "Attack": 10, "Defense": 5},
    {"name": "Orc", "HP": 80, "Attack": 12, "Defense": 8},
    {"name": "Dark Wizard", "HP": 60, "Attack": 15, "Defense": 3},
]

# Dictionary of shop items available for purchase:
# - Health Potion: Price = 10, Heal Amount = 30
# - Iron Sword: Price = 50, Attack = 5
# - Steel Armor: Price = 50, Defence = 5
SHOP = {
    "Health Potion": {"price": 10, "heal": 30},
    "Iron Sword": {"price": 50, "attack": 5},
    #"Steel Sword": {}
    #"Mythril Sword"
    "Steel Armor": {"price": 50, "defense": 5},
}

# Represents the player character.
# Manages player attributes, inventory, and in-game actions.
class Player:
   
    # Initializes the player with attributes based on the chosen character class
    def __init__(self, name, char_class):
        self.name = name  # Player's name
        self.char_class = char_class  # Selected class type
        self.hp = CHARACTER_CLASSES[char_class]["HP"]  # Set initial HP
        self.attack = CHARACTER_CLASSES[char_class]["Attack"]  # Set attack power
        self.defense = CHARACTER_CLASSES[char_class]["Defense"]  # Set defense power
        self.gold = 100  # Starting gold balance
        self.xp = 0  # Experience points, used for leveling up
        self.level = 1  # Player starts at level 1
        self.inventory = {"Health Potion": 2}  # Player starts with 2 health potions

    def level_up(self):
        """Handles leveling up the player when they earn enough XP."""
        if self.xp >= self.level * 20:  # Level up when XP reaches threshold (20 XP per level)
            self.level += 1
            self.xp = 0  # Reset XP after leveling up
            if self.char_class == "Warrior":
                self.hp += 20  # Increase maximum HP
                self.attack += 6  # Boost attack power
                self.defense += 3  # Increase defense
            elif self.char_class == "Mage":
                self.hp += 3  # Increase Maximum HP
                self.attack += 10  # Boost attack power
                self.defense += 1  # Increase defense
            elif self.char_class == "Rogue":
                self.hp += 5  # Increase Maximum HP
                self.attack += 5  # Boost attack power
                self.defense += 2  # Increase defense
            print(f"\n{self.name} leveled up to Level {self.level}!")

    def use_potion(self):
        """Allows the player to use a health potion to restore HP."""
        if self.inventory.get("Health Potion", 0) > 0:  # Check if player has potions
            self.hp += 30  # Restore health
            self.inventory["Health Potion"] -= 1  # Decrease potion count
            print(f"\n{self.name} used a Health Potion! HP restored to {self.hp}.")
        else:
            print("\nYou have no Health Potions!")

    def buy_item(self, item_name):
        """Allows the player to buy an item from the shop if they have enough gold."""
        if item_name in SHOP and self.gold >= SHOP[item_name]["price"]:
            self.gold -= SHOP[item_name]["price"]  # Deduct gold from player
            if "heal" in SHOP[item_name]:  # If the item is a health potion
                self.inventory["Health Potion"] = self.inventory.get("Health Potion", 0) + 1
            elif "attack" in SHOP[item_name]:  # If it's a weapon
                self.attack += SHOP[item_name]["attack"]
            elif "defense" in SHOP[item_name]:  # If it's armor
                self.defense += SHOP[item_name]["defense"]
            print(f"\nBought {item_name}! {self.name}'s stats improved.")
        else:
            print("\nNot enough gold or invalid item.")

class Enemy:
    """
    Represents an enemy that the player can fight.
    Each enemy is randomly chosen from the ENEMIES list.
    """
    def __init__(self):
        """Randomly selects an enemy from the predefined list."""
        enemy = random.choice(ENEMIES)  # Select a random enemy
        self.name = enemy["name"]  # Enemy name
        self.hp = enemy["HP"]  # Enemy HP
        self.attack = enemy["Attack"]  # Enemy attack power
        self.defense = enemy["Defense"]  # Enemy defense power

def battle(player):
    """Handles combat mechanics between the player and an enemy."""
    enemy = Enemy()  # Create a new random enemy
    print(f"\n{player.name} encounters a {enemy.name}!\n")

    while player.hp > 0 and enemy.hp > 0:
        print(f"\n{player.name} (HP: {player.hp}) vs. {enemy.name} (HP: {enemy.hp})")
        action = input("\nChoose action: [A]ttack | [H]eal | [R]un: ").lower()

        if action == "a":
            damage = max(1, player.attack - enemy.defense)  # Calculate damage dealt
            enemy.hp -= damage
            print(f"\n{player.name} attacks for {damage} damage!")
        elif action == "h":
            player.use_potion()  # Heal instead of attacking
            continue  # Skip enemy's turn after healing
        elif action == "r":
            if random.random() < 0.5:  # 50% chance to successfully escape
                print("\nYou successfully escaped!")
                return
            else:
                print("\nEscape failed!")

        if enemy.hp > 0:  # Enemy attacks if still alive
            enemy_damage = max(1, enemy.attack - player.defense)
            player.hp -= enemy_damage
            print(f"\n{enemy.name} attacks for {enemy_damage} damage!")

    if player.hp > 0:
        print(f"\n{player.name} defeated the {enemy.name}!")
        player.xp += 10  # Earn experience points
        gold_earned = random.randint(10, 20)  # Earn random gold amount
        player.gold += gold_earned
        print(f"\nGained {gold_earned} gold & 10 XP!")
        player.level_up()  # Check if player levels up
    else:
        print("\nYou were defeated! Game Over.")

def visit_shop(player):
    """Displays shop items and allows the player to make purchases."""
    print("\nWelcome to the Shop! You have", player.gold, "gold.")
    for item, details in SHOP.items():
        print(f"{item}: {details['price']} gold")

    choice = input("\nEnter item to buy (or 'exit' to leave): ").title()
    if choice in SHOP:
        player.buy_item(choice)
    elif choice == "Exit":
        print("\nLeaving the shop...")
    else:
        print("\nInvalid choice.")
        
def display_stats(player):
    """Displays the player's current stats."""
    print("\nPlayer Stats:")
    print(f"Name: {player.name}")
    print(f"Class: {player.char_class}")
    print(f"Level: {player.level}")
    print(f"HP: {player.hp}")
    print(f"Attack: {player.attack}")
    print(f"Defense: {player.defense}")
    print(f"Gold: {player.gold}")
    print(f"XP: {player.xp}")
    print(f"Inventory: {player.inventory}")

def main():
    """Handles game setup and main menu loop."""
    name = input("\nEnter your character's name: ")
    print("\nWelcome to Arena Master RPG!")

    print("\nChoose your class:")
    for i, cls in enumerate(CHARACTER_CLASSES.keys(), 1):
        print(f"{i}. {cls}")

    choice = input("\nEnter the number of your class: ")
    char_class = list(CHARACTER_CLASSES.keys())[int(choice) - 1]
    
    player = Player(name, char_class)  # Create player character
    print(f"\nWelcome, {player.name} the {char_class}!\n")

    while player.hp > 0:
        print("\nMain Menu:\n[1] Battle Arena\n[2] Shop\n[3] Stats\n[4] Quit")
        choice = input("\nChoose: ")
        if choice == "1":
            battle(player)
        elif choice == "2":
            visit_shop(player)
        elif choice == "3":
            display_stats(player)
        elif choice == "4":
            print("\nThanks For Playing!")
            break
        else:
            print("\nInvalid Input, Try Again.")

if __name__ == "__main__":
    main()


# In[ ]:


#######################################################
#
# MARIO LIKE GAME (WORK INPROGRESS)
#
######################################################


import pygame  # Import Pygame for game development
import sys  # Import sys to handle system-level operations
import random  # Import random to generate new obstacles and enemies

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mario-like Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Define game states
MENU, GAME, SETTINGS = "menu", "game", "settings"
game_state = MENU

# Define difficulty levels (affect player speed)
difficulty_levels = {"Easy": 5, "Medium": 7, "Hard": 10}
current_difficulty = "Medium"  # Default difficulty
player_speed = difficulty_levels[current_difficulty]  # Set initial speed

# Font setup
font = pygame.font.Font(None, 36)

# Menu options
menu_options = ["Start Game", "Load Game", "Settings", "Exit"]
selected_option = 0  # Index of the currently selected menu option

# Function to display text on the screen
def draw_text(text, x, y, selected=False):
    color = BLUE if selected else BLACK  # Highlight selected option
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, (x, y))

# Function to generate a new world with obstacles and enemies
def generate_new_world():
    """Creates a new set of obstacles and enemies when the player moves off-screen."""
    obstacles = [pygame.Rect(random.randint(100, SCREEN_WIDTH - 100), 500, 50, 50) for _ in range(5)]
    enemies = [pygame.Rect(random.randint(100, SCREEN_WIDTH - 100), 500, 50, 50) for _ in range(3)]
    return obstacles, enemies

# Function to handle the main menu
def menu():
    global game_state, selected_option
    
    while game_state == MENU:
        screen.fill(WHITE)  # Clear screen
        
        # Display menu options
        for i, option in enumerate(menu_options):
            draw_text(option, SCREEN_WIDTH // 2 - 100, 200 + i * 50, i == selected_option)

        pygame.display.flip()  # Update screen

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    if selected_option == 0:  # Start Game
                        game_loop()
                    elif selected_option == 1:  # Load Game (placeholder)
                        print("Load Game - Not Implemented")
                    elif selected_option == 2:  # Settings
                        settings()
                    elif selected_option == 3:  # Exit
                        pygame.quit()
                        sys.exit()

# Function to handle settings (difficulty selection)
def settings():
    global game_state, current_difficulty, player_speed
    
    setting_options = list(difficulty_levels.keys())  # Get difficulty names
    selected_setting = setting_options.index(current_difficulty)  # Find current index

    while game_state == MENU:
        screen.fill(WHITE)  # Clear screen
        
        draw_text("Select Difficulty:", SCREEN_WIDTH // 2 - 100, 200)
        for i, difficulty in enumerate(setting_options):
            draw_text(difficulty, SCREEN_WIDTH // 2 - 100, 250 + i * 50, i == selected_setting)

        pygame.display.flip()  # Update screen

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_setting = (selected_setting + 1) % len(setting_options)
                elif event.key == pygame.K_UP:
                    selected_setting = (selected_setting - 1) % len(setting_options)
                elif event.key == pygame.K_RETURN:
                    current_difficulty = setting_options[selected_setting]  # Apply selected difficulty
                    player_speed = difficulty_levels[current_difficulty]  # Update player speed
                    print(f"Difficulty set to {current_difficulty}")
                    return  # Return to menu

# Function to handle the main game loop
def game_loop():
    global game_state
    
    clock = pygame.time.Clock()  # Game clock for controlling FPS
    gravity = 1  # Gravity effect
    jump_strength = -15  # Jumping power
    velocity_y = 0  # Vertical velocity
    is_jumping = False  # Jump state

    player = pygame.Rect(100, 500, 50, 50)  # Player character
    ground = pygame.Rect(0, 550, SCREEN_WIDTH, 50)  # Ground platform

    obstacles, enemies = generate_new_world()  # Generate initial world

    game_state = GAME  # Set game state to active

    while game_state == GAME:
        screen.fill(WHITE)  # Clear screen
        pygame.draw.rect(screen, BLACK, ground)  # Draw ground
        pygame.draw.rect(screen, BLUE, player)  # Draw player

        # Draw obstacles
        for obstacle in obstacles:
            pygame.draw.rect(screen, GREEN, obstacle)

        # Draw enemies
        for enemy in enemies:
            pygame.draw.rect(screen, RED, enemy)

        pygame.display.flip()  # Update screen
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Get keys pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:  # Move left
            player.x -= player_speed
        if keys[pygame.K_RIGHT]:  # Move right
            player.x += player_speed
        if keys[pygame.K_SPACE] and not is_jumping:  # Jump
            velocity_y = jump_strength
            is_jumping = True

        # Apply gravity
        velocity_y += gravity
        player.y += velocity_y

        # Collision with ground
        if player.colliderect(ground):
            player.y = ground.y - player.height  # Keep player on ground
            is_jumping = False  # Reset jumping state
            velocity_y = 0  # Stop falling

        # Collision with obstacles
        for obstacle in obstacles:
            if player.colliderect(obstacle):
                player.y = obstacle.y - player.height  # Stand on obstacle
                is_jumping = False
                velocity_y = 0

        # If player moves off the screen, generate a new world
        if player.x > SCREEN_WIDTH:
            player.x = 0  # Reset player to left side
            obstacles, enemies = generate_new_world()  # Generate new world
        elif player.x < 0:
            player.x = SCREEN_WIDTH - player.width  # Move to right side
            obstacles, enemies = generate_new_world()  # Generate new world

        clock.tick(30)  # Limit FPS to 30

# Start the game by showing the menu
menu()


# In[ ]:




