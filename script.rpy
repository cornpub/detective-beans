
define r = Character("Insert Red herring here")
define k = Character("Insert killer here")
define w = Character("Insert first witness here")
define w2 = Character("Insert second witness here")
define w3 = Character("Insert Third witness here")
define m = Character("Insert main character here")
define v = Character("Insert Victim here")
define game = Character("    ", color="#009900", what_color="#009900")
define player_name = ("[player_name]")


# The game starts here.

label start:
    init python:
        renpy.music.register_channel("music2", "sfx", True)
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene placeholderroom
    show gar
    "Gattski""I'm not supposed to be in this game."

    return
