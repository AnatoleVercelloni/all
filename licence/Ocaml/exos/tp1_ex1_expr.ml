(* GRADE:  100% *)
(3 * 5) + 2;; (* type: int, valeur: 17*)

((fun x -> 2 * x) 7);; (* type: int, valeur: 14*)

((fun x -> 2 * x) (3 * 5));; (*type: int, valeur: 30*)

(((fun x -> (fun y -> x * y)) 3) 7);; (*type: int, valeur: 21*)

((fun x -> fun y -> x * y) 3 7);; (*type: int, valeur: 21*)

(fun f -> fun x -> (f x) + x) (fun x -> x - 1) 3;; (*type: int, valeur: 5*)

let (x, y) = (1, 2) in x + y;; (*type: int, valeur: 3*)

let a = (1, 2) in
let (x, y) = a in x + y;; (*type: int, valeur: 3*)

let f x = x + 1 in (f, 3);; (*type: (int->int)*int, valeur: (fonction, 3)*)

let b = true in
if b then (fun x -> x) else (fun x->0);; (*type: int->int, valeur: 
                                         fonction identité ou nulle, 
                                         on ne peut pas affecter 0 
                                         directement car son type est int 
                                         et non pas int->int*) 

let b = true in ((if b then (fun x -> x + 1) else (fun x -> x - 1)) 5);; (*type: int, valeur: 6*)

((fun b ->((fun x -> fun y -> 2 * x + 3 * y) (if b then 1 else 2) 5)) true);; (*type: int, valeur: 17*)

let f = fun x -> not x in
let g = fun f -> fun x -> fun y -> (f (not x)) && (f y) in
(g f true false);; (*type: bool, valeur: true*)

