(* GRADE:  100% *)
(* Exercice n°3 *)

(* Q1 *)
let nb_ingredients (rdic: dico) (r: string):int = 
  (List.length (List.assoc r rdic))

(* Q2 *)
let rec recette_avec (rdic:dico) (i:string): string list =
  match rdic with
    []->[]
  |(nom,_)::rdic2-> if (List.mem i (List.assoc nom rdic)) then nom::(recette_avec rdic2 i)
      else (recette_avec rdic2 i)
  

(* Q3 *)
let rec recette_sans (rdic:dico) (i:string): string list =
  match rdic with
    []->[]
  |(nom,_)::rdic2-> if (List.mem i (List.assoc nom rdic)) then (recette_sans rdic2 i)
      else nom::(recette_sans rdic2 i)
                
(* Q4 *)
let rec union (xs:'a list) (ys:'a list) : 'a list=
  match xs with
    []->ys
  |x::xs2 -> if (List.mem x ys)||(List.mem x xs2) then (union xs2 ys)
      else x::(union xs2 ys)

(* Q5 *)
let rec tous_ingredients (rdic:dico) : string list=
  match rdic with
    []->[]
  |(nom,_)::rdic2->(union (List.assoc nom rdic) (tous_ingredients rdic2))

(* Q6 *)
let dico_ingredients (rdic : dico) : dico=
  let ing = (tous_ingredients rdic) in
  let rec loop (ling: string list) (rdic:dico):dico=
    match ling with
      []->[]
    |i::ling2->(i,(recette_avec rdic i))::(loop ling2 rdic)
  in
  (loop ing rdic)

(* Q7 *)
let ingredient_principal (idic:dico):string=
  let rec loop (xs:dico) (r:string) (n:int):string=
    match xs with
      []->r
    |(ing,xi)::xs2->let k=(List.length xi) in
        if k>n then (loop xs2 ing k) 
        else (loop xs2 r n)
  in
  match idic with
    []->raise(Invalid_argument "idic")
  |(ing, xi)::xs->(loop xs ing (List.length xi))


