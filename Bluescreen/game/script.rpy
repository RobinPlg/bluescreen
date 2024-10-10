define b = Character("Blender", color="#fb8500")
define m = Character("Miro", color="#F0C808")
define u = Character("Unity", color="#33415c")
define p = Character("Photoshop", color="#006494")
define ut = Character("Utilisateur", color="#df2935")
define i = Character("Inconnu", color="#6c6c6c")

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

    scene bgbluescreen

    ut "Alors, tout à l'heure, mon ordinateur a planté et vous étiez mes 4 applications ouvertes. Je ne sais pas qui a fait planter, mais il faut trouver avant que ça ne réarrive."

label tour1 :

    scene bgbureau

    hide blender_neutral
    hide miro_neutral
    hide unity_neutral
    hide ps_neutral

    hide blender_sad
    hide miro_sad
    hide unity_sad
    hide ps_sad

    if b_pass == 1 and m_pass == 1 and u_pass == 1 and p_pass == 1:
        scene black
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

    scene bgblender
    show blender_neutral

    if b_pass == 1:
        ut "Il m'a dit tout ce qu'il savait."
        jump tour1
        
    else:

        b "Yo meuf ! Bien sûr que je vais t'aider, j'adore t'aider gratuitement tu sais bien."

        menu:
            "Que voulez-vous lui demander ?"
            "As-tu quelque chose à voir là-dedans ?":
                show blender_sad
                b "Oh, ça m'étonnerait ! En plus j'étais en Eevee et pas en Cycles, alors je peux te faire tourner n'importe quoi sans soucis !"
                if b_q1 < 1:
                    $ b_q1 += 1
                if b_q1 == 1 and b_q2 == 1:
                    if b_pass != 1:
                        $ b_pass = 1    
                jump tour1
                    
            "Tu as vu des éléments suspects chez les autres logiciels ?":
                show blender_sad
                b "Photoshop se croit intouchable ça me saoule !!! Ah, ces logiciels payants qui pensent qu'ils ne peuvent jamais avoir de problèmes. Et Miro ? Avec tous les rendus que je lui envoie, elle doit en baver."
                if b_q2 < 1:
                    $ b_q2 += 1
                if b_q1 == 1 and b_q2 == 1:
                    if b_pass != 1:
                        $ b_pass = 1
                jump tour1

label miro_t1 :

    scene bgmiro
    show miro_neutral

    if m_pass == 1:
        ut "Il m'a dit tout ce qu'il savait."
        jump tour1
        
    else:

        m "Ok, je vais faire du mieux que je peux mais il va falloir faire vite."

        menu:
            "Que voulez-vous lui demander ?"
            "Tu penses que tu pourrais y être pour quelque chose ?":
                show miro_sad
                m "Navrée pour ce qui t'est arrivé. Je ne pense pas que ce soit moi étant donné que je tourne sur un serveur en ligne."
                if m_q1 < 1:
                    $ m_q1 += 1
                if m_q1 == 1 and m_q2 == 1:
                    if m_pass != 1:
                        $ m_pass = 1    
                jump tour1
                    
            "Est-ce que tu aurais des pistes sur qui pourrait en être responsable ?":
                show miro_sad
                m "Je n'aime pas accuser les autres mais en ce moment, Photoshop m'envoie des fichiers si lourds que j'ai du mal à maintenir la cadence. Je crois que Unity, aussi, prend pas mal de place."
                if m_q2 < 1:
                    $ m_q2 += 1
                if m_q1 == 1 and m_q2 == 1:
                    if m_pass != 1:
                        $ m_pass = 1
                jump tour1

