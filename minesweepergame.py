import pygame
import minesweeperengine
from math import floor
from random import randint
import sys
import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
screen_width = screensize[0]
screen_height = screensize[1]
### KEY FOR VISIBLE BOARD

# First character:
# X = Hidden tile, E = empty tile, numbers 1-8 = tile number, O = un-numbered tile (which gets dealt with quickly)
# END GAME:
# M = mine, R = red mine, W = wrong flag

# Second character:
# F = flagged
# O = non-flagged (including open tiles)

# Generates 2 random numbers with an inputted range inclusive

def int_to_menu_num_image(num):
    match num:
        case 0:
            return menu_zero_image
        case 1:
            return menu_one_image
        case 2:
            return menu_two_image
        case 3:
            return menu_three_image
        case 4:
            return menu_four_image
        case 5:
            return menu_five_image
        case 6:
            return menu_six_image
        case 7:
            return menu_seven_image
        case 8:
            return menu_eight_image
        case 9:
            return menu_nine_image

def make_random_coord(x_min, x_max, y_min, y_max):
    x = randint(x_min, x_max)
    y = randint(y_min, y_max)
    return [x, y]

def draw_board():
    screen.fill(background_colour)
    coords = [0, 0]
    for a in range(game.height): # For every row number
        coords[1] = a * tile_size # Set the a coord
        for b in range(game.width): # For every spot in the row
            coords[0] = b * tile_size # Set the b coord
            match game.visible_board[a][b][0]:
                
                case "X":
                    screen.blit(tile_image, coords)
                case "E":
                    screen.blit(open_tile_image, coords)
                case "1":
                    screen.blit(one_tile_image, coords)
                case "2":
                    screen.blit(two_tile_image, coords)
                case "3":
                    screen.blit(three_tile_image, coords)
                case "4":
                    screen.blit(four_tile_image, coords)
                case "5":
                    screen.blit(five_tile_image, coords)
                case "6":
                    screen.blit(six_tile_image, coords)
                case "7":
                    screen.blit(seven_tile_image, coords)
                case "8":
                    screen.blit(eight_tile_image, coords)
                case "M":
                    screen.blit(mine_tile_image, coords)
                case "R":
                    screen.blit(red_mine_tile_image, coords)
                case "W":
                    screen.blit(wrong_flag_tile_image, coords)
                case "!":
                    screen.blit(win_tile_image, coords)
            if game.visible_board[a][b] == "XF": # Draw the flag icon
                screen.blit(flag_tile_image, coords)
            elif game.visible_board[a][b] == "!F":
                screen.blit(win_flag_tile_image, coords)

    pygame.display.flip()

def coords_to_square(coords):
    x = coords[0]
    y = coords[1]
    b = floor(x/tile_size)
    a = floor(y/tile_size)
    return [a, b]

### SET UP GAME

# Menu screen
menu_height = 500
menu_width = 500

menu_screen = pygame.display.set_mode((menu_width, menu_height))

pygame.display.set_caption("PySweeper Menu")
pygame.display.set_icon(pygame.image.load("data/flag_tile.png"))

# Units
w_unit = menu_width / 256
h_unit = menu_height / 256

# Button sizes
button_height = 28.444444 * h_unit
button_width = 28.444444 * w_unit

# Button images
up_button_image = pygame.transform.scale(pygame.image.load("data/up_button.png"), [button_width, button_height])
down_button_image = pygame.transform.scale(pygame.image.load("data/down_button.png"), [button_width, button_height])
double_up_button_image = pygame.transform.scale(pygame.image.load("data/double_up_button.png"), [button_width, button_height])
double_down_button_image = pygame.transform.scale(pygame.image.load("data/double_down_button.png"), [button_width, button_height])

