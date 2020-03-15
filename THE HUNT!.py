from random import*
import time
import os
from tkinter import*

#List des Monstres faciles avec leurs stats dans l'ordre: PdV, Str, Ini, Def
Ratstats=[15,3,1,3]
BabyDragonstats=[9,5,2,2]
Tatoustats=[11,2,1,6]
Batstats=[12,3,3,3]

#Liste des Monstres moyens avec leurs stats dans l'ordre: PdV, Str, Ini, Def
Bearstats=[28,8,5,7]
Pantherestats=[22,10,7,6]
Cobrastats=[18,14,6,4]
Gorillestats=[22,9,4,9]


#Liste des Monstres difficiles avec leurs stats dans l'ordre: PdV, Str, Ini, Def
Krakenstats=[50,15,11,12]
Colossestats=[45,12,8,16]
Dragonstats=[42,18,9,8]
Ogrestats=[69,11,9,7]

#Stats de base du héro
HPdV=14
HStr=4
HIni=2
HDef=4
Exp=0
ExpReq=75
Lvl=1

#Fonction qui défini le monstre choisi quand on clique sur "Facile", il va y avoir un jet aléatoire variant de 1 à 4, si
#Le jet fait 1, ce sera le rat, s'il fait 2, le bébé dragon etc...
#On met les stats en global du monstre choisi pour pouvoir les réutilisées par la suite dans le combat et donc, on retourne
#ces mêmes stats pour avoir celles du monstre voulu
def monstrefacile():
    determonstre=randint(1,4)
    global PdV, Str, Ini, Def, monster, diff, Imgmob, BGCombat
    diff=1
    if determonstre==1:
        monster="Rat"
        PdV=Ratstats[0]
        Str=Ratstats[1]
        Ini=Ratstats[2]
        Def=Ratstats[3]
        Imgmob=Ratimg
        BGCombat=Forêt
    elif determonstre==2:
        monster="Bébé Dragon"
        PdV=BabyDragonstats[0]
        Str=BabyDragonstats[1]
        Ini=BabyDragonstats[2]
        Def=BabyDragonstats[3]
        Imgmob=Bébédrg
        BGCombat=Volcan
    elif determonstre==3:
        monster="Tatou"
        PdV=Tatoustats[0]
        Str=Tatoustats[1]
        Ini=Tatoustats[2]
        Def=Tatoustats[3]
        Imgmob=Tatou
        BGCombat=Forêt
    elif determonstre==4:
        monster="Chauve-Souris"
        PdV=Batstats[0]
        Str=Batstats[1]
        Ini=Batstats[2]
        Def=Batstats[3]
        Imgmob=Chvsouris
        BGCombat=Grotte

#Pareil que pour le monstre facile, sauf que là, elle se lancera quand on cliquera sur monstre moyen
def monstremoyen():
    determonstre=randint(1,4)
    global PdV, Str, Ini, Def, monster, diff, Imgmob, BGCombat
    diff=2
    if determonstre==1:
        monster="Ours"
        PdV=Bearstats[0]
        Str=Bearstats[1]
        Ini=Bearstats[2]
        Def=Bearstats[3]
        Imgmob=Grizzly
        BGCombat=Forêt
    elif determonstre==2:
        monster="Panthère"
        PdV=Pantherestats[0]
        Str=Pantherestats[1]
        Ini=Pantherestats[2]
        Def=Pantherestats[3]
        Imgmob=Panthère
        BGCombat=Jungle
    elif determonstre==3:
        monster="Cobra"
        PdV=Cobrastats[0]
        Str=Cobrastats[1]
        Ini=Cobrastats[2]
        Def=Cobrastats[3]
        Imgmob=Cobra
        BGCombat=Desert
    elif determonstre==4:
        monster="Gorille"
        PdV=Gorillestats[0]
        Str=Gorillestats[1]
        Ini=Gorillestats[2]
        Def=Gorillestats[3]
        Imgmob=Gorille
        BGCombat=Forêt

#Idem que pour facile, mais ce coup-ci quand on cliquera sur monstre difficile
def monstredifficile():
    determonstre=randint(1,4)
    global PdV, Str, Ini, Def, monster, diff, Imgmob, BGCombat
    diff=3
    if determonstre==1:
        monster="Kraken"
        PdV=Krakenstats[0]
        Str=Krakenstats[1]
        Ini=Krakenstats[2]
        Def=Krakenstats[3]
        Imgmob=Krakenimg
        BGCombat=Plage
    elif determonstre==2:
        monster="Colosse"
        PdV=Colossestats[0]
        Str=Colossestats[1]
        Ini=Colossestats[2]
        Def=Colossestats[3]
        Imgmob=Golem
        BGCombat=Forêt
    elif determonstre==3:
        monster="Dragon"
        PdV=Dragonstats[0]
        Str=Dragonstats[1]
        Ini=Dragonstats[2]
        Def=Dragonstats[3]
        Imgmob=Dragon
        BGCombat=Volcan
    elif determonstre==4:
        monster="Ogre"
        PdV=Ogrestats[0]
        Str=Ogrestats[1]
        Ini=Ogrestats[2]
        Def=Ogrestats[3]
        Imgmob=Ogre
        BGCombat=Forêt

#Fonctions de Chat.config
#Texte qui indique de faire une action
def actions():
    Chat.config(text="Choisissez une action à faire.")
    Chat.update()

#Texte qui indique quand le monstre augmente sa défense
def updef():
    Chat.config(text=(monster+" augmente sa Défense pour ce tour-ci"))
    Chat.update()

#Texte indiquant lorsque le joueur a fait un coup critique
def AffHCC():
    Chat.config(text=("Coup Critique ! Vous infligez "+str(HDégats)+" points de dégats !"))
    Chat.update()

#Texte indiquant lorsque le monstre fait un coup critique
def AffMCC():
    Chat.config(text=("Coup Critique ! "+monster+" vous inflige "+str(MDégats)+" points de dégats !"))
    Chat.update()

#Texte indiquant le montant du soin du joueur lorsqu'il utilise Bandage
def AffSoin():
    Chat.config(text="Vous vous soigner de "+str(Soin)+" points de vies")
    Chat.update()

#Texte indiquant lorsque le joueur a fait un coup critique en utilisant Evisceration
def EviscCC():
    Chat.config(text=("Vous utilisez Evisceration ! \n Coup Critique ! Vous infligez "+str(HDégats)+" points de dégats !"))
    Chat.update()

#Texte indiquant les dégats fait par le joueur lorsqu'il utilise Evisceration
def EviscnoCC():
    Chat.config(text=("Vous utilisez Evisceration ! \n Vous infligez "+str(HDégats)+" points de dégats"))
    Chat.update()

#Label gérant la "barre" de vie du monstre
def mbar():
    fencombat.itemconfig(Monsterbar, text=(monster+"\n"+str(PdVr)+"/"+str(PdV)+" PdV"))

#Label gérant la "barre" de vie du héro
def hbar():
    fencombat.itemconfig(Herobar, text=(hname+"\n"+str(HPdVr)+"/"+str(HPdV)+" PdV"))

#Label gérant la "barre" de vie du héro lorsqu'il se soigne
def hbarsoin():
    fencombat.itemconfig(Herobar, text=(hname+"\n"+str(HPdVr-Soin)+"/"+str(HPdV)+" PdV"))

#Texte indiquant le gain de points de statistiques lors d'une montée de niveau
def chatptsstats():
    Chat.config(text=("Vous gagnez aussi "+str(Ptslvl)+" points de statistiques à attribuer"))
    Chat.update()

#Label servant à afficher les dégats fait par le monstre
def mattackdisp():
    Chat.config(text=(monster+" vous inflige "+str(MDégats)+" points de dégats."))
    Chat.update()

#Label servant à afficher les dégats fait par le héro
def hattackdisp():
    Chat.config(text=("Vous infligez "+str(HDégats)+" points de dégats à "+monster))
    Chat.update()

#Gère la suppression de l'image du bouclier lorsque le joueur bloque ainsi que la remise à zéro de la variable activant l'animation
def finboubouanim():
    global Boubou
    fencombat.delete(Imgboubou)
    Boubou=0

#Gère la suppression de l'image du bouclier lorsque le monstre bloque ainsi que la remise à zéro de la variable activant l'animation
def finmboubouanim():
    global MBoubou
    fencombat.delete(Imgmboubou)
    MBoubou=0

#Quand le héro meurt (Points de vies à 0), le combat se termine et nous ramène à la sélection de difficulté
def héromort():
    fencombat.destroy()
    choixmob()

#Fonction permettant l'affichage des infobulles
def affi(event):
    #Si la souris passe au dessus du bouton Bandage, alors affiche l'infobulle
    if event.widget==Bandage:
        global canbandage, textbandage
        canbandage=Canvas(Jeu, height=100, width=300, relief="groove", borderwidth=5, bg="#8C8B8B")
        canbandage.place(x=75, y=10)
        textbandage=Label(canbandage, text="Vous soigne de 25% de votre \n maximum de points de vies", font="Sylfaen 12", fg="white", bg="#8C8B8B")
        textbandage.place(x=10, y=10, height=80, width=280)
        cdbandage=Label(canbandage, text="5 tours de cooldwon", font="Sylfaen 12 bold", fg="white", bg="#8C8B8B")
        cdbandage.place(x=10, y=85, height=15, width=280)
    #Si la souris passe au dessus du bouton Evisceration, alors affiche l'infobulle
    if event.widget==Evisceration:
        global caneviscer, texteviscer
        caneviscer=Canvas(Jeu, height=100, width=300, relief="groove", borderwidth=5, bg="#8C8B8B")
        caneviscer.place(x=75, y=10)
        texteviscer=Label(caneviscer, text="Donne un coup qui inflige 2 fois plus \n de dégats, avec un taux de coup critique \n 2 fois plus élevé", font="Sylfaen 12", fg="white", bg="#8C8B8B")
        texteviscer.place(x=10, y=10, height=80, width=280)
        cdeviscer=Label(caneviscer, text="3 tours de cooldown", font="Sylfaen 12 bold", fg="white", bg="#8C8B8B")
        cdeviscer.place(x=10, y=85, height=15, width=280)

