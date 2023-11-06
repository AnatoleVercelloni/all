(* GRADE:  100% *)
(* Q1 *)
let rec repeat (n:int) (x:'a) : 'a list  = 
  if n <=0 then []
  else x::(repeat (n-1) x)


(* Q2 *)
let rec range_i (i:int) (j:int) : (int list) =
  if i>j then []
  else i::(range_i (i+1) j)

(* Q3 *)
let rec range_n (x:int) (n:int) : (int list) =
  if n <= 0 then []
  else x::(range_n (x+1) (n-1))







