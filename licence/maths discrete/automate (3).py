# -*- coding: utf-8 -*-
from transition import *
from state import *
import os
import copy
from sp import *
from myparser import *
from itertools import product
from automateBase import AutomateBase
import itertools


# binome : César Mathéus et Anatole Vercelloni

# les fonctions extract, contient_liste, contientInitial,contientFinal et lab sont uniquement utilisées dans la fonction déterminisation
#on a cree ces fonctions pour rendre le code plus lisible






"""cette fonction est utilisée dans la fonction déterminisation afin de savoir si un état de l'automtate déterminisé doit être final
ou non. Un état est final si un des états de l'automate indéteimport itertoolsrministe qu'il représente est final"""
def contientFinal(auto, ens):
    """ Automate x set(State) -> bool
    rend True si ens contient un état final, False sinon
    """
    liste_etat_final = auto.getListFinalStates()
    for elt in ens : 
        if elt in liste_etat_final:
            return True
    return False
def contient_liste(l):
    for e in l:
        if type(e)== list:
            return True
    return False


def extract(l):
    res = [e for e in l]
    cond = contient_liste(res)
    while cond : 
        l_temp = []
        for i in range(len(res)):
            if type(res[i])== list:
                for e in lf[i]:
                    l_temp.append(e)
            else:
                res = [e for e in l_temp ]
            cond = contient_liste(res)
    return res



#fonction ayant surtout un impact sur l'affichage de l'automate, elle permet de créer un label pour chaque état de l'automate résultat de la fonction determinisation
def lab(ensemble_etat):
    """ set<State> -> str
    rend un label pour etat correspondant à l'ensemble des etiquettes des éléments de ensemble_etat
    """
    res = "{"
    for s in ensemble_etat :
        res = res + str(s.id) + ","
    res = res[0:len(res)-1] 
    return res + "}"


#fonction pour l affichage des labels dans union et intersection
def labbis(tuple_state):
    return "(" + str(tuple_state[0].id) + "," +str(tuple_state[1].id) + ")"





def getListTransitionsTo(auto, st):
    """ Automate*State-> list[Transition]
    retourne la liste des transitions allant à l'état state
    """
    l= []
    
    for s in auto.listStates:
        for t in auto.getListTransitionsFrom(s):
            if t.stateDest == st:
               l.append(t)
    return l


class Automate(AutomateBase):
        
#renvoie la liste des états successeurs pour une liste déats et un caractère donné, pour ce faire on parcours 
#la liste détas passée en paramètre et on applique la fonction succelem à chauqe élément de cette liste
    def succ(self,L,a):
        """ Liste[State]*str ->Liste[state]"""

        #res : Liste[State]
        res = []
        # taille : int
        taille = len(L)
        for i in range(taille):
            res = res + self.succElem(L[i],a)
        return list(set(extract(res)))
    
    #pour la fonction accepte, on construit la liste des états dans lequel on peut se retrouver enfin de lecture du mot passé en 
    #parmètre sur l'automate self.si un des états de cette liste est final, alors le mot est accepté 
    def accepte(self,mot):
        """str -> bool"""

        # taille : int
        taille = len(mot)

        #temp : Liste[State]
        temp = self.succ(self.getListInitialStates(),mot[0])
        if mot == "":
            for i in self.getListInitialStates():
                if i.init :
                    return True
                return False
        for i in range (1,taille):
            temp = self.succ(temp,mot[i])
    
        for j in range(len(temp)):
            if temp[j] in self.getListFinalStates():
                print("le mot passé en paramètre est accepté par l'automate")
                return True

        print("le mot passé en paramètre n'est pas  accepté par l'automate")
        return False


        

    def succElem(self, state, lettre):
        """State x str -> list[State]
        rend la liste des états accessibles à partir d'un état
        state par l'étiquette lettre
        """
        successeurs = []
        # t: Transitions
        for t in self.getListTransitionsFrom(state):
            if t.etiquette == lettre and t.stateDest not in successeurs:
                successeurs.append(t.stateDest)
        return successeurs


  


   