menu_zero_image = pygame.transform.scale(pygame.image.load("data/zero_tile.png"), [button_width, button_height])
menu_one_image = pygame.transform.scale(pygame.image.load("data/one_tile.png"), [button_width, button_height])
menu_two_image = pygame.transform.scale(pygame.image.load("data/two_tile.png"), [button_width, button_height])
menu_three_image = pygame.transform.scale(pygame.image.load("data/three_tile.png"), [button_width, button_height])
menu_four_image = pygame.transform.scale(pygame.image.load("data/four_tile.png"), [button_width, button_height])
menu_five_image = pygame.transform.scale(pygame.image.load("data/five_tile.png"), [button_width, button_height])
menu_six_image = pygame.transform.scale(pygame.image.load("data/six_tile.png"), [button_width, button_height])
menu_seven_image = pygame.transform.scale(pygame.image.load("data/seven_tile.png"), [button_width, button_height])
menu_eight_image = pygame.transform.scale(pygame.image.load("data/eight_tile.png"), [button_width, button_height])
menu_nine_image = pygame.transform.scale(pygame.image.load("data/nine_tile.png"), [button_width, button_height])
play_button_image = pygame.transform.scale(pygame.image.load("data/play_button.png"), [button_width * 3, button_height])
number_outline_image = pygame.transform.scale(pygame.image.load("data/number_outline.png"), [button_width * 3, button_height])
number_outline_image.set_colorkey((255, 255, 255))

menu_background_image = pygame.transform.scale(pygame.image.load("data/open_tile.png"), (menu_width * 2, menu_height * 2))

# Text images
width_text_image = pygame.transform.scale(pygame.image.load("data/width_text.png"), [button_width * 3, button_height])
height_text_image = pygame.transform.scale(pygame.image.load("data/height_text.png"), [button_width * 3, button_height])
mines_text_image = pygame.transform.scale(pygame.image.load("data/mines_text.png"), [button_width * 3, button_height])

# Button rects

# Coords
# X (number coords are used for the three possible digits for each value)
w_num_one_x = 0
w_x = button_width
w_num_three_x = 2 * button_width - 1

h_num_one_x = 3 * button_height
h_x = 4 * button_height - 1
h_num_three_x = 5 * button_height - 1

b_num_one_x = 6 * button_width
b_x = 7 * button_width
b_num_three_x = 8 * button_width - 1

# Y
up_y = button_height # Up button height
num_y = 2 * button_height
down_y = 3 * button_height # Down button height
double_down_y = 4 * button_height # Other down button height
text_y = 5 * button_height
play_y = menu_height - button_height

# Rects
w_double_up_rect = pygame.Rect(w_x, 0, button_width, button_height)
w_up_rect = pygame.Rect(w_x, up_y, button_width, button_height)
w_down_rect = pygame.Rect(w_x, down_y, button_width, button_height)
w_double_down_rect = pygame.Rect(w_x, double_down_y, button_width, button_height)

h_double_up_rect = pygame.Rect(h_x, 0, button_width, button_height)
h_up_rect = pygame.Rect(h_x, up_y, button_width, button_height)
h_down_rect = pygame.Rect(h_x, down_y, button_width, button_height)
h_double_down_rect = pygame.Rect(h_x, double_down_y, button_width, button_height)

b_double_up_rect = pygame.Rect(b_x, 0, button_width, button_height)
b_up_rect = pygame.Rect(b_x, up_y, button_width, button_height)
b_down_rect = pygame.Rect(b_x, down_y, button_width, button_height)
b_double_down_rect = pygame.Rect(b_x, double_down_y, button_width, button_height)

play_rect = pygame.Rect(h_num_one_x, play_y, button_width * 3, button_height)

