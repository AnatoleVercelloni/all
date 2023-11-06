(* GRADE:  100% *)
(* Exercice n°2 *)

(* Q1 *)
let rec sublac (xs :'a list) (ys: 'a list) : bool=
  match (xs,ys) with
    ([],_)->true
  |(x::xs2, [])->false 
  |(x::xs2, y::ys2) -> if x=y then (sublac xs2 ys2) 
      else (sublac xs ys2)

(* Q2 *)
let rec sublying (xs: int list) (ys: int list): bool = 
  match (xs, ys) with
    ([], [])->true
  |(_,[])->false
  |([],_)->false
  |(x::xs2, y::ys2)->if x=y || x=0 then (sublying xs2 ys2)
      else false

(* Q3 *)
let rec stretch (xs: 'a list) (ys: 'a list) : 'a list = 
  match (xs, ys) with
    ([], [])->[] 
  |([], y::ys2)->0::(stretch xs ys2)
  |(_,[])->raise(Invalid_argument "stretch")
  |(x::xs2, y::ys2)->if x=y then x::(stretch xs2 ys2)
      else 0::(stretch xs ys2)

