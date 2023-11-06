(* GRADE:  100% *)
(* Q1 *)
let rec sum_n (n:int) : int =
  if n=0 then 0 
  else n + (sum_n (n-1))

(* Q2 *)
let rec sum_n2 (n:int) : int =
  if n<0 then raise (Invalid_argument "sum_n")
  else
  if n=0 then 0 
  else n + (sum_n2 (n-1))

(* Q3 *)
let rec sum_p (n:int) : int =
  if n = 0 then 0
  else n*2+ (sum_p (n-1))
      
(* Q4 *)
let rec sum_f (f : int -> int) (n:int) : int =
  if n= 0 then (f 0) 
  else (f n)+ (sum_f f (n-1))

let sum_p2 (n:int) : int = 
  let f n= 2*n  in
  (sum_f f n)

let _= assert ((sum_p 10)=(sum_p2 10))
