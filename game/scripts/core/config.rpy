## Configurações iniciais do Honey Project
define config.name = "Honey Project"
define config.version = "0.1.0"

# Personagens usados na narrativa
define o = Character("Oliver", color="#f3c623")
define m = Character("Mel", color="#ff8fb1")
define g = Character("Gustavo", color="#8ec7ff")
define j = Character("Jade", color="#9be39c")

default persistent.honey_seen_intro = False

init python:
    # Velocidade padrão das animações de caminhada
    ANIMATION_SPEED = 0.15

    # Caminhos auxiliares para os sprites
    def sprite_frames(name, direction):
        return [f"images/characters/{name}/{name}_{direction}_{frame}.png" for frame in range(3)]

    def build_animation(name, direction):
        frames = []
        for frame in sprite_frames(name, direction):
            frames.extend([frame, ANIMATION_SPEED])
        return Animation(*frames)

# Imagem de fundo padrão para o hub
define config.overlay_functions = []
image bg overworld = "images/backgrounds/overworld.png"
