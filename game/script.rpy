# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = DynamicCharacter('s_name', image='stella', what_prefix='"', what_suffix='"', ctc_position="fixed")
define h = DynamicCharacter('s_name', image='Him', what_prefix='"', what_suffix='"', ctc_position="fixed")
define dad = DynamicCharacter('s_name', image='Dad', what_prefix='"', what_suffix='"', ctc_position="fixed")
define mom = DynamicCharacter('s_name', image='Mom', what_prefix='"', what_suffix='"', ctc_position="fixed")
define m = DynamicCharacter('s_name', image='Mina', what_prefix='"', what_suffix='"', ctc_position="fixed")
define extra = DynamicCharacter('s_name', image='extra', what_prefix='"', what_suffix='"', ctc_position="fixed")


# The game starts here.

label start:

    $ s_name = "Stella"
    $ h_name = "Him"
    $ dad_name = "Dad"
    $ mom_name = "Mom"
    $ m_name = "Mina"
    $ extra_name = "???"

    jump Story1

    return
