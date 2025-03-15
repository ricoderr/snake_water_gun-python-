'''
snake vs water ----> snake 
gun vs water   ----> water 
snake vs gun   ----> gun
'''
'''
snake = 1
gun = 0
water = -1
'''
import random # importing necessary modules
import pygame
# Initialize Pygame and the sound mixer
pygame.init()
pygame.mixer.init()

# Load sound effects
win_sound = pygame.mixer.Sound("win.wav")  
lose_sound = pygame.mixer.Sound("lose.wav")  
draw_sound = pygame.mixer.Sound("draw.wav") 
win_sound.set_volume(1) # setting the volumes for the sounds
lose_sound.set_volume(0.5)
draw_sound.set_volume(1)

print("snake = 's' \n gun = 'g' \n water = 'w' ") 
com = random.choice([1,0,-1]) # using random function to make computer choose random number each time.
youDict = {"s": 1, "g": 0, "w": -1} # creating a dict to convert the str input into the int
youStr = input("Enter one from 's' (snake), 'g' (gun), and 'w' (water): ") # taking input from the user 

# Loop to ensure valid input
while youStr == "" or youStr not in youDict:
    print("Choose from 's', 'g', or 'w'")
    youStr = input("Enter again: ")

# Get the corresponding integer value from the dictionary
youInt = youDict[youStr]
 # using conditional expression to decide win and lose 
if (com == 1 and youInt == -1 ):
    print("Computer choses snake\nYou lose!")
    lose_sound.play()

elif (com == 1 and youInt == 0 ):
    print("Computer choses snake\nYou win!")
    win_sound.play() 

elif (com == 0 and youInt == -1):
    print("Computer choses gun\nYou win!!")
    win_sound.play() 

elif (com == 0 and youInt == 1):
    print("Computer choses gun\nYou lose!!")
    lose_sound.play() 

elif (com == -1 and youInt == 1):
    print("Computer choses water\nYou win!!")
    win_sound.play() 

elif (com == -1 and youInt == 0):
    print("Computer choses water\nYou lose!!")
    lose_sound.play() 

else :
    print(f"Computer choses {com}, It's a draw")
    draw_sound.play() 

pygame.time.delay(2000) # 2000 miliseconds = 2 sec delay to let the sound play after win, lose or draw
pygame.quit # quitting the pygame module