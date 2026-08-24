transform t11:
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom 1.15
        xcenter 1280 yoffset -20
        easein .25 yoffset 0 zoom 1.20 alpha 1.0

transform t21:
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom 1.15
        xcenter 850 yoffset -20
        easein .25 yoffset 0 zoom 1.20 alpha 1.0

transform t22:
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom 1.15
        xcenter 1700 yoffset -20
        easein .25 yoffset 0 zoom 1.20 alpha 1.0

transform t31:
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom 1.15
        xcenter 640 yoffset -20
        easein .25 yoffset 0 zoom 1.20 alpha 1.0

transform t32:
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom 1.15
        xcenter 1280 yoffset -20
        easein .25 yoffset 0 zoom 1.20 alpha 1.0

transform t33:
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom 1.15
        xcenter 1920 yoffset -20
        easein .25 yoffset 0 zoom 1.20 alpha 1.0

transform lhide:
    ease 1.0 xoffset -2000









# Him -----------------------------------------------------------

image him 11 = "images/him/1.png"
image him 12 = "images/him/2.png"
image him 13 = "images/him/3.png"
image him 14 = "images/him/4.png"

image him 21 = "images/him/21.png"
image him 22 = "images/him/22.png"
image him 23 = "images/him/23.png"
image him 24 = "images/him/24.png"

image him 31 = "images/him/31.png"
image him 32 = "images/him/32.png"

image him 41 = "images/him/41.png"
image him 42 = "images/him/42.png"

image him 51 = "images/him/51.png"
image him 52 = "images/him/52.png"






# Stella: Age 8 -------------------------------------------------

image stella 8y1 = "images/stella/1/1.png"
image stella 8y2 = "images/stella/1/2.png"
image stella 8y3 = "images/stella/1/3.png"
image stella 8y4 = "images/stella/1/4.png"
image stella 8y5 = "images/stella/1/5.png"
image stella 8y6 = "images/stella/1/6.png"
image stella 8y7 = "images/stella/1/7.png"
image stella 8y8 = "images/stella/1/8.png"
image stella 8y9 = "images/stella/1/9.png"
image stella 8y10 = "images/stella/1/10.png"
image stella 8y11 = "images/stella/1/11.png"









define s = DynamicCharacter('s_name', image='stella', what_prefix='"', what_suffix='"', ctc_position="fixed")
define h = DynamicCharacter('h_name', image='Him', what_prefix='"', what_suffix='"', ctc_position="fixed")
define dad = DynamicCharacter('dad_name', image='Dad', what_prefix='"', what_suffix='"', ctc_position="fixed")
define mom = DynamicCharacter('mom_name', image='Mom', what_prefix='"', what_suffix='"', ctc_position="fixed")
define m = DynamicCharacter('m_name', image='Mina', what_prefix='"', what_suffix='"', ctc_position="fixed")
define extra = DynamicCharacter('extra_name', image='extra', what_prefix='"', what_suffix='"', ctc_position="fixed")
define lena = DynamicCharacter('l_name', image='Lena', what_prefix='"', what_suffix='"', ctc_position="fixed")