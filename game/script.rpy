# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init:
    image figure zoomed:
        "figure hidden.png"
        zoom 0.7
    image figure hidden:
        "figure hidden.png"
    image bg mc_room_morning:
        "bg mc_room_morning.jpg"
        zoom 0.70

    image bg mc_room_morning_zoomed:
        im.Blur("bg mc_room_morning.jpg", 2.0)

    define mc = Character("Kouta Ace", color="#ff0000")
    define yuuna = Character("Yuuna Kisaragi")
    define rio = Character("Rio Amari")

style block2_multiple2_say_window:
    background None

style block2_multiple2_namebox:
    xpos 650

style multiple2_say_dialogue:
    xsize 372

style block2_multiple2_say_dialogue:
    xpos 675

# The game starts here.

label start:

    $ rio_route = 0

    jump opening_sequence

    # This ends the game.
    return