#Pour cette fonction on parcours la liste d'état de notre automate, pour chaque état on créée l'ensemble des étiquettes des transitions
#qui partent de cet état, si pour chaque état, cet ensemble est différend de l'alphabet, l'automate n'est pas complet (car il manque des transitions) 
    @staticmethod
    def estComplet(auto,alphabet) :
        """ Automate x str -> bool
         rend True si auto est complet pour alphabet, False sinon
        """

        #setalphabet : set<str>
        setalphabet = set()
        for a in alphabet:
            setalphabet.add(a)
        # temp : set<str>
        temp = set()
        len1 = len(auto.listStates) 
        for i in range(len1):
            for j in range(len(auto.getListTransitionsFrom(auto.listStates[i]))):
               temp.add(auto.getListTransitionsFrom(auto.listStates[i])[j].etiquette)
            if temp != setalphabet :
                print("l'automate n'est pas complet pour l'alphabet passé en paramètre")
                return False
            temp = set()
        print("l'automate est complet pour l'alphabet passé en paramètre")
        return True


#pour la fonction estDeterministe, on parcours la liste d'états de l'automate passé en paramètre, pour chaque état on créée 
#l'ensemble des étiquettes des transitions qui partent de cet état. On regarde si le cardinal de cette ensemble est plus petit que le nombre
#d'élément de la liste des transitions qui partent de ce même ensemble. si ce cardinal est inférieure, c'est qu'il y a au moins un doublon dans 
#la liste de transitions (cad deux transitions différentes ayant la même étiquettes) 
    @staticmethod
    def estDeterministe(auto) :
        """ Automate  -> bool
        rend True si auto est déterministe, False sinon
        """
        #temp : set<str>
        if (len(auto.getListInitialStates())>1):
            print("l'automate n'est pas deterministe")
            return False
        
        temp = set()
        for i in range(len(auto.listStates)):
            for j in range(len(auto.getListTransitionsFrom(auto.listStates[i]))):
               temp.add(auto.getListTransitionsFrom(auto.listStates[i])[j].etiquette)
            if len(temp)<len(auto.getListTransitionsFrom(auto.listStates[i])):
                print("l'automate n'est pas deterministe")
                return False
            temp = set()
        print("l'automate est deterministe")
        return True
        
#Pour compléter un automate, on reprend le code de la fonction estComplet, on parcours la liste d'état de l'automate
#et dès que l'on trouve un automate depuis lequel il manque une transition pour un élément l de l'alphabet, on créer une nouvelle transition
#allant de cet état vers un nouvel état, non final, et d'étiquette l.on crée allors des transitions de cet état vers lui-même pour toute les éléments de
#l'alphabet associé à l'automate. 
       
    @staticmethod
    def completeAutomate(auto,alphabet) :
        """ Automate x str -> Automate
        rend l'automate complété d'auto, par rapport à alphabet
        """

        #res : Automate
        res = copy.deepcopy(auto) 
        #trouve : bool
        trouve = False
        #temp :transition
        #taile : int
        taille = len(res.listStates)
        if not Automate.estComplet(res,alphabet):
            for i in range(taille):
                for s in alphabet: 
                    for j in range(len(res.getListTransitionsFrom(res.listStates[i]))):                   
                        if (s == res.getListTransitionsFrom(res.listStates[i])[j].etiquette) :
                            trouve =  True
                    if not(trouve) :
                        res.addState(State(-1,False,False))
                        res.addTransition(Transition(res.listStates[i],s,res.listStates[(len(res.listStates)-1)]))  
                    for a in alphabet : 
                        res.addTransition(Transition(res.listStates[(len(res.listStates)-1)],a,res.listStates[(len(res.listStates)-1)]))

                trouve = False
        return res 

       
#le principe de la fonction determinisation est le suivant:
#on associe chaque état de l'autmoate determinisé à un ensemble d'état de l'automate passé en paramètre.
#on crée "manuellement " l'état initial, qui correspond à l'ensemble des états initiaux de l'automate passé en paramètre 
#puis on fonctionne de proche, pour chaque ensemble d'état s, on regarde toute les transitions possibles pour chaque élément de notre 
#alphabet telles que les éléments de s soient les états de départs de ces transitions. On rassemblent alors les états "d'arrivées" de 
#ces transitions et on les regroupe dans un ensemble d'état  s' alors, deux cas sont possibles :
#- cet ensemble d'état n'existe pas, on crée donc  un état qui le représente dans l'automate déterministe (on ajoute cet ensemble 
#d'état à notre liste d'ensemble d'état)et on crée une nouvelle transition de l'état qui représente s vers l'état
#que l'on vient de créée s'

#- cet ensemble existe déjà dans notre liste d'ensemble d'état, alors on se contente d'ajouter la transition de s vers s'

