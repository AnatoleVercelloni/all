(* GRADE:  100% *)


(* Q1 *)
let rec map_filter (f:'a -> 'b) (p:'b -> bool) (xs:'a list) : 'b list =
  match xs with 
    []->[]
  |x::xs2->let k=(f x) in
      if (p k) then k::(map_filter f p xs2)
      else (map_filter f p xs2)

(* Q2 *)
let rec filter_map (p:'a -> bool) (f:'a ->  'b) (xs:'a list) : 'b list =
  match xs with
    []->[]
  |x::xs2 -> if (p x) then (f x)::(filter_map p f xs2)
      else (filter_map p f xs2)

(* Q3 *)
let rec map_foldr (f1: 'b -> 'c -> 'c) (f2:'a -> 'b) (xs:'a list) (z:'c) :'c =
  match xs with
    []->z
  |x::xs2->(f1 (f2 x) (map_foldr f1 f2 xs2 z)) 

(* Q4 *)
let rec map_foldl (f1: 'c -> 'b -> 'c) (z:'c) (f2:'a -> 'b) (xs:'a list) : 'c =
  match xs with
    []->z
  |x::xs2->(map_foldl f1 (f1 z (f2 x)) f2 xs2)  
  
(* Q5 *)
let rec filter_foldr (f:'a -> 'b -> 'b) (p:'a -> bool) (xs:'a list) (z:'b) : 'b =
  match xs with
    []->z
  |x::xs2 -> if (p x) then (f x (filter_foldr f p xs2 z))
      else (filter_foldr f p xs2 z)

(* Q6 *)
let rec filter_foldl (f:'b -> 'a -> 'b) (z:'b) (p:'a -> bool) (xs:'a list) : 'b =
  match xs with
    []->z
  |x::xs2-> if (p x) then (filter_foldl f (f z x) p xs2)
      else filter_foldl f z p xs2
  

