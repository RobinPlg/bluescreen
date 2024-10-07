define b = Character("Blender", color="#fb8500")
define m = Character("Miro", color="#F0C808")
define u = Character("Unity", color="#33415c")
define p = Character("Photoshop", color="#006494")
define u = Character("Utilisateur", color="#df2935")

default b_pass = 0
default m_pass = 0
default u_pass = 0
default p_pass = 0

default b_q1 = 0
default b_q2 = 0

default m_q1 = 0
default m_q2 = 0

default u_q1 = 0
default u_q2 = 0

default p_q1 = 0
default p_q2 = 0

label start :

    u "Argh mon ordinateur a planté ! Je dois trouver qui est responsable."

label taskmanager :

    if b_pass == 1 and m_pass == 1 and u_pass == 1 and p_pass == 1:
        menu:
            "Qui est le fautif ?"
            "Blender":
                "gg wp"
                return
            "Miro":
                "non c'était pas lui  HAHAHAHAHA"
                return
            "Unity":
                "non c'était pas lui  HAHAHAHAHA"
                return
            "Photoshop":
                "non c'était pas lui  HAHAHAHAHA"
                return

    menu:
        "Qui voulez-vous interroger ?"
        "Blender":
            jump blender
        "Miro":
            jump miro
        "Unity": 
            jump unity
        "Photoshop":
            jump photoshop
        

label blender :

    if b_pass == 1:
        u "Je l\'ai déjà interrogé !"
        jump taskmanager
    
    else:
        b "coucou je suis Blender !"
        $ b_pass += 1
        jump taskmanager


label miro :

    if m_pass == 1:
        u "Je l\'ai déjà interrogé !"
        jump taskmanager
    
    else:
        m "coucou je suis Miro !"
        $ m_pass += 1
        jump taskmanager


label unity :
   
    if u_pass == 1:
        u "Je l\'ai déjà interrogé !"
        jump taskmanager
    
    else:
        u "coucou je suis Unity !"
        $ u_pass += 1
        jump taskmanager

label photoshop : 

    if p_pass == 1:
        u "Je l\'ai déjà interrogé !"
        jump taskmanager
    
    else:
        p "coucou je suis Photoshop !"
        $ p_pass += 1
        jump taskmanager