(* GRADE:  100% *)
(* Q1 *)
let application (f : ('a -> 'b)) (x : 'a) =
  (f x)



(* Q2 *)
let composition (f : ('b -> 'c)) (g : ('a -> 'b)) (x : 'a) : 'c =
  (f (g x))



(* Q3 *)
let f_ou_ident (f : ('a -> 'a)) (b : bool) : 'a -> 'a =
  if b then (fun x->x) else f

