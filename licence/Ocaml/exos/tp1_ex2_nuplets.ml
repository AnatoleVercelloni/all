(* GRADE:  100% *)

(* Q1 *)
let fst p =
  let (a,b) = p in a

let snd p =
  let (a,b) = p in b
(* Q.2 *)
let paire a b=
  (a,b) 
  
(* Q.3 *)
let paire_true a=
  (true, a)
  
(* Q.4 *)
let curry f =
  let g x y = f (x, y) in g 
  
(* Q.5 *)
let uncurry g =
  let f (x,y) = g x y in f