#chaque ensemble détat créée est ajouté à une seconde liste que l'on parcours, à chaque parcours on lui retire son premier élément, et la fonction
 #et la boucle termine lorsque la liste est vide, cad lorsque on a bien passé en revu chaque ensemble d'état """
    @staticmethod
    def determinisation(auto) :
        """ Automate  -> Automate
        rend l'automate déterminisé d'auto
        """
        #cpt : int
        cpt = 1
        auto_res = Automate([])
         #alphabet : set<str>
        alphabet = set()
        for k in range(len(auto.listTransitions)):
            alphabet.add(auto.listTransitions[k].etiquette) # on cree l'alphabet associé à l'automate

        #listeState : list[set(State)] la liste d'ensemble d'état dont chaque élément va être associé à un état de l'automate résultat
        listeState = [set(auto.getListInitialStates())]

        #listeSuivant : list[set(State)]  liste utilisée pour parcourir les états de notre automate de départ
        listeSuivant = [set(auto.getListInitialStates())]

        #on créé l'état initial : 
        auto_res.addState(State(0, True, contientFinal(auto, set(auto.getListInitialStates())),lab(set(auto.getListInitialStates()))))

        while len(listeSuivant) != 0:
            #ed : set(State), 
            ed = listeSuivant.pop(0)
            for l in alphabet:
                #ef  set(State), l'ensemble des états x tels que la transition eif,l,x existe, où eif est un élément de ef
                ef = set(auto.succ(list(ed), l))
                if ef not in listeState:
                    listeState.append(ef)
                    auto_res.addState(State(cpt,False, contientFinal(auto, ef),lab(ef)))# ajout d'un état à l'automate résultat
                    cpt += 1 # nouvel état, donc incrémentation du compteur de nombre d'état
                    listeSuivant.append(ef)
                i_f = listeState.index(ef)
                i_d = listeState.index(ed)
                auto_res.addTransition(Transition(auto_res.listStates[i_d], l, auto_res.listStates[i_f]))# ajout d'une transition à l'automate résultat
        return auto_res
        
    @staticmethod
    def complementaire(auto,alphabet):
        """ Automate -> Automate
        rend  l'automate acceptant pour langage le complémentaire du langage de a
        """
        auto_res = Automate([])
        auto_res = determinisation(completeAutomate(auto))
        for i in range(len(auto_res.listeState)):
            if (auto_res.listeState[i].fin):
                auto_res.listeState[i].fin = False
            else :
                 auto_res.listeState[i].fin = True

        return  auto_res


   
    @staticmethod
    def intersection (auto0, auto1):
        """ Automate x Automate -> Automate
        rend l'automate acceptant pour langage l'intersection des langages des deux automates
        """

        """cette fonction a la meme structure que la fonctiondeterminisation, en representant les
            etats de l'automate resulatat comme des couples d états de auto0 et auto1"""
        cpt = 0
        auto_res = Automate([])
        alphabet = set()
        for k in range(len(auto0.listTransitions)):
            alphabet.add(auto0.listTransitions[k].etiquette) 
        
        for k in range(len(auto1.listTransitions)):
            alphabet.add(auto1.listTransitions[k].etiquette) # on cree l'alphabet associé à l'automate

        L1 = auto0.getListInitialStates()
        L2 = auto1.getListInitialStates()
        L = list(itertools.product(L1,L2))
        i = 0
        for elt in L : 
            auto_res.addState(State(cpt,True, (elt[0].fin and elt[1].fin), labbis(elt)))
            cpt+=1
        liste_a_traiter = list(L)
        while (len(liste_a_traiter)!=0):
            temp = liste_a_traiter.pop()
            
            for c in alphabet : 
                if(len(auto0.succElem(temp[0],c))!=0  or  len(auto1.succElem(temp[1],c))!=0) : #cette ligne est tres importante, c'est ce test qui assure qu'in ne traite que des états atteignables
                    L1 = auto0.succElem(temp[0],c)
                    L2 = auto1.succElem(temp[1],c)
                    L_temp =  list(itertools.product(L1,L2))
                else :
                    L_temp = []
                for elt in L_temp : 
                    if (elt not in L):
                        L.append(elt)
                        auto_res.addState(State(cpt,(elt[0].init and elt[1].init),(elt[0].fin and elt[1].fin),labbis(elt)))
                        cpt+=1
                        liste_a_traiter.append(elt)
                    i_f = L.index(elt)
                    i_d = L.index(temp)
                    auto_res.addTransition(Transition(auto_res.listStates[i_d],c,auto_res.listStates[i_f]))
        return auto_res

    @staticmethod
    def union (auto3, auto4):
        """ Automate x Automate -> Automate
        rend l'automate acceptant pour langage l'union des langages des deux automates
        """
        """fonction presque identique à intesrection, on construit au préalable des automates complets"""
        alphabet = set()

        for k in range(len(auto3.listTransitions)):
            alphabet.add(auto3.listTransitions[k].etiquette)  
        for k in range(len(auto4.listTransitions)):
            alphabet.add(auto4.listTransitions[k].etiquette) # on cree l'alphabet associé à l'automate
        alphabetbis = ""
        for a in alphabet:
        	alphabetbis += a

        auto0 = Automate.completeAutomate(auto3,alphabetbis)
        auto1 = Automate.completeAutomate(auto4,alphabetbis)

        cpt = 0
        auto_res = Automate([])
        

        L1 = auto0.getListInitialStates()
        L2 = auto1.getListInitialStates()
        L = list(itertools.product(L1,L2))
        i = 0
        for elt in L : 
            auto_res.addState(State(cpt,True, (elt[0].fin or elt[1].fin), labbis(elt)))#ici un or sur le conditionfinal
            cpt+=1
        liste_a_traiter = list(L)
        while (len(liste_a_traiter)!=0):
            temp = liste_a_traiter.pop()
            
            for c in alphabet : 
                if(len(auto0.succElem(temp[0],c))!=0  or  len(auto1.succElem(temp[1],c))!=0) : 
                    L1 = auto0.succElem(temp[0],c)
                    L2 = auto1.succElem(temp[1],c)
                    L_temp =  list(itertools.product(L1,L2))
                else :
                    L_temp = []
                for elt in L_temp : 
                    if (elt not in L):
                        L.append(elt)
                        auto_res.addState(State(cpt,(elt[0].init and elt[1].init),(elt[0].fin or elt[1].fin),labbis(elt)))#encore un or sur la condition final
                        cpt+=1
                        liste_a_traiter.append(elt)
                    i_f = L.index(elt)
                    i_d = L.index(temp)
                    auto_res.addTransition(Transition(auto_res.listStates[i_d],c,auto_res.listStates[i_f]))
        return auto_res

        #return Automate.intersection(Automate.completeAutomate(auto0,alphabet),Automate.completeAutomate(auto1,alphabet))
         

   
       

    @staticmethod
    def concatenation (auto1, auto2):
        """ Automate x Automate -> Automate
        rend l'automate acceptant pour langage la concaténation des langages des deux automates
        """
        auto_res = copy.deepcopy(auto1)
        cpt = len (auto1.listStates)
        l = auto2.getListInitialStates()
        ls = []
        
        
        for i in range(len(l)):
            ls.append(State(cpt,True,(l[i]).fin))
            auto_res.addState(ls[i])
            #On ajoute les états initiaux de auto 2 à auto_res
            for s in auto1.getListFinalStates():
                for t in getListTransitionsTo(auto1,s):
                # Pour chaque état final de auto1, pour chaque transition allant vers un etat final, on la  reproduit vers chaque état initial de auto_2
                    auto_res.addTransition(Transition(t.stateSrc,t.etiquette,ls[i]))
            cpt = cpt + 1
        ls = []
        cpt = cpt-i
        #On rajoute les états non initiaux de auto2 à l'automate résulat 
        
        for i in range (len(auto2.listStates)):
            ls.append(State(cpt,False,((auto2.listStates)[i]).fin))
            cpt = cpt + 1
            if (auto2.listStates[i]).init == False :
                auto_res.addState(ls[i])
        for i in range (len(auto2.listStates)):
            for t in auto2.getListTransitionsFrom((auto2.listStates)[i]):
                if (ls[(auto2.listStates).index(t.stateSrc)]  in auto_res.listStates) & (ls[(auto2.listStates).index(t.stateDest)]  in auto_res.listStates):
                    auto_res.addTransition(Transition(ls[(auto2.listStates).index(t.stateSrc)],t.etiquette,ls[(auto2.listStates).index(t.stateDest)]))
        return auto_res
        
        
       
    @staticmethod
    def etoile (auto):
        """ Automate  -> Automate
        rend l'automate acceptant pour langage l'étoile du langage de a
        """
        return




