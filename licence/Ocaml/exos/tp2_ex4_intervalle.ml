(* GRADE:  100% *)
(* Q1 *)
let rec sum_inter (a:int) (b:int) : int =
  if a>b then 0
  else a + (sum_inter (a+1) b)

(* Q2 *)
let rec sum1_inter (k:int) (a:int) (b:int) : int =
  if a>b then 0
  else k + a + (sum1_inter k (a+1) b)

(* Q3 *)
let sum2_inter (a:int) (b:int) : int =
  let rec loop k =
    if k > b then 0
    else (sum1_inter k a b) + (loop (k+1))
  in
  (loop a)