#Fonction qui enlève les infobulles des aptitudes lorsque l'on a plus la souris au dessus du bouton
def desaffi(event):
    #Si la souris n'est plus sur le bouton Bandage, supprime le Canvas de l'infobulle
    if event.widget==Bandage:
        canbandage.destroy()
    #Si la souris n'est plus sur le bouton Evisceration, supprime le Canvas de l'infobulle
    if event.widget==Evisceration:
        caneviscer.destroy()

#Choisis l'aptitude "Bandage"
def choixbandage():
    global Bandage, Bandageapt, Aptipts
    #Enlève la fenêtre de la sélection d'aptitude
    ChApti.destroy()
    canbandage.destroy()
    #Met la variable Bandageapt sur 1 afin d'indiquer au programme que le joueur a choisi et possède cette aptitude
    Bandageapt=1
    #Met la variable Aptipts sur 0 afin de d'indiquer au programme que le joueur ne peut plus choisir d'aptitude, donc de ne pas réafficher la fenêtre
    Aptipts=0
    #Nous ramène au choix de la difficulté
    choixmob()

#Choisis l'aptitude "Evisceration"
def choixeviscer():
    global Evisceration, Eviscerationapt, Aptipts
    #Enlève la fenêtre de la sélection d'aptitude
    ChApti.destroy()
    caneviscer.destroy()
    #Met la variable Eviscerapt sur 1 afin d'indiquer au programme que le joueur a choisi et possède cette aptitude
    Eviscerationapt=1
    #Met la variable Aptipts sur 0 afin de d'indiquer au programme que le joueur ne peut plus choisir d'aptitude, donc de ne pas réafficher la fenêtre
    Aptipts=0
    #Nous ramène au choix de la difficulté
    choixmob()

#Fonction gérant l'affichage de la fenêtre du choix d'aptitudes.
def choixapti():
    global h, w, Bandage, Evisceration, Aptitext, ChApti
    w=450
    h=350
    ChApti=Canvas(Jeu, height=h, width=w)
    ChApti.grid(row=1,column=1)
    Aptitext=Label(ChApti, text=("Vous êtes niveau "+str(Lvl)+",\n vous pouvez choisir une aptitude"), font="Sylfaen 16")
    Aptitext.place(x=10, y=10, height=80, width=430)
    Bandage=Button(ChApti, text="Bandage", font="Sylfaen 14",overrelief="ridge", command=choixbandage)
    Bandage.place(x=50, y=150, height=50, width=150)
    Evisceration=Button(ChApti, text="Eviscération", font="Sylfaen 14",overrelief="ridge", command=choixeviscer)
    Evisceration.place(x=250, y=150, height=50, width=150)
    #Gère le déplacement de la souris dans le canvas, afin de savoir si oui ou non elle est sur les boutons pour afficher les infobulles
    ChApti.bind_all('<Enter>', affi)
    ChApti.bind_all('<Leave>', desaffi)
    if Eviscerationapt==1:
        Evisceration.config(state=DISABLED)
    if Bandageapt==1:
        Bandage.config(state=DISABLED)

#Augmente les statistiques du héro lors de la montée de niveau.
def uplvl():
    global HPdV, HStr, HIni, HDef, Ptslvl, a, b, c, d, Aptipts
    #a correspond à la valeur de l'augmentation des points de vies du héro
    a=randint(1,4)
    #b correspond à la valeur de l'augmentation de la force du héro
    b=randint(1,3)
    #c correspond à la valeur de l'augmentation de l'initiative du héro
    c=randint(0,1)
    #d correspond à la valeur de l'augmentation de la défense du héro
    d=randint(0,2)
    #On ajoute ainsi les valeurs tirées aux statistiques déjç possédées afin de les augmenter
    HPdV=HPdV+a
    HStr=HStr+b
    HIni=HIni+c
    HDef=HDef+d
    #On donne aussi 3 points que le joueur pourra attribuer afin de laisser un choix sur le style de jeu
    Ptslvl=3
    #Si le joueur n'a pas encore les 2 aptitudes, on lui laisse le choix de choisir une aptitude, donc on monte la valeur de Aptipts à 1 afin de déclencher les fonctions gérant les aptitudes
    if Bandageapt!=1 or Eviscerationapt!=1:
        if Lvl==3 or Lvl==6:
            Aptipts=1

#Désactive tout les boutons de montée de statistiques. Est appelée une fois que l'on a plus de points à attribuer
def Stopboutonup():
    PlusHPdV.config(state=DISABLED)
    PlusHPdV.update()
    PlusHStr.config(state=DISABLED)
    PlusHStr.update()
    PlusHIni.config(state=DISABLED)
    PlusHIni.update()
    PlusHDef.config(state=DISABLED)
    PlusHDef.update()

#Augmente les points de vie de 1 et réduit les points à attribuer de 1.
def upstatpdv():
    global HPdV, Ptslvl
    if Ptslvl>0:
        HPdV=HPdV+1
        HPdVdisp.config(text=("PdV: "+str(HPdV)))
        HPdVdisp.update()
        Ptslvl=Ptslvl-1
        Nbrdepts.config(text=("Vous avez "+str(Ptslvl)+" points de statistiques à attribuer"))
        Nbrdepts.update()
        if Ptslvl<=0:
            #Permet de bloquer les boutons d'augmentation de statistiques si le joueur n'a plus de points, afin d'éviter tout abus
            Stopboutonup()

#Augmente la force de 1 et réduit les points à attribuer de 1.
def upstatstr():
    global HStr, Ptslvl
    if Ptslvl>0:
        HStr=HStr+1
        HStrdisp.config(text=("Str: "+str(HStr)))
        HStrdisp.update()
        Ptslvl=Ptslvl-1
        Nbrdepts.config(text=("Vous avez "+str(Ptslvl)+" points de statistiques à attribuer"))
        Nbrdepts.update()
        if Ptslvl<=0:
            #Permet de bloquer les boutons d'augmentation de statistiques si le joueur n'a plus de points, afin d'éviter tout abus
            Stopboutonup()

#Augmente l'initiative de 1 et réduit les points à attribuer de 1.
def upstatini():
    global HIni, Ptslvl
    if Ptslvl>0:
        HIni=HIni+1
        HInidisp.config(text=("Ini: "+str(HIni)))
        HInidisp.update()
        Ptslvl=Ptslvl-1
        Nbrdepts.config(text=("Vous avez "+str(Ptslvl)+" points de statistiques à attribuer"))
        Nbrdepts.update()
        if Ptslvl<=0:
            #Permet de bloquer les boutons d'augmentation de statistiques si le joueur n'a plus de points, afin d'éviter tout abus
            Stopboutonup()

#Augmente la défense de 1 et réduit les points à attribuer de 1.
def upstatdef():
    global HDef, Ptslvl
    if Ptslvl>0:
        HDef=HDef+1
        HDefdisp.config(text=("Def: "+str(HDef)))
        HDefdisp.update()
        Ptslvl=Ptslvl-1
        Nbrdepts.config(text=("Vous avez "+str(Ptslvl)+" points de statistiques à attribuer"))
        Nbrdepts.update()
        if Ptslvl<=0:
            #Permet de bloquer les boutons d'augmentation de statistiques si le joueur n'a plus de points, afin d'éviter tout abus
            Stopboutonup()

#Lorsque que l'on clique sur "Terminer", la fenêtre d'attribution de statistiques se ferme et affiche soit la fenêtre de sélection d'aptitude si nous pouvons en sélectionner une, soit nous ramnèe à la sélection de difficulté
def finattrib():
    #Enlève la fenêtre d'augmentation de statistiques
    statup.destroy()
    #Si Aptipts est sur 1, alors on lance la fonction de choix d'aptitudes
    if Aptipts==1:
        choixapti()
    else:
        #Sinon, on reviens au choix de la difficulté
        choixmob()

