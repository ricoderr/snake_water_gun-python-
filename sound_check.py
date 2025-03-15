import pygame

# Initialize Pygame
pygame.init()

# Load the sound
sound = pygame.mixer.Sound("win.wav")

# Set the volume (0.0 to 1.0)
sound.set_volume(0.5)  # Set volume to 50%

# Play the sound
sound.play()

# Keep the program running long enough to hear the sound
pygame.time.delay(2000)  # Delay for 2 seconds

# Quit Pygame
pygame.quit()
