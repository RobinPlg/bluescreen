define b = Character("Blender", color="#fb8500")
define m = Character("Miro", color="#F0C808")
define u = Character("Unity", color="#33415c")
define p = Character("Photoshop", color="#006494")
define ut = Character("Utilisateur", color="#df2935")

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

    ut "Alors, tout à l'heure, mon ordinateur a planté et vous étiez mes 4 applications ouvertes. Je ne sais pas qui a fait planter, mais il faut trouver avant que ça ne réarrive."

label tour1 :

    if b_pass == 1 and m_pass == 1 and u_pass == 1 and p_pass == 1:
        ut "Bien, j'ai intérrogé tout le monde, voyons voir maintenant ce qu'ils pensent les uns des autres."
        jump tour2

    menu:
        "Qui voulez-vous interroger ?"
        "Blender":
            jump blender_t1
        "Miro":
            jump miro_t1
        "Unity": 
            jump unity_t1
        "Photoshop":
            jump photoshop_t1
        

label blender_t1 :

    if b_pass == 1:
        ut "Il m'a dit tout ce qu'il savait."
        jump tour1
        
    else:

        b "Yo meuf ! Bien sûr que je vais t'aider, j'adore t'aider gratuitement tu sais bien."

        menu:
            "Que voulez-vous lui demander ?"
            "As-tu quelque chose à voir là-dedans ?":
                b "Oh, ça m'étonnerait ! En plus j'étais en Eevee et pas en Cycles, alors je peux te faire tourner n'importe quoi sans soucis !"
                if b_q1 < 1:
                    $ b_q1 += 1
                if b_q1 == 1 and b_q2 == 1:
                    if b_pass != 1:
                        $ b_pass = 1    
                jump tour1
                    
            "Tu as vu des éléments suspects chez les autres logiciels ?":
                b "Photoshop se croit intouchable ça me saoule !!! Ah, ces logiciels payants qui pensent qu'ils ne peuvent jamais avoir de problèmes. Et Miro ? Avec tous les rendus que je lui envoie, elle doit en baver."
                if b_q2 < 1:
                    $ b_q2 += 1
                if b_q1 == 1 and b_q2 == 1:
                    if b_pass != 1:
                        $ b_pass = 1
                jump tour1

label miro_t1 :

    if m_pass == 1:
        ut "Il m'a dit tout ce qu'il savait."
        jump tour1
        
    else:

        m "Ok, je vais faire du mieux que je peux mais il va falloir faire vite."

        menu:
            "Que voulez-vous lui demander ?"
            "Tu penses que tu pourrais y être pour quelque chose ?":
                m "Navrée pour ce qui t'est arrivé. Je ne pense pas que ce soit moi étant donné que je tourne sur un serveur en ligne."
                if m_q1 < 1:
                    $ m_q1 += 1
                if m_q1 == 1 and m_q2 == 1:
                    if m_pass != 1:
                        $ m_pass = 1    
                jump tour1
                    
            "Est-ce que tu aurais des pistes sur qui pourrait en être responsable ?":
                m "Je n'aime pas accuser les autres mais en ce moment, Photoshop m'envoie des fichiers si lourds que j'ai du mal à maintenir la cadence. Je crois que Unity, aussi, prend pas mal de place."
                if m_q2 < 1:
                    $ m_q2 += 1
                if m_q1 == 1 and m_q2 == 1:
                    if m_pass != 1:
                        $ m_pass = 1
                jump tour1

label unity_t1 :

    if u_pass == 1:
        ut "Il m'a dit tout ce qu'il savait."
        jump tour1
        
    else:

        u "U-une femme ? Bool fille = t-true ?? J'espère que je pourrais t'aider... moi je-"

        menu:
            "Que voulez-vous lui demander ?"
            "Aurais-tu un rapport avec le crash de mon ordinateur ?":
                u "Euh... j-je... j'étais juste dans ma scène, à faire tourner la dernière animation que m'a envoyé Blender."
                if u_q1 < 1:
                    $ u_q1 += 1
                if u_q1 == 1 and u_q2 == 1:
                    if u_pass != 1:
                        $ u_pass = 1    
                jump tour1
                    
            "Y a-t-il quelqu'un parmi les autres qui pourrait être coupable ?":
                u "Jamais de la vie c'est Miro-chan ! Elle fait toujours tout bien, elle garde toute la pipeline organisée pour moi- euh... pour toi bien sûr. Ça pourrait être moi, j'utilise plus de rame qu'elle. "
                u "Pho-photoshop-sensei, je sais pas, j'ose pas lui parler. Cette baka de Blender refait tout le temps des exports, encore tout à l'heure, elle me sortait une nouvelle version de son animation remplie de n-gons."
                if u_q2 < 1:
                    $ u_q2 += 1
                if u_q1 == 1 and u_q2 == 1:
                    if u_pass != 1:
                        $ u_pass = 1
                jump tour1