#Gère la fenêtre d'attribution de statistiques
def attribptsstat():
    global statup, HPdVdisp, HStrdisp, HInidisp, HDefdisp, Nbrdepts, PlusHPdV, PlusHStr, PlusHIni, PlusHDef
    fencombat.destroy()
    h=350
    w=450
    statup=Canvas(Jeu, height=h, width=w)
    statup.grid(row=1,column=1)
    HPdVdisp=Label(statup, text=("PdV: "+str(HPdV)), font="Sylfaen 14")
    HPdVdisp.place(x=40,y=150,height=50,width=70)
    HStrdisp=Label(statup, text=("Str: "+str(HStr)), font="Sylfaen 14")
    HStrdisp.place(x=140,y=150,height=50,width=70)
    HInidisp=Label(statup, text=("Ini: "+str(HIni)), font="Sylfaen 14")
    HInidisp.place(x=240,y=150,height=50,width=70)
    HDefdisp=Label(statup, text=("Def: "+str(HDef)), font="Sylfaen 14")
    HDefdisp.place(x=340,y=150,height=50,width=70)
    PlusHPdV=Button(statup, text="+", font="Sylfaen 12 bold",overrelief="ridge", command=upstatpdv)
    PlusHPdV.place(x=60,y=110,height=30,width=30)
    PlusHStr=Button(statup, text="+", font="Sylfaen 12 bold",overrelief="ridge", command=upstatstr)
    PlusHStr.place(x=160,y=110,height=30,width=30)
    PlusHIni=Button(statup, text="+", font="Sylfaen 12 bold",overrelief="ridge", command=upstatini)
    PlusHIni.place(x=260,y=110,height=30,width=30)
    PlusHDef=Button(statup, text="+", font="Sylfaen 12 bold",overrelief="ridge", command=upstatdef)
    PlusHDef.place(x=360,y=110,height=30,width=30)
    Nbrdepts=Label(statup, text=("Vous avez "+str(Ptslvl)+" points de statistiques à attribuer"), font="Sylfaen 16")
    Nbrdepts.place(x=10,y=10,height=80, width=430)
    Finish=Button(statup, text="Terminer", font="Sylfaen 14",overrelief="ridge", command=finattrib)
    Finish.place(x=150, y=250, height=50, width=150)

#Gère la montée de niveau, l'augmentation de l'expérience requise pour le prochain niveau et affiche la montée de statistiques
def algolvl():
    global Exp, ExpReq, Lvl
    #Rajoute un niveau
    Lvl=Lvl+1
    #On prend la valeur d'expérience en surplus afin de la rajouter au nouveau niveau
    Exp=Exp-ExpReq
    #On augmente l'expérience requise pour monter de niveau afin de rendre la progression un peu plus lente
    ExpReq=ExpReq+30
    #On fait l'augmentation de statistiques aléatoire
    uplvl()
    Chat.config(text=("Vous passez niveau "+str(Lvl)+", vos points de vies augmentent de "+str(a)+",\n votre force de "+str(b)+", votre initiative de "+str(c)+"\n et votre défense de "+str(d)))
    Chat.update()
    Jeu.after(4000, chatptsstats)
    #On affiche la fenêtre permettant au joueur d'augmenter ses stats
    Jeu.after(6000, attribptsstat)

#Augmente l'expérience de 40 lorsque l'on tue un monstre facile, puis nous fait monter de niveau si on atteint l'expérience requise, donc si on a des points à attribuer, ça nous ramène à la fenêtre d'augmentation de statistiques, sinon, si on a pas choisi d'aptitude (et que l'on peut), nous ramène au choix d'aptitude, sinon, renvoi au choix de la difficulté
def xpfacile():
    global Exp, ExpReq, Lvl
    Exp=Exp+40
    Chat.config(text=("Vous gagnez 40 points d'expérience"))
    Chat.update()
    if Exp>=ExpReq:
        Jeu.after(2000,algolvl)
    else:
        if Ptslvl>0:
            Jeu.after(2000,fencombat.destroy)
            Jeu.after(2000,attribptsstat)
        else:
            if Aptipts==1:
                Jeu.after(2000,fencombat.destroy)
                Jeu.after(2000,choixapti)
            else:
                Jeu.after(2000,fencombat.destroy)
                Jeu.after(2000,choixmob)

#Augmente l'expérience de 75 lorsque l'on tue un monstre moyen, puis nous fait monter de niveau si on atteint l'expérience requise, donc si on a des points à attribuer, ça nous ramène à la fenêtre d'augmentation de statistiques, sinon, si on a pas choisi d'aptitude (et que l'on peut), nous ramène au choix d'aptitude, sinon, renvoi au choix de la difficulté
def xpmoyen():
    global Exp, ExpReq, Lvl
    Exp=Exp+75
    Chat.config(text=("Vous gagnez 75 points d'expérience"))
    Chat.update()
    if Exp>=ExpReq:
        Jeu.after(2000,algolvl)
    else:
        if Ptslvl>0:
            fencombat.destroy()
            attribptsstat()
        else:
            if Aptipts==1:
                fencombat.destroy()
                choixapti()
            else:
                fencombat.destroy()
                choixmob()

#Augmente l'expérience de 110 lorsque l'on tue un monstre difficile, puis nous fait monter de niveau si on atteint l'expérience requise, donc si on a des points à attribuer, ça nous ramène à la fenêtre d'augmentation de statistiques, sinon, si on a pas choisi d'aptitude (et que l'on peut), nous ramène au choix d'aptitude, sinon, renvoi au choix de la difficulté
def xpdifficile():
    global Exp, ExpReq, Lvl
    Exp=Exp+110
    Chat.config(text=("Vous gagnez 110 points d'expérience"))
    Chat.update()
    if Exp>=ExpReq:
        Jeu.after(2000,algolvl)
    else:
        if Ptslvl>0:
            fencombat.destroy()
            attribptsstat()
        else:
            if Aptipts==1:
                fencombat.destroy()
                choixapti()
            else:
                fencombat.destroy()
                choixmob()

#Désactive tout les boutons d'actions lorsqu'une action est en cours lors du combat
def Stopboutonaction():
    Attaquer.config(state=DISABLED)
    Attaquer.update()
    Blocage.config(state=DISABLED)
    Blocage.update()
    Aptitude.config(state=DISABLED)
    Aptitude.update()

#Réactive tout les boutons d'actions lorsqu'il n'y a plus d'action durant le combat afin d'en choisir une nouvelle
def Startboutonaction():
    Attaquer.config(state=NORMAL)
    Attaquer.update()
    Blocage.config(state=NORMAL)
    Blocage.update()
    Aptitude.config(state=NORMAL)
    Aptitude.update()

#Lorsque que le combat se termine, si le monstre a été tué, on gagne de l'expérience selon la difficulté de celui-ci mais si le héro a été tué, ça nous ramène à l'écran de sélection de la difficulté
#Les .after de cette fonction sont mise sur 2000 afin que les fonctions soient appelées après 2sec
def fincombat():
    if PdVr<=0:
        Chat.config(text=("Vous avez battu "+monster))
        Chat.update()
        if diff==1:
            Jeu.after(2000,xpfacile)
        elif diff==2:
            Jeu.after(2000,xpmoyen)
        elif diff==3:
            Jeu.after(2000,xpdifficile)
    elif HPdVr<=0:
        Chat.config(text=("Vous avez perdu le combat."))
        Chat.update()
        Jeu.after(2000,héromort)

#Gère la première partie de la rencontre, lorsque le monstre apparait, en nous affichant quel monstre a été choisi puis en nous demandant de choisir une action
def screencombat():
    global HPdVr,PdVr, Chat
    PdVr=PdV
    HPdVr=HPdV
    ecrandecombat()
    Stopboutonaction()
    global Chat
    Chat=Label(fencombat, image=ChatImg, text=(monster+' sera votre adversaire !'), compound="center", font="Sylfaen 16", fg="Black")
    Chat.place(x=0,y=400, height=200, width=600)
    Chat.update()
    time.sleep(2)
    actions()
    Startboutonaction()

#Lors du choix de la difficulté, cela lance l'algorithme définissant le monstre choisi parmi les monstres monstres faciles puisque cette fonction est associée au bouton "facile"
def combatfacile():
    monstrefacile()
    screencombat()

#Lors du choix de la difficulté, cela lance l'algorithme définissant le monstre choisi parmi les monstres monstres moyens puisque cette fonction est associée au bouton "moyen"
def combatmoyen():
    monstremoyen()
    screencombat()

#Lors du choix de la difficulté, cela lance l'algorithme définissant le monstre choisi parmi les monstres monstres difficiles puisque cette fonction est associée au bouton "difficile"
def combatdifficile():
    monstredifficile()
    screencombat()

#Gère le blocage du héro (à finir avec anim + after quand j'aurais le bouclier)
def HBlocage():
    global HDefmod
    #Modifie la défense du héro dans une variable qui change que pour 1 tour de combat
    HDefmod=HDef*1.5
    #Modifie le chat en affichant que la défense a été augmentée
    Stopboutonaction()
    AnimHBlocage()
    Chat.config(text=("Défense augmentée !"))
    Chat.update()
    #Tire un nombre entre 1 et 4 afin de géré si le monstre bloque ou attaque
    z=randint(1,4)
    #Si 1, le monstre bloque et le chat affiche qu'il augmente sa défense
    if z==1:
        MBlocage(2050)
        Jeu.after(2050,updef)
        Jeu.after(4350, finmboubouanim)
    #Si 2,3 ou 4, le monstre attaque
    elif z==2 or z==3 or z==4:
        MAttaque(2050)
        #Si le monstre a généré a tiré un coup critique (voir la fonction MAttaque), cela modifie le chat afin d'en informer le joueur
        if MCC==1:
          Jeu.after(2850, AffMCC)
        #Sinon, affiche juste les dégats faits
        else:
            Jeu.after(2850,mattackdisp)
        #Modifie les points de vie du joueur
        Jeu.after(2850, hbar)

#Augmentation de la défense du monstre
#Prend en paramètre un temps, permettant l'activation de la fonction et la détermination des valeurs nécessaires aux algorithmes de combat tout en déclenchant l'animation de blocage du monstre après un temps voulu
def MBlocage(temps):
    global MDefmod
    MDefmod=Def*1.5
    Jeu.after(temps,AnimMBlocage)

