## Telas básicas para o Honey Project
## Adaptado do template padrão do Ren'Py

screen say(who, what):
    window:
        id "window"
        text what id "what"

    if who:
        window:
            style "namebox"
            text who id "who"

screen choice(items):
    vbox:
        style_prefix "choice"
        for i in items:
            textbutton i.caption action i.action

screen navigation_overlay():
    zorder 100
    vbox:
        align (0.98, 0.98)
        spacing 4
        text "ESC para menu" size 14 xalign 1.0

init python:
    config.overlay_screens.append("navigation_overlay")
