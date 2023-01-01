import pyglet
import random

# Set the screen size
screen_size = (800, 600)

# Set the player size and initial position
player_size = (50, 50)
player_pos = [screen_size[0]//2 - player_size[0]//2, screen_size[1] - player_size[1]]

# Set the player speed
player_speed = 5

# Set the obstacle size and initial position
obstacle_size = (50, 50)
obstacle_pos = [random.randint(0, screen_size[0] - obstacle_size[0]), 0]

# Set the obstacle speed
obstacle_speed = 5

# Set the game over flag and score
game_over = False
score = 0

# Create the window
window = pyglet.window.Window(width=screen_size[0], height=screen_size[1])

# Load the player and obstacle images
player_image = pyglet.image.load('player.png')
obstacle_image = pyglet.image.load('obstacle.png')

@window.event
def on_draw():
    # Clear the window
    window.clear()

    # Draw the player and obstacle images
    player_image.blit(player_pos[0], player_pos[1])
    obstacle_image.blit(obstacle_pos[0], obstacle_pos[1])

def update(dt):
    # Update the player position
    player_pos[0] += player_speed

    # Check if the player has collided with the edges of the screen
    if player_pos[0] < 0 or player_pos[0] + player_size[0] > screen_size[0]:
        player_speed = -player_speed

    # Update the obstacle position
    obstacle_pos[1] += obstacle_speed

    # Check if the obstacle has moved off the screen
    if obstacle_pos[1] > screen_size[1]:
        # Increment the score and move the obstacle to a new random position
        score += 1
        obstacle_pos = [random.randint(0, screen_size[0] - obstacle_size[0]), 0]

    # Check if the player has collided with the obstacle
    if player_pos[0] < obstacle_pos[0] + obstacle_size[0] and player_pos[0] + player_size[0] > obstacle_pos[0]:
        if player_pos[1] < obstacle_pos[1] + obstacle_size[1] and player_pos[1] + player_size[1] > obstacle_pos[1]:
            game_over = True
            pyglet.app.exit()

# Schedule the update function to be called regularly
pyglet.clock.schedule_interval(update, 1/60.0)

# Run the pyg