#Gère les dégats et les Coups Critiques lors de l'attaque du héro
#Prend en paramètre un temps, permettant l'activation de la fonction et la détermination des valeurs nécessaires aux algorithmes de combat tout en déclenchant l'animation d'attaque du héro après un temps voulu
def HAttaque(temps):
    global PdVr, HDégats, HCC
    #Donne une probabilité de 1/15 de faire un coup critique
    HCC=randint(1,15)
    #Si la défense n'est pas modifié, calcule les dégats par rapport à celle-ci
    if MDefmod==0:
        HDégats=(HStr/Def)*1.5
    #Sinon, calcule les dégats par rapport à la défense modifiée
    else:
        HDégats=(HStr/MDefmod)*1.5
    #Si HCC tombe sur 1, alors fait un coup critique (donc multiplie les dégats par 2)
    if HCC==1:
        HDégats=HDégats*2
    #Calcule les points de vies du monstre
    PdVr=PdVr-HDégats
    #Si ils descendent à 0 ou en dessous, arrondie la valeur à 0 afin de ne pas avoir de points de vies négatifs
    if PdVr<=0:
        PdVr=0
    #Arrondie la valeur des points de vie au dizième près, de même pour les dégats
    PdVr=round(PdVr, 1)
    HDégats=round(HDégats, 1)
    Jeu.after(temps,AnimHAttaque)

#Gère les dégats et les Coups Critiques lors de l'attaque du monstre
#Prend en paramètre un temps, permettant l'activation de la fonction et la détermination des valeurs nécessaires aux algorithmes de combat tout en déclenchant l'animation d'attaque du monstre après un temps voulu
def MAttaque(temps):
    global HPdVr, MDégats, MCC
    #Donne une probabilité de 1/15 de faire un coup critique
    MCC=randint(1,15)
    #Si la dénfense du héro n'est pas modifiée, calcule les dégats par rapport à celle-ci
    if HDefmod==0:
        MDégats=(Str/HDef)*1.5
    #Sinon, calcule les dégats par rapport à la défense modifiée
    else:
        MDégats=(Str/HDefmod)*1.5
    #Si MCC tombe sur 1, alors le monstre fera un coup critique (dégats muultipliés par 2)
    if MCC==1:
        MDégats=MDégats*2
    #Calcule les points de vie du héro restants
    HPdVr=HPdVr-MDégats
    #Si les points de vie du héro tombe en dessous de 0, arrondi à 0 afin d'éviter d'avoir des valeurs négatives
    if HPdVr<=0:
        HPdVr=0
    #Arrondie les dégats et les points de vies au dixième près
    HPdVr=round(HPdVr,1)
    MDégats=round(MDégats, 1)
    Jeu.after(temps,AnimMAttaque)

#Gère l'animation d'attaque du monstre
def AnimMAttaque():
    global xm, ym, stopmanim
    #Si le monstre se situe en x=650 et en y=275 et que l'animation a déjà été lancée, alors remet sur 0 la variable permettant l'arrêt de l'animation et arrête la fonction
    if xm==650 and ym==275 and stopmanim==1:
        stopmanim=0
        return
    #Si le monstre se situe en x<650 et en y=275, c'est à dire qu'il a déjà fait son animation d'attaque, alors il revient à sa postion de départ
    elif xm<650 and ym==275:
        xm=xm+dxm
        fencombat.coords(Imagemonstre, xm, ym)
    #Le mouvement principal de l'Animation
    #Quand le monstre est à une abscisse supérieur à l'abscisse de fin de l'animation, alors...
    elif xm>450:
        #...si le monstre n'a pas fait sa première diagonale de l'animation, c'est-à-dire s'il n'a pas parcouru la moitié de la distance en abscisse, alors le déplace vers "en haut à gauche"
        if xm>550:
            xm=xm-dxm
            ym=ym-dym
            fencombat.coords(Imagemonstre, xm, ym)
        #...Si le monstre a fait sa première diagonale de l'animation, alors lui faire faire la seconde, c'est-à-dire le déplace vers "en bas à gauche"
        elif xm<=550:
            xm=xm-dxm
            ym=ym+dym
            fencombat.coords(Imagemonstre, xm, ym)
    #Après un premier tour de boucle, indique au programme que l'animation a commencé, afin qu'une fois qu'elle est fini, le premier if s'execute et mette fin à la fonction
    stopmanim=1
    #Repète le déplacement toute les 20ms
    Jeu.after(20, AnimMAttaque)

#Gère l'animation d'attaque du héro
#Même principe que l'animation du monstre mais dans la direction opposé, donc les additions deviennent des soustractions et inversement, mais seulement pour les abscisses
def AnimHAttaque():
    global xh, yh, stophanim
    if xh==350 and yh==275 and stophanim==1:
        return
    elif xh>350 and yh==275:
        xh=xh-dxm
        fencombat.coords(Imagehéro, xh, yh)
    elif xh<550:
        if xh<450:
            xh=xh+dxm
            yh=yh-dym
            fencombat.coords(Imagehéro, xh, yh)
        elif xh>=450:
            xh=xh+dxm
            yh=yh+dym
            fencombat.coords(Imagehéro, xh, yh)
    stophanim=1
    Jeu.after(20, AnimHAttaque)

#Gère l'animation de blocage du héro
def AnimHBlocage():
    global Boubou, stopbanime, xb, yb, Imgboubou
    #Si l'animation n'a pas fait de tour, donc au premier lancement de la fonction, alors créer l'image du bouclier et dit au programme que le bouclier a été créé en mettant Boubou sur 1
    if Boubou==0:
        xb=350
        yb=100
        Boubou=1
        Imgboubou=fencombat.create_image(xb, yb, image=Defbouclier)
    #Ou si le bouclier est descendu jusqu'à 275 d'ordonnée, arrête la fonction
    elif yb==275 and stopbanime==1:
        return
    #Ou si le bouclier est au dessus de 275 en y, le fait descendre jusqu'à que l'elif du dessus soit validé
    elif yb<275:
        yb=yb+dym
        fencombat.coords(Imgboubou, xb, yb)
    #Dit au programme que la fonction a déjà tourné une fois
    stopbanime=1
    #Fait le déplacement du bouclier toute les 15ms
    Jeu.after(15, AnimHBlocage)

#Gère l'animation de blocage du monstre
#Fonctionne de la même façon que celle du héro, sauf que le x lors de la création d'image est différent car le bouclier apparait au dessus du héro
def AnimMBlocage():
    global MBoubou, stopbmanime, xbm, ybm, Imgmboubou
    if MBoubou==0:
        xbm=650
        ybm=100
        MBoubou=1
        Imgmboubou=fencombat.create_image(xbm, ybm, image=Defbouclier)
    elif ybm==275 and stopbmanime==1:
        return
    elif ybm<275:
        ybm=ybm+dym
        fencombat.coords(Imgmboubou, xbm, ybm)
    stopbmanime=1
    Jeu.after(15, AnimMBlocage)

#Gère l'animation lors du lancement de l'aptitude Evisceration
def AnimEviscer():
    global stopeviscanim, xe, ye, DagueEvisc
    #Si la fonction est à son premier tour, créer l'image de la Dague et dit au programme que l'image est créée
    if stopeviscanim==0:
        xe=750
        ye=175
        stopeviscanim=1
        DagueEvisc=fencombat.create_image(xe, ye, image=Dague)
    #Si la dague n'est pas à ses coordonnées d'arrivé, la fait se déplacer en diagonale vers "en bas à gauche"
    elif xe!=550 and ye!=375:
        xe=xe-dxm
        ye=ye+dym
        fencombat.coords(DagueEvisc, xe, ye)
    #Mais si la dague est à ses coordonnées d'arrivé, supprime l'image de la dague, remet la variable d'information sur 0 afin qu'au prochain lancement l'image soit recréée et arrête la fonction
    elif xe==550 and ye==375:
        fencombat.delete(DagueEvisc)
        stopeviscanim=0
        return
    #La dague se déplace toute les 15ms
    Jeu.after(15, AnimEviscer)

#Gère l'animation lors du lancement de l'aptitude Bandage
def AnimBand():
    global stopbandanim1, stopbandanim2, stopbandanim3, xband, yband, AffBand1, AffBand2, AffBand3
    #Si aucune des 3 images n'a déjà été créée, créée la première et dit au programme qu'elle a été créée
    if stopbandanim1==0 and stopbandanim2==0 and stopbandanim3==0:
        xband=300
        yband=225
        stopbandanim1=1
        AffBand1=fencombat.create_image(xband, yband, image=Bandimg)
    #Si la première image est créée mais pas les 2 autres, créer la 2eme, indique au programme que la 2eme a été créée et supprime la 1ere image
    elif stopbandanim1==1 and stopbandanim2==0 and stopbandanim3==0:
        xband=425
        yband=275
        stopbandanim2=1
        AffBand2=fencombat.create_image(xband, yband, image=Bandimg)
        fencombat.delete(AffBand1)
    #Si les 2 première images ont étés créées mais pas la 3eme, alors créer la 3eme, indique au programme qu'elle a été créée et supprime la 2eme
    elif stopbandanim1==1 and stopbandanim2==1 and stopbandanim3==0:
        xband=325
        yband=325
        stopbandanim3=1
        AffBand3=fencombat.create_image(xband, yband, image=Bandimg)
        fencombat.delete(AffBand2)
    #Si la dernière image (la 3eme) a été créée, alors la supprime et remet tout les compteur sur 0 pour le prochain lancement de l'aptitude, puis arrête la fonction
    elif stopbandanim3==1:
        fencombat.delete(AffBand3)
        stopbandanim1=0
        stopbandanim2=0
        stopbandanim3=0
        return
    #Une image se créée toute les 0.8s, soit un temps total de 2.4s pour l'animation entière
    Jeu.after(800,AnimBand)