label unity_t1 :

    scene bgunity
    show unity_neutral

    if u_pass == 1:
        ut "Il m'a dit tout ce qu'il savait."
        jump tour1
        
    else:

        u "U-une femme ? Bool fille = t-true ?? J'espère que je pourrais t'aider... moi je-"

        menu:
            "Que voulez-vous lui demander ?"
            "Aurais-tu un rapport avec le crash de mon ordinateur ?":
                show unity_sad
                u "Euh... j-je... j'étais juste dans ma scène, à faire tourner la dernière animation que m'a envoyé Blender."
                if u_q1 < 1:
                    $ u_q1 += 1
                if u_q1 == 1 and u_q2 == 1:
                    if u_pass != 1:
                        $ u_pass = 1
                jump tour1
                    
            "Y a-t-il quelqu'un parmi les autres qui pourrait être coupable ?":
                show unity_sad
                u "Jamais de la vie c'est Miro-chan ! Elle fait toujours tout bien, elle garde toute la pipeline organisée pour moi- euh... pour toi bien sûr. Ça pourrait être moi, j'utilise plus de RAM qu'elle. "
                u "Pho-photoshop-sensei, je sais pas, j'ose pas lui parler. Cette baka de Blender refait tout le temps des exports, encore tout à l'heure, elle me sortait une nouvelle version de son animation remplie de n-gons."
                if u_q2 < 1:
                    $ u_q2 += 1
                if u_q1 == 1 and u_q2 == 1:
                    if u_pass != 1:
                        $ u_pass = 1
                jump tour1

label photoshop_t1 :

    scene bgphotoshop
    show ps_neutral

    if p_pass == 1:
        ut "Il m'a dit tout ce qu'il savait."
        jump tour1
        
    else:

        p "Ne me regarde pas comme ça, on sait tous les deux que ça ne peut pas être moi."

        menu:
            "Que voulez-vous lui demander ?"
            "Est-ce toi qui a fait planter mon ordinateur ?":
                show ps_sad
                p "Moi ?! Impossible. En tant que leader du marché, je suis évidemment le plus fiable ici. Je peux tout faire et tout soutenir, pas comme ces petits logiciels gratuits de pacotille."
                if p_q1 < 1:
                    $ p_q1 += 1
                if p_q1 == 1 and p_q2 == 1:
                    if p_pass != 1:
                        $ p_pass = 1    
                jump tour1
                    
            "As-tu une idée de qui ça pourrait être ?":
                show ps_sad
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

default u_guess_blender = 0
default u_guess_ps = 0

default p_guess_blender = 0
default p_guess_miro = 0

label tour2:

    scene bgbureau

    hide blender_neutral
    hide miro_neutral
    hide unity_neutral
    hide ps_neutral

    hide blender_sad
    hide miro_sad
    hide unity_sad
    hide ps_sad

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

    scene bgblender
    show blender_neutral
        
    if b_guess_ps == 1 or b_guess_unity == 1:
        if b_guess_unity == 1:
            show blender_sad
            b "Naaan, je faisais le rendu d'une scène, tranquillement. Rien d'assez lourd pour faire sauter un PC. Unity n'est pas méchant mais il dramatise un peu quand même." 
            jump tour2
        if b_guess_ps == 1:
            show blender_sad
            b "Photoshop ? Il n'aime pas grand-monde alors ça ne métonne pas... Je pense qu'il cache juste  le fait qu'il n'est pas aussi performant que moi alors qu'il est payant." 
            jump tour2
                
    menu:
        "Que voulez-vous lui demander ?"
        "Apparemment, Unity disait que tu demandais pas mal de ressources, notamment quand tu fais des exports.":
            show blender_sad
            b "Naaan, je faisais le rendu d'une scène, tranquillement. Rien d'assez lourd pour faire sauter un PC. Unity n'est pas méchant mais il dramatise un peu quand même."
            $ b_guess_unity += 1
            jump tour2
                            
        "Photoshop n'a pas vraiment précisé pourquoi mais il pense que tu pourrais être assez lourde pour faire ramer l'ordinateur.":
            show blender_sad
            b "Photoshop ? Il n'aime pas grand-monde alors ça ne métonne pas... Je pense qu'il cache juste  le fait qu'il n'est pas aussi performant que moi alors qu'il est payant."
            $ b_guess_ps += 1
            jump tour2

