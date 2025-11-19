# Honey Project – Um Jogo de Memórias em Ren'Py

Presente especial da família para a mamãe 💛

Este projeto é um jogo desenvolvido em Ren'Py, criado para ser um presente emocional, interativo e único. A experiência combina pixel art personalizada da família — Gustavo, Mel, Jade e Oliver — com animações, narrativa e um pequeno sistema de overworld que serve como hub de memórias.

## Objetivo do Projeto
- Criar um presente especial onde o Oliver introduz o jogo.
- Apresentar memórias importantes da família através de cenas.
- Utilizar sprites animados em 16-bit dos personagens reais.
- Fornecer um jogo fofo, leve e completamente personalizado.

## Personagens Incluídos
Todos os personagens possuem sprites animados (4 direções com 3 frames) e frames idle para uso imediato:
- Gustavo — estilo pixel com cabelo comprido e camiseta preta.
- Mel — roupa preta, cabelo longo com franja.
- Jade — camiseta verde com estrela, saia rosa e calça lilás.
- Oliver — bebê com body amarelo de listras.

Os arquivos devem ser organizados em `game/images/characters/<nome>/` e mapeados automaticamente por `game/scripts/core/sprites.rpy`.

## Estrutura do Projeto
```
honey-project2/
├── game/
│   ├── audio/               # vazio, aguardando trilha
│   ├── images/
│   │   ├── backgrounds/     # vazio; insira os fundos aqui
│   │   └── characters/      # pastas jade, oliver, gus, mel (insira sprites)
│   ├── options.rpy          # configurações básicas
│   ├── screens.rpy          # telas padrão
│   └── scripts/
│       ├── core/
│       │   ├── config.rpy   # utilitários e definição de personagens
│       │   ├── overworld.rpy# hub de memórias
│       │   └── sprites.rpy  # gera animações automaticamente
│       └── story/
│           └── intro.rpy    # cena inicial
└── README.md
```

## Cenas Importantes
- **Cena inicial (`label start`)**: o Oliver aparece no centro da tela e apresenta o presente, depois salta para o overworld.
- **Overworld (`label overworld_start`)**: Mel recebe o jogador e apresenta um menu com portas para memórias. Labels de memórias já estão criados como placeholders e prontos para expansão.

## Como Rodar o Projeto
1. Instale o [Ren'Py Launcher](https://www.renpy.org/latest.html).
2. Abra o launcher e clique em **Open Project** → selecione a pasta `honey-project2`.
3. Clique em **Launch Project** para iniciar.

## Como Personalizar
- **Adicionar música**: coloque arquivos `.mp3` ou `.ogg` em `game/audio/` e use `play music "audio/nome.ogg"` dentro das cenas.
- **Adicionar cenários**: adicione imagens em `game/images/backgrounds/` e use `scene bg nome_do_background`.
- **Adicionar sprites**: coloque os PNGs recortados em `game/images/characters/<nome>/`; os nomes devem seguir o padrão `<nome>_<direcao>_<frame>.png` (por exemplo, `jade_down_0.png`).
- **Criar novas memórias**: crie arquivos `.rpy` em `game/scripts/story/` e conecte-os no overworld adicionando novos botões ou triggers.

## Próximos Passos Ideais
- Criar CGs personalizados da família.
- Implementar movimento completo no mapa.
- Criar as memórias individuais.
- Inserir trilha sonora escolhida.
- Criar um final especial.

Feito com carinho por Gustavo, Mel, Jade e Oliver. ❤️
