(* GRADE:  100% *)
(* Q1 *)
let rec less_divider (i:int) (n:int) : int =
  (*hypothèse: i<=n, i > 0, n > 0*)
  if n=i then 0
  else if n mod i = 0 then i
  else (less_divider (i+1) n)

(* Q2 *)
let prime (n:int) : bool = 
  if n=1 then false
  else ((less_divider 2 n)=0)

(* Q3 *)
let rec next_prime (n:int) : int=
  if (prime n) then n
  else (next_prime (n+1))
  

(* Q4  *)
let nth_prime (n:int) : int = 
  let rec loop i k =
    if i=n then (next_prime k)
    else (loop (i+1) (next_prime k+1))
  in
  (loop 0 2)