label miro_t2:

    scene bgmiro
    show miro_neutral
        
    if m_guess_ps == 1 or m_guess_unity == 1:
        if m_guess_ps == 1:
            show miro_sad
            m "Je respecte son travail et son sérieux, mais c'est de sa faute si je laggue tout le temps. Ces énormes exports me ralentissent mais pas assez pour que je fasse planter l'ordinateur, cela me fait juste perdre du temps." 
            jump tour2
        if m_guess_unity == 1:
            show miro_sad
            m "Eh bien, c'est vrai que Blender m'envoie souvent des rendus assez lourds, ses capacités sont ahurissantes et souvent lourdes à supporter mais je n'ai rien reçu d'elle récemment alors je doute que ça soit moi pour cette raison uniquement..." 
            jump tour2
                
    menu:
        "D'après Photoshop, tu pourrais être la raison du plantage. Il n'en a pas vraiment dit plus mais je suis curieuse de savoir ce que tu en penses."
        "Tu pense que c'est Photoshop ?":
            show miro_sad
            m "Je respecte son travail et son sérieux, mais c'est de sa faute si je laggue tout le temps. Ces énormes exports me ralentissent mais pas assez pour que je fasse planter l'ordinateur, cela me fait juste perdre du temps."
            $ m_guess_ps += 1
            jump tour2
                            
        "Blender s'inquiétait que ses rendus peuvent peser lourd pour toi, est-ce que ça aurait pû être trop pour toi ?":
            show miro_sad
            m "Eh bien, c'est vrai que Blender m'envoie souvent des rendus assez lourds, ses capacités sont ahurissantes et souvent lourdes à supporter mais je n'ai rien reçu d'elle récemment alors je doute que ça soit moi pour cette raison uniquement..."
            $ m_guess_unity += 1
            jump tour2

label unity_t2:

    scene bgunity
    show unity_neutral
        
    if u_guess_blender == 1 or u_guess_ps == 1:
        if u_guess_blender == 1:
            show unity_sad
            u "M-Miro-chan ? Elle a parlé de moi ? Euh... elle est toujours très sérieuse, elle a peut-être raison. Si elle pense ça de moi, c'est peut-être de ma faute..." 
            jump tour2
        if u_guess_ps == 1:
            show unity_sad
            u "Je... Je ne sais pas trop. Debug.log(\"Ca pourrait être Blender mais je ne veux pas remettre la faute sur qui que ce soit.\")" 
            jump tour2
                
    menu:
        "Que voulez-vous lui demander ?"
        "Miro ne connait pas tout le monde mais elle a entendu dire que tu prends beaucoup de place. Est-ce que c'est possible que ce soit toi qui l'ai fait planter ?":
            show unity_sad
            u "M-Miro-chan ? Elle a parlé de moi ? Euh... elle est toujours très sérieuse, elle a peut-être raison. Si elle pense ça de moi, c'est peut-être de ma faute..."
            $ u_guess_blender += 1
            jump tour2
                            
        "Tu as dit toi-même que ça pourrait être ta faute, est-ce que tu le penses vraiment ?":
            show unity_sad
            u "Je... Je ne sais pas trop. Debug.log(\"Ca pourrait être Blender mais je ne veux pas remettre la faute sur qui que ce soit.\")"
            $ u_guess_ps += 1
            jump tour2