### MENU LOOP
menu_on = True
game_width = 30
game_height = 16
game_mines = 99
while menu_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # Button presses
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            coords = pygame.mouse.get_pos()
            tile_count = game_height * game_width

            # Width buttons
            if w_double_up_rect.collidepoint(coords) and game_width <= 20: # Width up by 10
                game_width += 10
            elif w_up_rect.collidepoint(coords) and game_width < 30: # Width up by 1
                game_width += 1
            elif w_down_rect.collidepoint(coords) and game_width > 9: # Widith down by 1
                game_width -= 1
                if game_mines > game_width * game_height - 9 or game_mines >= game_width * game_height / 2:
                    game_mines = min(game_width * game_height - 9, int(game_width * game_height / 2 - 1))
            elif w_double_down_rect.collidepoint(coords) and game_width > 19: # Width down by 10
                game_width -= 10
                if game_mines > game_width * game_height - 9 or game_mines >= game_width * game_height / 2:
                    game_mines = min(game_width * game_height - 9, int(game_width * game_height / 2 - 1))

            # Height buttons
            elif h_double_up_rect.collidepoint(coords) and game_height <= 20: # height up by 10
                game_height += 10
            elif h_up_rect.collidepoint(coords) and game_height < 30: # height up by 1
                game_height += 1
            elif h_down_rect.collidepoint(coords) and game_height > 9: # height down by 1
                game_height -= 1
                if game_mines > game_width * game_height - 9 or game_mines >= game_width * game_height / 2:
                    game_mines = min(game_width * game_height - 9, int(game_width * game_height / 2 - 1))
            elif h_double_down_rect.collidepoint(coords) and game_height > 19: # height down by 10
                game_height -= 10
                if game_mines > game_width * game_height - 9 or game_mines >= game_width * game_height / 2:
                    game_mines = min(game_width * game_height - 9, int(game_width * game_height / 2 - 1))

            # Mine buttons
            elif b_double_up_rect.collidepoint(coords) and game_mines <= 190 and game_mines + 10 < tile_count: # mines up by 10
                game_mines += 10
            elif b_up_rect.collidepoint(coords) and game_mines < 200 and game_mines + 1 < tile_count: # mines up by 1
                game_mines += 1
            elif b_down_rect.collidepoint(coords) and game_mines > 1: # mines down by 1
                game_mines -= 1
            elif b_double_down_rect.collidepoint(coords) and game_mines > 10: # mines down by 10
                game_mines -= 10
            elif play_rect.collidepoint(coords):
                menu_on = False
            

    ### Draw menu
    menu_screen.blit(menu_background_image, (menu_width / -2, menu_height / -2))

    ### Buttons
    menu_screen.blit(play_button_image, (h_num_one_x, play_y))

    # Up
    menu_screen.blit(up_button_image, w_up_rect)
    menu_screen.blit(up_button_image, h_up_rect)
    menu_screen.blit(up_button_image, b_up_rect)

    # Double up
    menu_screen.blit(double_up_button_image, w_double_up_rect)
    menu_screen.blit(double_up_button_image, h_double_up_rect)
    menu_screen.blit(double_up_button_image, b_double_up_rect)

    # Down
    menu_screen.blit(down_button_image, w_down_rect)
    menu_screen.blit(down_button_image, h_down_rect)
    menu_screen.blit(down_button_image, b_down_rect)

    # Double down
    menu_screen.blit(double_down_button_image, w_double_down_rect)
    menu_screen.blit(double_down_button_image, h_double_down_rect)
    menu_screen.blit(double_down_button_image, b_double_down_rect)

    # Text
    menu_screen.blit(width_text_image, (w_num_one_x, text_y))
    menu_screen.blit(height_text_image, (h_num_one_x, text_y))
    menu_screen.blit(mines_text_image, (b_num_one_x, text_y))
    
    # Numbers
    game_width_string = str(game_width)
    game_height_string = str(game_height)
    game_mines_string = str(game_mines)

    # Width numbers
    if len(game_width_string) == 1: # Width is only one digit long
        menu_screen.blit(menu_zero_image, (w_num_one_x, num_y)) # First digit 0
        menu_screen.blit(menu_zero_image, (w_x, num_y)) # Second digit 0
        menu_screen.blit(int_to_menu_num_image(game_width), (w_num_three_x, num_y)) # Third digit
        
        
    elif len(game_width_string) == 2: # Width is 2 digits long
        menu_screen.blit(menu_zero_image, (w_num_one_x, num_y)) # First digit 0
        menu_screen.blit(int_to_menu_num_image(int(game_width_string[0])), (w_x, num_y)) # Second digit
        menu_screen.blit(int_to_menu_num_image(int(game_width_string[1])), (w_num_three_x, num_y)) # Third digit

    elif len(game_width_string) == 3:
        menu_screen.blit(int_to_menu_num_image(int(game_width_string[0])), (w_num_one_x, num_y)) # First digit 0
        menu_screen.blit(int_to_menu_num_image(int(game_width_string[1])), (w_x, num_y)) # Second digit
        menu_screen.blit(int_to_menu_num_image(int(game_width_string[2])), (w_num_three_x, num_y)) # Third digit
    menu_screen.blit(number_outline_image, (w_num_one_x, num_y)) # Outline for the numbers


    # Height numbers
    if len(game_height_string) == 1: # Height is only one digit long
        menu_screen.blit(menu_zero_image, (h_num_one_x, num_y)) # First digit 0
        menu_screen.blit(menu_zero_image, (h_x, num_y)) # Second digit 0
        menu_screen.blit(int_to_menu_num_image(game_height), (h_num_three_x, num_y)) # Third digit
        
        
    elif len(game_height_string) == 2: # height is 2 digits long
        menu_screen.blit(menu_zero_image, (h_num_one_x, num_y)) # First digit 0
        menu_screen.blit(int_to_menu_num_image(int(game_height_string[0])), (h_x, num_y)) # Second digit
        menu_screen.blit(int_to_menu_num_image(int(game_height_string[1])), (h_num_three_x, num_y)) # Third digit

    elif len(game_height_string) == 3:
        menu_screen.blit(int_to_menu_num_image(int(game_height_string[0])), (h_num_one_x, num_y)) # First digit 0
        menu_screen.blit(int_to_menu_num_image(int(game_height_string[1])), (h_x, num_y)) # Second digit
        menu_screen.blit(int_to_menu_num_image(int(game_height_string[2])), (h_num_three_x, num_y)) # Third digit
    menu_screen.blit(number_outline_image, (h_num_one_x, num_y)) # Outline for the numbers

    # Mine numbers
    if len(game_mines_string) == 1: # mine is only one digit long
        menu_screen.blit(menu_zero_image, (b_num_one_x, num_y)) # First digit 0
        menu_screen.blit(menu_zero_image, (b_x, num_y)) # Second digit 0
        menu_screen.blit(int_to_menu_num_image(game_mines), (b_num_three_x, num_y)) # Third digit
        
        
    elif len(game_mines_string) == 2: # mine is 2 digits long
        menu_screen.blit(menu_zero_image, (b_num_one_x, num_y)) # First digit 0
        menu_screen.blit(int_to_menu_num_image(int(game_mines_string[0])), (b_x, num_y)) # Second digit
        menu_screen.blit(int_to_menu_num_image(int(game_mines_string[1])), (b_num_three_x, num_y)) # Third digit

    elif len(game_mines_string) == 3:
        menu_screen.blit(int_to_menu_num_image(int(game_mines_string[0])), (b_num_one_x, num_y)) # First digit 0
        menu_screen.blit(int_to_menu_num_image(int(game_mines_string[1])), (b_x, num_y)) # Second digit
        menu_screen.blit(int_to_menu_num_image(int(game_mines_string[2])), (b_num_three_x, num_y)) # Third digit
    menu_screen.blit(number_outline_image, (b_num_one_x, num_y)) # Outline for the numbers
    
    
    pygame.display.flip()
