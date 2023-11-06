(* GRADE:  100% *)
(* Q1 *)
let rec merge (xs:'a list) (ys:'a list) : 'a list =
  match xs with 
    [] -> ys
  |x::xs2 -> match ys with 
      [] -> xs
    |y::ys2 -> if x < y then x::(merge xs2 ys)
        else y::(merge xs ys2)
                

(* Q2 *)
let rec split (xs:'a list) : ('a list * 'a list) = 
  match xs with 
    []->([],[]) 
  | x::[] -> ([x], [])
  |x::y::ys -> let (a,b) = (split ys) in (x::a, y::b)

(* Q3 *)
let rec merge_sort (xs:'a list) : 'a list =
  match xs with 
    [] -> []
  | x::[] -> xs
  | _ -> let (xa, xb)= (split xs) in
      merge (merge_sort xa) (merge_sort xb)

(* Q4 *)
let rec merge_gen (cmp:'a -> 'a -> bool) (xs:'a list) (ys:'a list) : 'a list =
  match xs with 
    [] -> ys
  |x::xs2 -> match ys with 
      [] -> xs
    |y::ys2 -> if (cmp x y) then x::(merge_gen cmp xs2 ys)
        else y::(merge_gen cmp xs ys2)
                
  
(* Q5 *)
let rec merge_sort_gen (cmp:'a -> 'a -> bool) (xs:'a list) : 'a list =
  match xs with 
    [] -> []
  | x::[] -> xs
  | _ -> let (xa, xb)= (split xs) in
      merge_gen cmp (merge_sort_gen cmp xa) (merge_sort_gen cmp xb)

(* Q6 *)
let sort (xs:(int*int) list) : (int*int) list =
  let cmp (x: (int*int)) (y:(int*int)): bool = 
    let (x1, x2) = x in 
    let (y1, y2) = y in
    if x1 + x2 < y1 + y2 then true
    else false 
  in
  merge_sort_gen cmp xs
    