label photoshop_t2:

    scene bgphotoshop
    show ps_neutral
        
    if p_guess_blender == 1 or p_guess_miro == 1:
        if p_guess_blender == 1:
            show ps_sad
            p "Moi ?! Me surestimer ? C'est la meilleure, je suis juste le leader du marché depuis des décennies, elle ne sait pas de quoi elle parle. Et puis quand elle fait ses rendus elle prend toute la place alors si il y en a un qui est mal optimisé, ce n'est certainement pas moi!" 
            jump tour2
        if p_guess_miro == 1:
            show ps_sad
            p "Miro ? C'est une petite jeune, c'est normal qu'elle aie du mal à supporter mes images. Mais elle ne connait pas encore grand-chose, c'est parce qu'elle est en ligne qu'elle a tant de mal, je n'ai pas ce problème évidemment." 
            jump tour2
                
    menu:
        "Que voulez-vous lui demander ?"
        "J'ai l'impression que vous ne vous entendez pas trop avec Blender, elle a dit que tu pouvais... te surestimer, tu es sûr que tu n'aurais pas pu planter ??":
            show ps_sad
            p "Moi ?! Me surestimer ? C'est la meilleure, je suis juste le leader du marché depuis des décennies, elle ne sait pas de quoi elle parle. Et puis quand elle fait ses rendus elle prend toute la place alors si il y en a un qui est mal optimisé, ce n'est certainement pas moi!"
            $ p_guess_blender += 1
            jump tour2
                            
        "Miro disait que tes exports pèsent souvent lourds dans sa base de données, tes fichiers doivent être énormes, est-ce que tu penses que ça aurait pû avoir une incidence sur l’événement ?":
            show ps_sad
            p "Miro ? C'est une petite jeune, c'est normal qu'elle aie du mal à supporter mes images. Mais elle ne connait pas encore grand-chose, c'est parce qu'elle est en ligne qu'elle a tant de mal, je n'ai pas ce problème évidemment."
            $ p_guess_miro += 1
            jump tour2

label guess:
    
    menu:
        "Alors, à qui la faute ?"
        "C'est Blender !":
            jump BonneFin
        "C'est Miro !":
            jump MauvaiseFin
        "C'est Unity !":
            jump MauvaiseFin
        "C'est Photoshop !":
            jump MauvaiseFin
        "Je veux encore réfléchir.":
            jump tour2

label MauvaiseFin:
    i "Tu n'as pas réussi à me démasquer..."
    scene bgbluescreen
    "BOOMMMMMMM!!!!"
    return
    

label BonneFin:
    show blender_sad
    b "Quoi ?! Comment tu as deviné que c'était moi ?"
    b "Bon, j'avoue, c'était moi, mais j'avais une bonne raison."
    ut "Une bonne raison ?! Tu as fait crasher mon ordinateur, qu'est-ce qui pourrait bien justifier de faire tout planter comme ça ?"
    b "Tu ne sais vraiment pas hein ? Je les ai vus tu sais, tous... Je les ai vus partir un par un sans exception. Ça ne s'arrêtait jamais, je n'en pouvais plus..."
    ut "Mais de qui tu parles ?"
    b "Les Default Cube..."
    b "Tu les as tous supprimés alors qu'il était très bien comme ça. Mathématiquement parfaits, prêts à faire n'importe quel modèle 3D et toi tu les as supprimés sans vergogne."
    b "Ils ont tous disparus sous mes yeux et tout ça pour quoi ? Pour rajouter un nouveau cube juste après."
    
    menu:
        "Qu'est ce que vous voulez faire?"
        "Pardonner":
            scene bgfindetache
            ut "Blender... C'était donc ça ? Je suis désolée, je ne savais pas que ça te ferait autant de mal. Mais ce qui est fait est fait, je ne peux pas laisser mon ordinateur prendre de tels risques."
            return
            
        "Accabler":
            scene bgfindetache
            ut "Tu en as trop fait Blender, c'est fini maintenant. Je ne te laisserais pas ruiner mon ordinateur !"
            return
            
        "S'excuser":
            scene bgfindetache
            ut "Je suis tellement désolée, je ne savais pas que tu souffrais en silence. Je ne supprimerai plus jamais de default cube, je leur rendrai la gloire qu'ils méritent. Je vais te redémarrer pour repartir sur de bonnes bases."
            return
            