label photoshop_t1 :

    if p_pass == 1:
        ut "Il m'a dit tout ce qu'il savait."
        jump tour1
        
    else:

        p "Ne me regarde pas comme ça, on sait tous les deux que ça ne peut pas être moi."

        menu:
            "Que voulez-vous lui demander ?"
            "Est-ce toi qui a fait planter mon ordinateur ?":
                p "Moi ?! Impossible. En tant que leader du marché, je suis évidemment le plus fiable ici. Je peux tout faire et tout soutenir, pas comme ces petits logiciels gratuits de pacotille."
                if p_q1 < 1:
                    $ p_q1 += 1
                if p_q1 == 1 and p_q2 == 1:
                    if p_pass != 1:
                        $ p_pass = 1    
                jump tour1
                    
            "As-tu une idée de qui ça pourrait être ?":
                p "Selon moi, c'est soit Miro, soit Blender mais certainement pas ce gringalet de Unity"
                if p_q2 < 1:
                    $ p_q2 += 1
                if p_q1 == 1 and p_q2 == 1:
                    if p_pass != 1:
                        $ p_pass = 1
                jump tour1

default b_guess_unity = 0
default b_guess_ps = 0

default m_guess_unity = 0
default m_guess_ps = 0

default u_guess_unity = 0
default u_guess_ps = 0

default p_guess_unity = 0
default p_guess_ps = 0

label tour2:

    menu:
        "Qui voulez-vous interroger ?"
        "Blender":
            jump blender_t2
        "Miro":
            jump miro_t2
        "Unity": 
            jump unity_t2
        "Photoshop":
            jump photoshop_t2
        "Je sais qui est le/la coupable !":
            jump guess

label blender_t2:
        
    if b_guess_ps == 1 or b_guess_unity == 1:
        if b_guess_unity == 1:
            b "C'est unity !" 
            jump tour2
        if b_guess_ps == 1:
            b "C'est photoshop !" 
            jump tour2
                
    menu:
        "Que voulez-vous lui demander ?"
        "Tu pense que c'est Unity ?":
            b "Oui"
            $ b_guess_unity += 1
            jump tour2
                            
        "Tu pense que c'est Photoshop ?":
            b "Oui"
            $ b_guess_ps += 1
            jump tour2

label miro_t2:
        
    if m_guess_ps == 1 or m_guess_unity == 1:
        if m_guess_ps == 1:
            m "C'est Photoshop !" 
            jump tour2
        if m_guess_unity == 1:
            m "C'est Unity !" 
            jump tour2
                
    menu:
        "Que voulez-vous lui demander ?"
        "Tu pense que c'est Photoshop ?":
            m "Oui"
            $ m_guess_ps += 1
            jump tour2
                            
        "Tu pense que c'est Unity ?":
            m "Oui"
            $ m_guess_unity += 1
            jump tour2

label unity_t2:
        
    if b_guess_ps == 1 or b_guess_unity == 1:
        if b_guess_unity == 1:
            b "C'est unity !" 
            jump tour2
        if b_guess_ps == 1:
            b "C'est photoshop !" 
            jump tour2
                
    menu:
        "Que voulez-vous lui demander ?"
        "Tu pense que c'est Unity ?":
            b "Oui"
            $ b_guess_unity += 1
            jump tour2
                            
        "Tu pense que c'est Photoshop ?":
            b "Oui"
            $ b_guess_ps += 1
            jump tour2

label photoshop_t2:
        
    if b_guess_ps == 1 or b_guess_unity == 1:
        if b_guess_unity == 1:
            b "C'est unity !" 
            jump tour2
        if b_guess_ps == 1:
            b "C'est photoshop !" 
            jump tour2
                
    menu:
        "Que voulez-vous lui demander ?"
        "Tu pense que c'est Unity ?":
            b "Oui"
            $ b_guess_unity += 1
            jump tour2
                            
        "Tu pense que c'est Photoshop ?":
            b "Oui"
            $ b_guess_ps += 1
            jump tour2

label guess:
    
    menu:
        "Alors, à qui la faute ?"
        "C'est Blender !":
            "gg wp"
            return
        "C'est Miro !":
            "eh non HAHAHAHAHA"
            return
        "C'est Unity !":
            "eh non HAHAHAHAHA"
            return
        "C'est Photoshop !":
            "eh non HAHAHAHAHA"
            return
        "Je veux encore réfléchir.":
            jump tour2