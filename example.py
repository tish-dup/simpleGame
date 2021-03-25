
import pygame  # Imports a game library to use specific functions in this program.
import random  # Import to generate random numbers.

# Initialize the pygame modules to get everything started.

pygame.init()

# The screen that will be created needs a width and a height.

screen_width = 1040
screen_height = 680
# This creates the screen and gives it the width and height specified as a 2 item sequence.
screen = pygame.display.set_mode((screen_width, screen_height))

# This creates the player and the prize and gives them the image found in this folder.

player = pygame.image.load("image.png")
prize = pygame.image.load("prize.jpg")


# Create a class Enemy for the enemy and assign properties to the class.
class Enemy:
    def __init__(self):
        # This creates the enemy and gives it the image found in this folder.
        self.image = pygame.image.load("enemy.png")
        # Get the width and height of the images in order to do boundary detection (i.e. make sure the image stays
        # within screen boundaries or know when the image is off the screen).
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        # Make the enemy start off screen and at a random x position and random y position.
        self.positionX = random.randint(screen_width, screen_width * 2)
        self.positionY = random.randint(0, screen_height - self.height)
        # Generate a random number between 0.5 and 0.7 for the speed at which the enemy moves
        self.speed_positionX = random.randint(5, 7) / 10
        # Create a box around the enemy so that we can determine when the player collides with the enemy.
        self.enemyBox = pygame.Rect(self.image.get_rect())
        self.enemyBox.top = self.positionY
        self.enemyBox.left = self.positionX


# Create an array for the enemies so that we can generate a random amount of enemies. The minimum amount is set at 3
# and the maximum amount at 7.
enemies_array = []
num_of_enemies = random.randint(3, 7)

# In for loop from range 1 to random number of enemies, append each enemies to the array.
# This will generate a random amount of enemies (between 3 and 7) for the game.
for enemy in range(1, num_of_enemies):
    enemies_array.append(Enemy())

# Get the width and height of the images in order to do boundary detection
# (i.e. make sure the image stays within screen boundaries or know when the image is off the screen).

image_height = player.get_height()
image_width = player.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()

print("This is the height of the player image: " + str(image_height))
print("This is the width of the player image: " + str(image_width))

# Store the positions of the player as variables to be used later in the code.

playerXPosition = 50
playerYPosition = random.randint(0, screen_height - image_height)

# Make the prize start off screen and at a random x and y positions.

prize_XPosition = random.randint(screen_width, screen_width * 2)
prize_YPosition = random.randint(0, screen_height - prize_height)

# This checks if the up, down, left or right key is pressed.
# Right now they are not so make them equal to the boolean value (True or False) of False. 
# Boolean values are True or False values that can be used to test conditions and test states that are binary,
# i.e. either one way or the other.

keyUp = False
keyDown = False
keyLeft = False
keyRight = False

# This is the game loop.
# In games the game logic needs to run over and over again.
# You need to refresh/update the screen window and apply changes to represent real time game play.

while 1:  # This is a looping structure that will loop the indented code until it is told to stop
    screen.fill(0)  # Clears the screen.
    # This draws the player image to the screen at the position specified. I.e. (50, random).
    screen.blit(player, (playerXPosition, playerYPosition))
    # This draws the prize image to the screen at a random position.
    screen.blit(prize, (prize_XPosition, prize_YPosition))

    # To ensure that each enemy that was create in the for loop appears on the screen.
    for enemy in enemies_array:
        screen.blit(enemy.image, (enemy.positionX, enemy.positionY))

    pygame.display.flip()  # This updates the screen.

    # This loops through events in the game.

    for event in pygame.event.get():

        # This event checks if the user quits the program, then if so it exits the program. 

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        # This event checks if the user press a key down.

        if event.type == pygame.KEYDOWN:

            # Test if the key pressed is the one we want.

            if event.key == pygame.K_UP:  # pygame.K_UP represents a keyboard key constant.
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True

        # This event checks if the key is up(i.e. not pressed by the user).

        if event.type == pygame.KEYUP:

            # Test if the key released is the one we want.

            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False

    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.

    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position. 

    if keyUp == True:
        if playerYPosition > 0:  # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - image_height:  # This makes sure that the user does not move the player below the window.
            playerYPosition += 1
    if keyLeft == True:
        if playerXPosition > 0:  # This makes sure that the user does not move the player above the window.
            playerXPosition -= 1
    if keyRight == True:
        if playerXPosition < screen_width - image_width:  # This makes sure that the user does not move the player outside the window on the right.
            playerXPosition += 1

    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We the need to test if these boxes intersect. If they do then there is a collision.

    # Bounding box for the player:

    playerBox = pygame.Rect(player.get_rect())

    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 

    playerBox.top = playerYPosition
    playerBox.left = playerXPosition

    # In a for loop, create a bounding box for each enemy that has been generated

    for box in enemies_array:
        box.enemyBox = pygame.Rect(box.image.get_rect())
        box.enemyBox.top = box.positionY
        box.enemyBox.left = box.positionX

    # Bounding box for the prize:

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prize_YPosition
    prizeBox.left = prize_XPosition

    # Test collision of the boxes. Use for loop to test the collision with evey enemy that has been generated
    for collision in enemies_array:
        if playerBox.colliderect(collision.enemyBox):
            # Display losing status to the user:

            print("You lose!")

            # Quite game and exit window:

            pygame.quit()
            exit(0)

    # If the enemy is off the screen the user wins the game:
    # Use for loop to check if whether all the enemies are off the screen
    num_enemies_past = 0
    for enemy_gone in enemies_array:
        if enemy_gone.positionX < 0 - enemy_gone.width:
            num_enemies_past += 0

    if num_enemies_past == len(enemies_array):
        # Display wining status to the user: 

        print("You win!")

        # Quite game and exit window: 
        pygame.quit()

        exit(0)

    # If player collides with the prize box, the user wins the game:

    if playerBox.colliderect(prizeBox):
        # Display winning status to the user:

        print("You win!")

        # Quite game and exit window:

        pygame.quit()
        exit(0)

    # Make enemy approach the player. Generate different speed for each enemy.

    for enemy_speed in enemies_array:
        enemy_speed.positionX -= enemy_speed.speed_positionX

    # Make prize approach player at a slower pace than enemies.
    prize_XPosition -= 0.3

    # ================The game loop logic ends here. =============

# Reference: https://www.w3schools.com/python/python_classes.asp
# Used this reference to create an object for the enemy which allows me to create a random
# amount of enemies in for loops.
