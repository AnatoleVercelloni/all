(* GRADE:  100% *)
(* Exercice n°1 *)

(* Q1 *)
let rec drop (n:int) (xs:'a list) : ('a list) =
  if n<=0 then xs 
  else match xs with
      []->[]
    |x::ys -> (drop (n-1) ys)
  

(* Q2 *)
let rec take (n:int) (xs: 'a list) : ('a list) =
  if n<=0 then []
  else match xs with
      [] -> []
    |x::ys -> x::(take (n-1) ys)

(* Q3 *)
let sub (xs: 'a list) (start: int) (len: int) : ('a list)=
  (take len (drop start xs))

