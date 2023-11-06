(* GRADE:  100% *)

(* Q1 *)
let inverse_i (xs:int list) : float list = 
  let f (x:int):float =
    if x=0 then 0.
    else
      1./.(float_of_int x)
  in
  (List.map f xs)

(* Q2 *)
let list_sum_tuple (cs:(int*int) list) (s:int) : (int*int) list =
  let f (x:(int*int)): bool=
    let (a,b) = x in
    (a+b>=s)
  in
  (List.filter f cs )

(* Q3 *)
let parenthese (xs:string list) : string =
  let f (x:string) (a:string):string=
    "("^x^")"^a
  in
  (List.fold_right f xs "")

(* Q4 *)
let list_non_0 (nss:(int list) list) : (int list) list =
  let f (xs:int list):bool=
    not (List.mem 0 xs)
  in
  (List.filter f nss)

(* Q5 *)
let dpoints (xs:int list) (a:int) (b:int) : (int*int) list =
  let f (x:int):(int*int)=
    (x,a*x+b) 
  in
  (List.map f xs)

(* Q6 *)
let prod_sum_tuple (cs:(int*int) list) : int =
  let f (a:int) (x:(int*int)) =
    let (x1,x2)=x in (x1+x2)*a
  in
  (List.fold_left f 1 cs)
    


  