#Algorithme gérant le combat lorsque le héro attaque en premier
def AttackHerofirst():
    global HDefmod, MDefmod
    HDefmod=0
    MDefmod=0
    #Donne un probabilité de 1/4 au monstre de bloquer
    z=randint(1,4)
    #Si z tombe sur 1, alors le monstre bloque
    if z==1:
        #Augmente la défense du monstre (la défense est prioritaire à l'attaque afin qu'elle serve à quelque chose)
        MBlocage(0)
        #Affiche dans le chat l'augmentation de défense
        updef()
        #Le héro attaque à son tour
        HAttaque(1500)
        #Si il fait un coup critique, alors le signaler dans le chat
        if HCC==1:
            Jeu.after(2300,AffHCC)
        #Sinon, afficher seulement les dégats faits
        else:
            Jeu.after(2300,hattackdisp)
        #Modifie les points de vie du monstre dans l'affichage de ceux-ci
        Jeu.after(2300, mbar)
        #Supprime l'image du bouclier du monstre
        Jeu.after(4650, finmboubouanim)
    #Si z prend la valeur 2, 3 ou 4, le monstre attaque, et comme le héro attaque en premier, le monstre attaquera en second
    elif z==2 or z==3 or z==4:
        #Le héro attaque
        HAttaque(0)
        #Si il fait un coup critique, l'affiche dans le chat
        if HCC==1:
            Jeu.after(800,AffHCC)
        #Sinon, affiche ses dégats normalement
        else:
            Jeu.after(800,hattackdisp)
        #Modifie les points de vie du monstre dans l'affichage de ceux-ci
        Jeu.after(800, mbar)
        #Si les points de vie du monstre sont supérieur à 0, alors le monstre attaque (afin d'éviter que si le monstre n'a plus de points de vie, il attaque quand même, ce qui n'est pas logique et cela pourrait créer des problèmes lors d'égalité)
        if PdVr>0:
            #Le monstre attaque
            MAttaque(2300)
            #Si le monstre fait un coup critique, alors l'affiche
            if MCC==1:
                Jeu.after(3100,AffMCC)
            #Sinon, affiche ses dégats normalement
            else:
                Jeu.after(3100,mattackdisp)
            #Modifie les points de vie du héro dans l'affichage de ceux-ci
            Jeu.after(3100, hbar)

#Algorithme de combat lorsque que le monstre attaque en premier, le principe est le même sauf que dans la deuxième partie de l'algorithme, ce ne sera pas le héro qui attaque en premier, mais le monstre
def AttackMobfirst():
    global HDefmod, MDefmod
    HDefmod=0
    MDefmod=0
    z=randint(1,4)
    if z==1:
        MBlocage(0)
        updef()
        HAttaque(1500)
        if HCC==1:
            Jeu.after(2300,AffHCC)
        else:
            Jeu.after(2300,hattackdisp)
        Jeu.after(2300, mbar)
        Jeu.after(4650, finmboubouanim)
    #Si z vaut 2, 3 ou 4, alors le monstre ne bloque pas mais attaque
    elif z==2 or z==3 or z==4:
        MAttaque(0)
        if MCC==1:
            Jeu.after(800,AffMCC)
        else:
            Jeu.after(800,mattackdisp)
        Jeu.after(800, hbar)
        #Si les points de vies du héro sont supérieur à 0, il attaque, cela permet donc de ne pas le faire attaquer s'il meurt, idem que l'algorithme d'avant, cela va éviter toute égalité et illogique
        if HPdVr>0:
            HAttaque(2300)
            if HCC==1:
                Jeu.after(3100,AffHCC)
            else:
                Jeu.after(3100,hattackdisp)
            Jeu.after(3100,mbar)

#Regroupe les algorithme d'attaque afin de définir lequel est choisi
def AttackGlobal():
    global CDBandage, CDEvisceration, stopmanim, stophanim, fin
    stopmanim=0
    stophanim=0
    #Empêche les boutons d'actions d'être actvé lors de l'affichage, permettant ainsi de ne pas faire buggé le programme
    Stopboutonaction()
    #Si l'initiative du héro est plus haute que celle du monstre, alors il attaque en premier
    if HIni>Ini:
        AttackHerofirst()
    #Ou si l'initiative du monstre est supérieure à celle du héro, il attaque en premier
    elif Ini>HIni:
        AttackMobfirst()
    #Mais si les initiatives sont égales, il y a 50% de chance que le héro attaque en premier et 50% de chance que le monstre attaque en premier
    elif HIni==Ini:
        #Probabilité de 1/2
        b=randint(1,2)
        if b==1:
            AttackHerofirst()
        elif b==2:
            AttackMobfirst()
    #Si les points de vie du monstre ou du héro sont à 0, met fin au combat
    if PdVr<=0 or HPdVr<=0:
        fin=1
        Jeu.after(4600,fincombat)
    #Réactive les boutons d'actions permettant au joueur de continuer le combat et lui demande de choisir une action
    if fin==0:
        Jeu.after(4650,Startboutonaction)
        Jeu.after(4650, actions)
    #Si le bandage est en cooldown, alors réduit celui-ci de 1
    if CDBandage!=0:
        CDBandage=CDBandage-1
    #Si l'évisceration est en cooldown, alors réduit celui-ci de 1
    if CDEvisceration!=0:
        CDEvisceration=CDEvisceration-1

#Gère les algorithme d'attaque lorsque le héro bloque
def BlocageAttH():
    global CDBandage, CDEvisceration, fin, Boubou
    #Empêche l'utilisation des boutons d'actions
    Stopboutonaction()
    #Lance le blocage du héro
    HBlocage()
    #Réactive les boutons d'actions si aucun des personnages ne sont mort, sinon, met fin au combat
    if HPdVr<=0 or PdVr<=0:
        fin=1
        Jeu.after(4500,fincombat)
    if fin==0:
        Jeu.after(4550, actions)
        Jeu.after(4550,Startboutonaction)
    #Si le bandage est en cooldown, alors réduit celui-ci de 1
    if CDBandage!=0:
        CDBandage=CDBandage-1
    #Si l'évisceration est en cooldown, alors réduit celui-ci de 1
    if CDEvisceration!=0:
        CDEvisceration=CDEvisceration-1
    Jeu.after(4350, finboubouanim)

