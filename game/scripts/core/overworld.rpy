# Cena do hub de memórias
label overworld_start:
    scene bg overworld
    show mel idle at facing_center

    if persistent.honey_seen_intro:
        m "Bem-vinda ao nosso pequeno mundo de memórias."
    else:
        m "Oi! Vamos explorar juntos."  # fallback se chegar aqui direto

    show screen overworld_menu
    "Use o menu para entrar em uma lembrança." # pausa até escolha
    return

screen overworld_menu():
    modal False
    frame:
        align (0.5, 0.1)
        has vbox
        text "Hub de memórias" size 32
        text "Escolha por onde começar" size 20

    vbox:
        spacing 10
        align (0.5, 0.25)
        textbutton "Nascimento do Oliver" action Jump("memory_oliver_birth")
        textbutton "Momentos especiais da Jade" action Jump("memory_jade_special")
        textbutton "Histórias da família" action Jump("memory_family_story")
        textbutton "Voltar" action Return()

label memory_oliver_birth:
    scene bg overworld
    o "Ainda vamos colocar fotos e animações aqui. Obrigado por jogar um pedacinho!"
    return

label memory_jade_special:
    scene bg overworld
    j "Essa memória será preenchida com histórias da Jade e sua energia incrível."
    return

label memory_family_story:
    scene bg overworld
    g "Logo teremos cenas especiais dessa história."
    return
