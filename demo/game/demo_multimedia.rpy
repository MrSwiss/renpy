# This file contains demonstrations of Ren'Py's multimedia
# support. Right now, this is just showing off sound and music, but
# Ren'Py does support movies, and we'll add them sometime later.


label demo_multimedia:

    e "Ren'Py supports a number of multimedia functions."

    e "You're probably hearing music playing in the background."

    # This stops the music, and fades it out.
    stop music fadeout 0.5

    e "We can stop it, with a fadeout..."

    # This plays music.
    play music "mozart.ogg"

    e "... and start it playing again."

    # This plays a sound effect.
    play sound "18005551212.ogg"

    e "We can also play up to eight channels of sound effects on top of the music."

    e "Voice support is included as part of Ren'Py, although we don't yet have a demonstration."

    e "We also support playing mpeg movies, but we don't have one to show you right now."

    show eileen concerned

    e "Sorry."

    show eileen happy
    
    e "That's about it for multimedia."

    return