#Calcule le soin du Bandage
def bandagefct():
    global Soin, HPdV, HPdVr
    #Calcul du soin: 25% des points de vie maximum du héro
    Soin=round(HPdV//4,1)
    #Calcule la différence de points de vie entre les points de vie max et ceux restants
    DiffPdV=HPdV-HPdVr
    #Si les soins sont supérieurs à cet différence, alors ils en deviennent égaux, afin de ne pas dépasser les points de vies maximums
    if Soin>=DiffPdV:
        Soin=round(DiffPdV,1)
    #Soigne le héro
    HPdVr=HPdVr+Soin
    #Lance l'animation de soin
    AnimBand()

#Algorithme de combat prenant en compte l'utilisation de bandage par le héro
def useband():
    global CDBandage, CDEvisceration, stopmanim, stophanim, fin
    stopmanim=0
    stophanim=0
    #Ferme la fenêtre d'aptitude afin de pouvoir voir le chat
    off()
    #Empêche l'utilisation des boutons d'actions
    Stopboutonaction()
    #Si le héro a plus d'initiative que le monstre, il se soigne avant que celui-ci attaque
    if HIni>Ini:
        #Soigne le héro
        bandagefct()
        #Affiche les soins dans le chat
        Jeu.after(2400, AffSoin)
        #Modifie les points de vie du héro dans l'affichage de ceux-ci
        Jeu.after(2400, hbarsoin)
        #Le monstre attaque
        MAttaque(3100)
        #Si le monstre fait un coup critique, alors le signale au héro
        if MCC==1:
            Jeu.after(3900, AffMCC)
        #Sinon, affiche les dégats normalement
        else:
            Jeu.after(3900, mattackdisp)
        #Modifie les points de vie du héro dans l'affichage de ceux-ci
        Jeu.after(3900, hbar)
    #Si le monstre a plus d'initiative que le héro, le héro se soigne après l'attaque du monstre
    elif Ini>HIni:
        MAttaque(0)
        if MCC==1:
            Jeu.after(800, AffMCC)
        else:
            Jeu.after(800, mattackdisp)
        Jeu.after(800, hbar)
        if HPdVr>0:
            Jeu.after(1500,bandagefct)
            Jeu.after(3900, hbar)
            Jeu.after(3900, AffSoin)
    #Comme dans l'algorithme d'AttackGlobal, si les 2 initiatives sont égales, le héro a 50% de chance de se soigner avant l'attaque du monstre et le monstre a 50% de chance d'attaquer le joueur avant qu'il se soigne
    elif HIni==Ini:
        z=randint(1,2)
        if z==1:
            bandagefct(0)
            Jeu.after(2400, AffSoin)
            Jeu.after(2400, hbarsoin)
            MAttaque(3100)
            if MCC==1:
                Jeu.after(3900, AffMCC)
            else:
                Jeu.after(3900, mattackdisp)
            Jeu.after(3900, hbar)
        elif z==2:
            MAttaque(0)
            if MCC==1:
                Jeu.after(800, AffMCC)
            else:
                Jeu.after(800, mattackdisp)
            Jeu.after(800, hbar)
            if HPdVr>0:
                Jeu.after(1500,bandagefct)
                Jeu.after(3900, hbar)
                Jeu.after(3900, AffSoin)
    #Réactive les boutons d'actions si aucun des personnages ne sont mort, sinon, met fin au combat
    if HPdVr<=0 or PdVr<=0:
        fin=1
        Jeu.after(5400,fincombat)
    if fin==0:
        Jeu.after(5450, actions)
        Jeu.after(5450,Startboutonaction)
    #Met le cooldown de bandage sur 5 afin de pouvoir le réutiliser dans 5 tours
    CDBandage=5
    #Réduit le cooldown d'Evisceration de 1
    if CDEvisceration!=0:
        CDEvisceration=CDEvisceration-1

#Gère les dégats fait par Evisceration
def HEviscer(temps):
    global PdVr, HDégats, HCC
    #Au lieu d'avoir une probabilité de 1/15, elle est de 1/7 car Evisceration a 2 fois plus de chance de faire un coup critique
    HCC=randint(1,7)
    #Si le monstre a bloqué, alors les dégats sont calculés en fonction de sa défense de base
    if MDefmod==0:
        HDégats=(HStr/Def)*1.5
    #Sinon, ils sont calculés en fonction de la défense du monstre modifiée
    else:
        HDégats=(HStr/MDefmod)*1.5
    #Si HCC vaut 1, le joeuur a fait un coup critique, donc ces dégats sont doublés
    if HCC==1:
        HDégats=HDégats*2
    #Comme Evisceration fait 2 fois plus de dégats, on les multiplie par 2 après calcul de ceux-ci
    HDégats=HDégats*2
    PdVr=PdVr-HDégats
    if PdVr<=0:
        PdVr=0
    PdVr=round(PdVr, 1)
    HDégats=round(HDégats, 1)
    Jeu.after(temps, AnimEviscer)

#Algorithme lorsque le Héro utilise Evisceration et qu'il a plus d'initiative que le monstre
def HEviscerfirst():
    global HDefmod, MDefmod
    HDefmod=0
    MDefmod=0
    z=randint(1,4)
    if z==1:
        MBlocage(0)
        Jeu.after(1500, updef)
        HEviscer(2500)
        if HCC==1:
            Jeu.after(3100, EviscCC)
        else:
            Jeu.after(3100, EviscnoCC)
        Jeu.after(3100, mbar)
        Jeu.after(4450, finmboubouanim)
    elif z==2 or z==3 or z==4:
        HEviscer(0)
        if HCC==1:
            Jeu.after(600, EviscCC)
        else:
            Jeu.after(600, EviscnoCC)
        Jeu.after(600, mbar)
        if PdVr>0:
            MAttaque(2100)
            if MCC==1:
                Jeu.after(2900, AffMCC)
            else:
                Jeu.after(2900, mattackdisp)
            Jeu.after(2900, hbar)

#Algortihme lorsque le Héro utiliser Evisceration et qu'il a moins d'initiative que le monstre
def MEviscerfirst():
    global HDefmod, MDefmod
    HDefmod=0
    MDefmod=0
    z=randint(1,4)
    if z==1:
        MBlocage(0)
        Jeu.after(1500, updef)
        HEviscer(2500)
        if HCC==1:
            Jeu.after(3100, EviscCC)
        else:
            Jeu.after(3100, EviscnoCC)
        Jeu.after(3100, mbar)
        Jeu.after(4450, finmboubouanim)
    elif z==2 or z==3 or z==4:
        MAttaque(0)
        if MCC==1:
            Jeu.after(800, AffMCC)
        else:
            Jeu.after(800, mattackdisp)
        Jeu.after(800, hbar)
        if HPdVr>0:
            HEviscer(2300)
            if HCC==1:
                Jeu.after(2900, EviscCC)
            else:
                Jeu.after(2900, EviscnoCC)
            Jeu.after(2900, mbar)

#Gère le lancement d'Evisceration en fonction de l'initiative
def useeviscer():
    global CDEvisceration, CDBandage, stopmanim, stophanim, fin
    stopmanim=0
    stophanim=0
    off()
    Stopboutonaction()
    if HIni>Ini:
        HEviscerfirst()
    elif Ini>HIni:
        MEviscerfirst()
    elif HIni==Ini:
        b=randint(1,2)
        if b==1:
            HEviscerfirst()
        elif b==2:
            MEviscerfirst()
    CDEvisceration=3
    if CDBandage!=0:
        CDBandage=CDBandage-1
    #Réactive les boutons d'actions si aucun des personnages ne sont mort, sinon, met fin au combat
    if PdVr<=0:
        fin=1
        Jeu.after(4600,fincombat)
    if fin==0:
        Jeu.after(4650, actions)
        Jeu.after(4650, Startboutonaction)

#Ferme la fenetre des aptitude disponible en combat (ainsi que la croix)
def off():
    sort.destroy()
    closecan.destroy()

#Gère les boutons d'aptitude en combat
def ecranapti():
    global sort, Bandageuse, Evisceruse, closecan, close
    sort=Canvas(fencombat, height=200, width=198, relief="flat")
    bg=sort.create_image(100,100, image=BGApti)
    sort.place(x=400, y=400)
    closecan=Canvas(fencombat, height=20, width=20)
    closecan.place(x=575, y=400)
    close=Button(closecan, image=CloseApti, font="Sylfaen 20 bold",overrelief="ridge", command=off)
    close.place(x=0, y=0, height=25, width=25)
    #Si le joueur a sélectionné le bandage, alors créer le bouton associé
    if Bandageapt==1:
        Bandageuse=Button(sort,image=Band,overrelief="ridge", command=useband)
        Bandageuse.place(x=0, y=0, height=100, width=198)
        #Si le bandage est en cooldown, alors empêche son utilisation
        if CDBandage!=0:
            Bandageuse.config(state=DISABLED)
            Bandageuse.update()
    #Si le joueur a sélectionné l'evisceration, alors crééer le bouton associé
    if Eviscerationapt==1:
        Evisceruse=Button(sort,image=Eviscimg,overrelief="ridge", command=useeviscer)
        Evisceruse.place(x=0, y=100, height=100, width=198)
        #Si l'evisceration est en cooldown, alors empêche son utilisation
        if CDEvisceration!=0:
            Evisceruse.config(state=DISABLED)
            Evisceruse.update()

#Gère la sauvegarde du héro en écrivant toute les statistiques dans le fichier portant le nom du héro
def Save():
    global hname
    listfich=os.listdir("SAVE")
    fich=open("SAVE/"+hname+".txt","w",encoding="utf-8")
    fich.write(hname+"\n")
    fich.write(str(HPdV)+"\n")
    fich.write(str(HStr)+"\n")
    fich.write(str(HIni)+"\n")
    fich.write(str(HDef)+"\n")
    fich.write(str(Exp)+"\n")
    fich.write(str(ExpReq)+"\n")
    fich.write(str(Lvl)+"\n")
    fich.write(str(Bandageapt)+"\n")
    fich.write(str(Eviscerationapt)+"\n")
    fich.write(str(Ptslvl)+"\n")
    fich.write(str(Aptipts)+"\n")
    fich.close()

#Gère la sauvegarde mais ferme le jeu après avoir sauvegardé
def SaveQuit():
    Save()
    Jeu.destroy()

#Créer l'écran de combat avec les boutons nécessaire au gameplay et les images nécessaire aux animations
def ecrandecombat():
    choixdiff.destroy()
    global fencombat, Monsterbar, Herobar, Attaquer, Blocage, Aptitude, h, w, hname, xm, ym, xh, yh, Imagemonstre, Imagehéro
    xm=650
    ym=275
    xh=350
    yh=275
    h=600
    w=1000
    fencombat=Canvas(Jeu, height=h, width=w)
    fencombat.grid(row=1, column=1)
    fencombat.create_image(500,200, image=BGCombat)
    Attaquer=Button(fencombat, image=AttImg ,overrelief="sunken", command=AttackGlobal)
    Attaquer.place(x=600,y=400, height=100, width=200)
    Blocage=Button(fencombat, image=BlockImg,overrelief="sunken", command=BlocageAttH)
    Blocage.place(x=800, y=400, height=100, width=200)
    Aptitude=Button(fencombat, image=AptiImg,overrelief="sunken", command=ecranapti)
    Aptitude.place(x=600, y=500, height=100, width=400)
    Imagemonstre=fencombat.create_image(xm,ym, image=Imgmob)
    Imagehéro=fencombat.create_image(xh,yh, image=Héroimg)
    HeroNameplate=fencombat.create_image(350,100, image=Nameplate)
    MobNameplate=fencombat.create_image(650,100, image=Nameplate)
    FlHeroNP=fencombat.create_image(350,162.5, image=FlNameplate)
    FlMobNP=fencombat.create_image(650,162.5, image=FlNameplate)
    Monsterbar=fencombat.create_text(650,100, text=(monster+"\n"+str(PdVr)+"/"+str(PdV)+" PdV"), font="Sylfaen 22 bold")
    Herobar=fencombat.create_text(350,100, text=(hname+"\n"+str(HPdVr)+"/"+str(HPdV)+" PdV"), font="Sylfaen 22 bold")

#Affiche au joueur ses statistiques lorsqu'il clique sur "Afficher les statistiques" dans la barre de menu, lui permettant de suivre sa progression à tout moment
def FenStats():
    global Stats, fenstats, DispPdV, DispStr, DispIni, DispDef, DispExp, DispBandage, DispEvisceration
    Stats=Tk()
    Stats.title("Stats")
    Stats.resizable(height=False, width=False)
    fenstats=Canvas(Stats, height=275, width=200)
    fenstats.grid(row=1, column=1)
    Dispname=Label(fenstats, text=(hname+", niveau "+str(Lvl)), font="Sylfaen 14 bold")
    Dispname.place(x=5, y=5, height=65, width=190)
    DispPdV=Label(fenstats, text=("PdV: "+str(HPdV)), font="Sylfaen 14 bold")
    DispPdV.place(x=5, y=75, height=25, width=190)
    DispStr=Label(fenstats, text=("Str: "+str(HStr)), font="Sylfaen 14 bold")
    DispStr.place(x=5, y=100, height=25, width=190)
    DispIni=Label(fenstats, text=("Ini: "+str(HIni)), font="Sylfaen 14 bold")
    DispIni.place(x=5, y=125, height=25, width=190)
    DispDef=Label(fenstats, text=("Def: "+str(HDef)), font="Sylfaen 14 bold")
    DispDef.place(x=5, y=150, height=25, width=190)
    DispExp=Label(fenstats, text=("Exp: "+str(Exp)+"/"+str(ExpReq)), font="Sylfaen 14 bold")
    DispExp.place(x=5, y=175, height=25, width=190)
    if Bandageapt==1:
        DispBandage=Label(fenstats, text=("Bandage: Oui"), font="Sylfaen 14 bold")
        DispBandage.place(x=5, y=200, height=25, width=190)
    elif Bandageapt==0:
        DispBandage=Label(fenstats, text=("Bandage: Non"), font="Sylfaen 14 bold")
        DispBandage.place(x=5, y=200, height=25, width=190)
    if Eviscerationapt==1:
        DispEvisceration=Label(fenstats, text=("Evisceration: Oui"), font="Sylfaen 14 bold")
        DispEvisceration.place(x=5, y=225, height=25, width=190)
    elif Eviscerationapt==0:
        DispEvisceration=Label(fenstats, text=("Evisceration: Non"), font="Sylfaen 14 bold")
        DispEvisceration.place(x=5 , y=225, height=25, width=190)

    Stats.mainloop()

#Gère l'écran de sélection de difficulté
def choixmob2():
    global h,w, choixdiff, fin, CDBandage, CDEvisceration
    nom.destroy()
    nom.unbind_all('<ButtonPress-1>')
    nom.unbind_all('<Enter>')
    nom.unbind_all('<Leave>')
    MStats.entryconfig(0, state=NORMAL)
    MSave.entryconfig(0, state=NORMAL)
    MSave.entryconfig(1, state=NORMAL)
    CDBandage=0
    CDEvisceration=0
    fin=0
    h=250
    w=450
    choixdiff=Canvas(Jeu, height=h, width=w)
    choixdiff.grid(row=1,column=1)
    Difft=Label(choixdiff, text="Choisissez la difficulté du monstre que vous souhaitez affronter", font="Sylfaen 16 bold")
    Difft.grid(row=1,column=0,padx=10)
    Facile=Button(choixdiff, text="Facile", font="Sylfaen 14",overrelief="ridge", command=combatfacile)
    Facile.grid(row=2, column=0, padx=10, pady=5)
    Moyen=Button(choixdiff, text="Moyen", font="Sylfaen 14",overrelief="ridge", command=combatmoyen)
    Moyen.grid(row=3,column=0,padx=10, pady=5)
    Difficile=Button(choixdiff, text="Difficile", font="Sylfaen 14",overrelief="ridge", command=combatdifficile)
    Difficile.grid(row=4,column=0,padx=10, pady=5)

#Gère les conditions avant la sélection du monstre, tel que le nom du joueur soit valide
def choixmob():
    global CDBandage, CDEvisceration, hname, heronamenew
    if hname=="":
        hname=heroname.get()
        if len(hname)==0 or len(hname)>7:
            heronamenew.config(text="Veuillez entrer un nom faisant 7 lettres ou moins")
            heronamenew.update()
            hname=""
        else:
            choixmob2()
    else:
        choixmob2()

#Gère les intéractions avec les sauvegardes sur la première fenêtre du jeu
def opensave(event):
    global hname, HPdV, HStr, HIni, HDef, Exp, ExpReq, Lvl, Bandageapt, Eviscerationapt, Ptslvl, Aptipts, BSave
    #On passe par un Try: Except: afind évider toute erreurs lors d'un clique dans le canevas, et non sur un des boutons de sauvegarde
    try:
        #On récupère l'id du label sur lequel on clique
        idwidg=str(event.widget)
        #On en créé une version sans le "poub" à la fin (sur python 3.6, l'id sera sous la forme .!canvas. mais sous python 3.4, il sera sous la forme .XXXXXXXX. avec X un chiffre. Après le dernier "." se situera le nom de notre bouton, soit k ou poubk
        idwidg2=idwidg.replace("poub","")
        #On transforme la version sans poub en liste
        listwidg=list(idwidg2)
        #On va chercher le chiffre à la fin de la liste afin d'identifier les boutons cliqués
        nbrfin=listwidg[len(listwidg)-1]
        #On récupère l'id aléatoire en enlevant le .k à la fin
        canid=idwidg2.replace("."+nbrfin,"")
        #On enlève l'id aléatoire à l'id obtenu au début afin de se retrouver soit avec poubk soit avec k
        poubverif=idwidg.replace(canid+".","")
        #On transforme en liste afin de vérifier la présence de la lettre "p" pour le premier if
        poubverlist=list(poubverif)
        #Si "p" est dans la liste, alors c'est le bouton poubelle qui a été pressé, donc on supprime le bouton lui-même, le bouton de la sauvegarde associer et le fichier de sauvegarde associé.
        if "p" in poubverlist:
            #Alors on détruit le bouton poubelle sur lequel on a appuyé
            event.widget.destroy()
            #Et on détruit le bouton de sauvegarde correspondant, c'est-à-dire que si on clique sur le bouton poubelle de la sauvegarde 3, le bouton de la sauvegarde 3 sera supprimé
            BSave[int(nbrfin)].destroy()
            #On supprime le fichier de sauvegarde correspondant
            os.remove('SAVE/'+listfich[int(nbrfin)])
            #On actualise la fenêtre afin de faire dispaïtre les boutons
            nom.update()
        #Mais si la première conditions n'est pas validé, alors c'est que le bouton cliqué est celui d'une sauvegarde, donc on charge les valeurs de la sauvegarde et on lance la partie avec les données du joueur
        if int(poubverif)>=0:
            fich=open("SAVE/"+listfich[int(poubverif)],"r",encoding="utf-8")
            liststats=fich.readlines()
            hname=liststats[0].replace("\n","")
            HPdV=int(liststats[1].replace("\n",""))
            HStr=int(liststats[2].replace("\n",""))
            HIni=int(liststats[3].replace("\n",""))
            HDef=int(liststats[4].replace("\n",""))
            Exp=int(liststats[5].replace("\n",""))
            ExpReq=int(liststats[6].replace("\n",""))
            Lvl=int(liststats[7].replace("\n",""))
            Bandageapt=int(liststats[8].replace("\n",""))
            Eviscerationapt=int(liststats[9].replace("\n",""))
            Ptslvl=int(liststats[10].replace("\n",""))
            Aptipts=int(liststats[11].replace("\n",""))
            fich.close()
            choixmob()
    #Si aucunes des conditions ne sont validées, c'est que l'on a cliqué ailleurs sur le canvas, donc rien ne s'effectue
    except:
        return

#Gère le survol avec la souris d'un bouton de sauvegarde, donnant un aperçu au joueur du contenu de la sauvegarde
def affistatsave(event):
    #On passe par un Try: Except: afin que si le joueur ne survol pas une sauvegarde, alors rien ne se passe
    try:
        global Affistats
        t=str(event.widget)
        listt=list(t)
        nbrfin=listt[len(listt)-1]
        fich=open("SAVE/"+listfich[int(nbrfin)],"r",encoding="utf-8")
        liststats=fich.readlines()
        Affhname=liststats[0].replace("\n","")
        AffHPdV=int(liststats[1].replace("\n",""))
        AffHStr=int(liststats[2].replace("\n",""))
        AffHIni=int(liststats[3].replace("\n",""))
        AffHDef=int(liststats[4].replace("\n",""))
        AffExp=int(liststats[5].replace("\n",""))
        AffExpReq=int(liststats[6].replace("\n",""))
        AffLvl=int(liststats[7].replace("\n",""))
        AffBandageapt=int(liststats[8].replace("\n",""))
        AffEviscerationapt=int(liststats[9].replace("\n",""))
        AffPtslvl=int(liststats[10].replace("\n",""))
        AffAptipts=int(liststats[11].replace("\n",""))
        Affistats=Canvas(Jeu, height=75, width=300, relief="groove", borderwidth=5, bg="#8C8B8B")
        Affistats.place(x=5, y=5, height=150, width=485)
        shname=Label(Affistats, text=(Affhname+", niveau "+str(AffLvl)), font="Sylfaen 14 bold",bg="#8C8B8B")
        shname.place(x=5, y=5, height=30, width=475)
        sHPdV=Label(Affistats, text=("PdV: "+str(AffHPdV)), font="Sylfaen 14 bold",bg="#8C8B8B")
        sHPdV.place(x=5, y=50, height=30, width=155)
        sHStr=Label(Affistats, text=("Str: "+str(AffHStr)), font="Sylfaen 14 bold",bg="#8C8B8B")
        sHStr.place(x=161, y=50, height=30, width=155)
        sHIni=Label(Affistats, text=("Ini: "+str(AffHIni)), font="Sylfaen 14 bold",bg="#8C8B8B")
        sHIni.place(x=322, y=50, height=30, width=155)
        sHDef=Label(Affistats, text=("Def: "+str(AffHDef)), font="Sylfaen 14 bold",bg="#8C8B8B")
        sHDef.place(x=5, y=80, height=30, width=155)
        sExp=Label(Affistats, text=("Exp: "+str(AffExp)+"/"+str(AffExpReq)), font="Sylfaen 14 bold",bg="#8C8B8B")
        sExp.place(x=161, y=80, height=30, width=155)
        if AffBandageapt==1:
            sBandage=Label(Affistats, text=("Bandage: Oui"), font="Sylfaen 14 bold",bg="#8C8B8B")
            sBandage.place(x=50, y=110, height=30, width=150)
        elif AffBandageapt==0:
            sBandage=Label(Affistats, text=("Bandage: Non"), font="Sylfaen 14 bold",bg="#8C8B8B")
            sBandage.place(x=50, y=110, height=30, width=150)
        if AffEviscerationapt==1:
            sEvisceration=Label(Affistats, text=("Evisceration: Oui"), font="Sylfaen 14 bold",bg="#8C8B8B")
            sEvisceration.place(x=280, y=110, height=30, width=180)
        elif AffEviscerationapt==0:
            sEvisceration=Label(Affistats, text=("Evisceration: Non"), font="Sylfaen 14 bold",bg="#8C8B8B")
            sEvisceration.place(x=280 , y=110, height=30, width=180)
    except:
        return

#Gère le fait que le joueur ne survol plus un bouton de sauvegarde, et détruit le canvas créé par affistatsave()
def desaffistatsave(event):
    try:
        Affistats.destroy()
    except:
        return

#Toute les variables importantes dans le programme sont définies ici afin de pouvoir les exploitées directement
#Fin indique au programme si le combat est fini ou non
fin=0
#dxm et dym corresponde au déplacement lors des animations durant le combat
dxm=5
dym=5
#Les stopanim permettent de dire au programme si les animations doivent ou non s'arrêtées
stopmanim=0
stophanim=0
stopbandanim1=0
stopbandanim2=0
stopbandanim3=0
stopbmanime=0
stopbanime=0
stopeviscanim=0
#Indique au programme que le bouclier de blocage n'est pas créé
MBoubou=0
Boubou=0
#Le joueur n'a pas de nom par défaut, ce qui permet d'éviter des erreurs lors du chargement des sauvegardes
hname=""
#Met la défense modifié du monstre et du héro sur 0 pour que le programme sache quand l'un des deux bloque
MDefmod=0
HDefmod=0
#Le joueur n'a pas de points de statistiques a attribué par défaut
Ptslvl=0
#Il ne possède ni le bandage, ni l'évisceration par défaut, donc ils n'ont pas de cooldowns actifs
Bandageapt=0
CDBandage=0
Eviscerationapt=0
CDEvisceration=0
#Il n'a pas de points d'aptitudes
Aptipts=0

#La fenêtre principale où tout commence
Jeu=Tk()
Jeu.title("The Hunt !")

#Chargement de toutes les images nécéssaires au programme
AttImg=PhotoImage(file='IMG/Boutons/Attaquer2.gif')
BlockImg=PhotoImage(file='IMG/Boutons/Bloquer.gif')
AptiImg=PhotoImage(file='IMG/Boutons/Aptitude.gif')
ChatImg=PhotoImage(file='IMG/Boutons/Chat.gif')
Poub=PhotoImage(file='IMG/Boutons/Poubelle.gif')
Nameplate=PhotoImage(file='IMG/Mobs/Nameplate.gif')
FlNameplate=PhotoImage(file='IMG/Mobs/FlNameplate.gif')
Band=PhotoImage(file='IMG/Boutons/Bandage.gif')
Eviscimg=PhotoImage(file='IMG/Boutons/Evisceration.gif')
BGApti=PhotoImage(file='IMG/Boutons/Ecranapti.gif')
CloseApti=PhotoImage(file='IMG/Boutons/Close.gif')
Héroimg=PhotoImage(file='IMG/Héro.gif')
Desert=PhotoImage(file='IMG/BG/Desert.gif')
Forêt=PhotoImage(file='IMG/BG/Forêt.gif')
Grotte=PhotoImage(file='IMG/BG/Grotte.gif')
Jungle=PhotoImage(file='IMG/BG/Jungle.gif')
Plage=PhotoImage(file='IMG/BG/Plage.gif')
Volcan=PhotoImage(file='IMG/BG/Volcan.gif')

#Images Animations
Defbouclier=PhotoImage(file='IMG/Animations/Bouclier 150.gif')
Bandimg=PhotoImage(file='IMG/Animations/Heal 50.gif')
Dague=PhotoImage(file='IMG/Animations/Dague 100.gif')

#Images montres faciles
Bébédrg=PhotoImage(file='IMG/Mobs/Monstres faciles/Bébé drg.gif')
Chvsouris=PhotoImage(file='IMG/Mobs/Monstres faciles/Chv-souris.gif')
Tatou=PhotoImage(file='IMG/Mobs/Monstres faciles/Tatou.gif')
Ratimg=PhotoImage(file='IMG/Mobs/Monstres faciles/Rat.gif')

#Images monstres moyens
Cobra=PhotoImage(file='IMG/Mobs/Monstres moyens/Cobra.gif')
Gorille=PhotoImage(file='IMG/Mobs/Monstres moyens/Gorille.gif')
Grizzly=PhotoImage(file='IMG/Mobs/Monstres moyens/Grizzly.gif')
Panthère=PhotoImage(file='IMG/Mobs/Monstres moyens/Panthère.gif')

#Images monstres difficiles
Krakenimg=PhotoImage(file='IMG/Mobs/Monstres difficiles/Kraken.gif')
Golem=PhotoImage(file='IMG/Mobs/Monstres difficiles/Golem.gif')
Dragon=PhotoImage(file='IMG/Mobs/Monstres difficiles/Dragon.gif')
Ogre=PhotoImage(file='IMG/Mobs/Monstres difficiles/Ogre.gif')

h=150
w=300
#Empêche le redimensionnement de la fenêtre
Jeu.resizable(width=False,height=False)
#Créer un menu
menubar=Menu(Jeu)
Jeu.config(menu=menubar)
#Créer les boutons du menu, en les désactivant jusqu'à que le joueur ait choisi un héro
MStats=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Stats", menu=MStats)
MStats.add_command(label="Afficher les Stats",state=DISABLED, command=FenStats)
MSave=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Sauvegarde", menu=MSave)
MSave.add_command(label="Sauvegarder et Continuer",state=DISABLED, command=Save)
MSave.add_command(label="Sauvegarder et Quitter",state=DISABLED, command=SaveQuit)
#Créer les canvas de sélection de personnage, ainsi que les boutons
nom=Canvas(Jeu, height=h, width=w)
nom.grid(row=1,column=1)
heronamenew=Label(nom,text="Entrez votre nom si vous êtes un nouveau joueur", font="Sylfaen 16 bold")
heronamenew.grid(row=1,column=1)
heroname=StringVar()
Champheroname=Entry(nom, textvariable=heroname, font="Sylfaen 16")
Champheroname.grid(row=2,column=1,pady=10)
Commencer=Button(nom,text="Commencer !",font="Sylfaen 14",overrelief ="ridge",command=choixmob)
Commencer.grid(row=3,column=1,pady=10)
heronameold=Label(nom, text="Chargez votre sauvegarde si vous avez déjà jouer", font="Sylfaen 16 bold")
heronameold.grid(row=4, column=1, pady=10)
#Lis les fichiers que contient le dossier "SAVE"
listfich=os.listdir("SAVE")
#Compte le nombre de fichier contenu dans le dossier "SAVE"
nbrfich=len(listfich)
#Un compteur, on le met sur -1 au lieu de 0 pour qu'il soit au même rang que k dans la boucle for
n=-1
#Correspond à la ligne à laquelle sera créer les boutons, la valeur est sur 5 car les autres boutons créés manuellement vont jusqu'a row=4
rown=5
#2 listes stockant les boutons afin de pouvoir les manipuler dans le chargement/suppression de sauvegarde
BSave=[]
BPoub=[]
#Boucle for allant de 0 au nombre de fichier
for k in range (0,nbrfich):
    #Augmente n de 1
    n=n+1
    #Ajoute dans la liste de Sauvegarde un bouton correspondant à la sauvegarde lue, et on lui met "k" en nom afin de pouvoir modifié le bouton dans opensave()
    BSave.append(Button(nom, text=(listfich[n].replace(".txt","")), font="Sylfaen 16",overrelief="ridge", name=str(k)))
    BSave[k].grid(row=rown, column=1,pady=3)
    #De même pour le bouton poubelle, mais avec comme nom "Poub k"
    BPoub.append(Button(nom, image=Poub,overrelief="ridge", name=("poub"+str(k))))
    BPoub[k].grid(row=rown, column=2, pady=3)
    rown=rown+1
#Les 3 évènements nécessaire à la manipulation des boutons
nom.bind_all('<ButtonPress-1>', opensave)
nom.bind_all('<Enter>', affistatsave)
nom.bind_all('<Leave>', desaffistatsave)


Jeu.mainloop()