pygame.display.quit()

# Engine

game = minesweeperengine.GameState(game_width, game_height, game_mines)

# Dimensions
width = 1920
height = width/game.width_height_ratio
while height > screen_height - 100:
    width -= 1
    height = width/game.width_height_ratio

# Pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PySweeper")
pygame.display.set_icon(pygame.image.load("data/flag_tile.png"))

# Screen
tile_size = width/game.width
background_colour = (120, 120, 120)

### IMAGES

# Tiles
tile_image = pygame.transform.scale(pygame.image.load("data/tile.png"), (tile_size, tile_size))
open_tile_image = pygame.transform.scale(pygame.image.load("data/open_tile.png"), (tile_size, tile_size))
mine_tile_image = pygame.transform.scale(pygame.image.load("data/mine_tile.png"), (tile_size, tile_size))
red_mine_tile_image = pygame.transform.scale(pygame.image.load("data/red_mine_tile.png"), (tile_size, tile_size))
flag_tile_image = pygame.transform.scale(pygame.image.load("data/flag_tile.png"), (tile_size, tile_size))
wrong_flag_tile_image = pygame.transform.scale(pygame.image.load("data/wrong_flag_tile.png"), (tile_size, tile_size))
win_tile_image = pygame.transform.scale(pygame.image.load("data/win_tile.png"), (tile_size, tile_size))
win_flag_tile_image = pygame.transform.scale(pygame.image.load("data/win_flag_tile.png"), (tile_size, tile_size))

