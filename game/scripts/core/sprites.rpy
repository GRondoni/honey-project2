# Definições automáticas de sprites e animações
init python:
    characters = ["oliver", "mel", "gus", "jade"]
    directions = ["down", "left", "right", "up"]

    for name in characters:
        # Frames idle posicionados para reaproveitar a direção para baixo
        renpy.image(f"{name} idle", f"images/characters/{name}/{name}_idle.png")

        for direction in directions:
            renpy.image(
                f"{name} {direction}",
                build_animation(name, direction)
            )

# Transforma dicionários em imagens animadas para uso no mapa
transform walking_center:
    xalign 0.5
    yalign 0.5

transform facing_center:
    xalign 0.5
    yalign 0.5
