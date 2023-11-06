(* GRADE:  100% *)
(* Q1 *)
let f (a:float) (x:float) : float =
  (1./.2.) *. (x +. (a/.x))

(* Q2 *)
let rec sqrt_n (n:int) (a:float) (x0:float) =
  if n=0 then x0
  else (f a (sqrt_n (n-1) a x0))

(* Q3 *)
let eq_eps (e:float) (x:float) (y:float) : bool =
  let abs (x:float): float= 
    if x>=0. then x
    else -.x 
  in 
  ((abs (x-.y))<e)

(* Q4 *)
let sqrt_x (e:float) (a:float) (x0:float) : float =
  let rec loop x=
    let y=(f a x) in
    if (eq_eps e x y) then y
    else (loop (f a x))
  in 
  (loop x0)