# Numbers
one_tile_image = pygame.transform.scale(pygame.image.load("data/one_tile.png"), (tile_size, tile_size))
two_tile_image = pygame.transform.scale(pygame.image.load("data/two_tile.png"), (tile_size, tile_size))
three_tile_image = pygame.transform.scale(pygame.image.load("data/three_tile.png"), (tile_size, tile_size))
four_tile_image = pygame.transform.scale(pygame.image.load("data/four_tile.png"), (tile_size, tile_size))
five_tile_image = pygame.transform.scale(pygame.image.load("data/five_tile.png"), (tile_size, tile_size))
six_tile_image = pygame.transform.scale(pygame.image.load("data/six_tile.png"), (tile_size, tile_size))
seven_tile_image = pygame.transform.scale(pygame.image.load("data/seven_tile.png"), (tile_size, tile_size))
eight_tile_image = pygame.transform.scale(pygame.image.load("data/eight_tile.png"), (tile_size, tile_size))



### GAME LOOP
while True:
    
    alive = True
    first_turn = True
    draw_board()

    while alive: # Each game loop

        # Event handler
        for event in pygame.event.get():

            # Quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Left click or space
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 or event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:

                
                # Set coordinates
                ab = coords_to_square(pygame.mouse.get_pos())
                a = ab[0]
                b = ab[1]
                
                # Not a flagged tile
                if game.visible_board[a][b][1] != "F":

                    # Safe start
                    if first_turn:
                        print("first turn")
                        if game.number_square(ab) != 0: # If your first click isn't on a zero square
                            making_board = True
                            print("you clicked on a mine")
                            while making_board: # Keep making a board until the square is 0
                                game.make_board()
                                print("remade the board")
                                if game.number_square(ab) == 0 and game.board[a][b] != "X": # Check if the first square is now a 0
                                    print("the square is now" + str(game.number_square(ab)) + ", " + str(game.board[a][b]))
                                    making_board = False
                    first_turn = False
                
                    # If you clicked on a hidden, non-flagged tile
                    if game.visible_board[a][b] == "XO":
                    
                        # Set coordinates
                        selected_tile = coords_to_square(pygame.mouse.get_pos())
                        a = selected_tile[0]
                        b = selected_tile[1]

                        # Clicked on a mine
                        if game.board[a][b] == "X":
                            for a in range(game.height):
                                for b in range(game.width):
                                    if game.visible_board[a][b] == "XO": # Hidden unflagged tile
                                        if game.board[a][b] == "X": # Hidden mine
                                            game.visible_board[a][b] = "MO" # Make it a mine
                                        if [a, b] == ab:
                                            game.visible_board[a][b] = "RO" # Make the mine you click on red
                                    if game.visible_board[a][b] == "XF" and game.board[a][b] == "O": # A wrongly flagged tile
                                        game.visible_board[a][b] = "WO"
                            draw_board()
                            pygame.display.flip()
                            alive = False

                        # Clicked on not a mine
                        else:
                            game.visible_board[a][b] = "OO" # Marks the square as an unknown number
                            game.number_board() # Replace "OO" with the number of mines next to the square
                            game.open_board() # If it is a 0, open all tiles around it and run everything above again

                            draw_board()
                            pygame.display.flip()
                        game.make_clean_visible_board()
            
            # Right click (or l shift)
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 3) or (event.type == pygame.KEYDOWN and event.key == pygame.K_LSHIFT):

                # Set coordinates
                ab = coords_to_square(pygame.mouse.get_pos())
                a = ab[0]
                b = ab[1]

                # If you clicked on an unflagged tile
                if game.visible_board[a][b] == "XO":
                    game.visible_board[a][b] = "XF" # Make it flagged
                
                # If you clicked on a flagged tile
                elif game.visible_board[a][b] == "XF":
                    game.visible_board[a][b] = "XO" # Make it not flagged
                draw_board()

            # Left and right click (chording)
            mouse_pressed = pygame.mouse.get_pressed()
            if (mouse_pressed[0] and mouse_pressed[2]) and event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN and event.key == pygame.K_LCTRL):

                # Set coordinates
                ab = coords_to_square(pygame.mouse.get_pos())
                a = ab[0]
                b = ab[1]
                flag_count = 0
                if game.visible_board[a][b] != "X": # If you click on a non hidden tile
                    for i in game.get_surrounding_squares([a, b]): # For every tile touching it
                        if game.visible_board[i[0]][i[1]][1] == "F":
                            flag_count += 1

                    # If there are the right amount of flags
                    if str(flag_count) == game.visible_board[a][b][0]:
                        
                        for i in game.get_surrounding_squares([a, b]): # For every surrounding square
                            a = i[0]
                            b = i[1]
                            ab = [a, b]

                            if game.visible_board[a][b] == "XO": # if it is a hidden tile
        # TODO fix safe start, stop you from clicking if you blow up
                                # Clicked on a mine
                                if game.board[a][b] == "X":
                                    for a in range(game.height):
                                        for b in range(game.width):
                                            if game.visible_board[a][b] == "XO": # Hidden unflagged tile

                                                if game.board[a][b] == "X": # Hidden mine
                                                    game.visible_board[a][b] = "MO" # Make it a mine
                                                    
                                                if [a, b] == ab: # The hidden mine that you clicked on
                                                    game.visible_board[a][b] = "RO" # Make the mine you click on red
                                            if game.visible_board[a][b] == "XF" and game.board[a][b] == "O": # A wrongly flagged tile
                                                game.visible_board[a][b] = "WO"

                                    draw_board()
                                    pygame.display.flip()
                                    alive = False

                                # Clicked on not a mine
                                else:
                                    game.visible_board[a][b] = "OO" # Marks the square as an unknown number
                                    game.number_board() # Replace "OO" with the number of mines next to the square
                                    game.open_board() # If it is a 0, open all tiles around it and run everything above again
                                    draw_board()
                                    pygame.display.flip()
                                game.make_clean_visible_board
        
        if game.is_won():
            for a in range(game.height):
                for b in range(game.width):
                    tile = game.visible_board[a][b]
                    if tile == "XO":
                        game.visible_board[a][b] = "!O"
                    elif tile == "XF":
                        game.visible_board[a][b] = "!F"
            draw_board()
            pygame.display.flip()
            alive = False

    dead = True
    while dead:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                dead = False
                alive = True
                game = minesweeperengine.GameState(game_width, game_height, game_mines)
                pygame.display.flip()
            if event.type == pygame.QUIT:
                pygame.quit()

pygame.quit()