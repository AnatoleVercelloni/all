(* GRADE:  100% *)

let rec list_impair (ns:int list) : int list =
  match ns with
    []->[]
  | x::xs -> if x mod 2 = 1 then x::(list_impair xs)
      else list_impair xs

let rec list_non_nulle (xs:string list) : string list =
  match xs with
    []->[]
  | c::cs -> if String.length c =0 then list_non_nulle cs
      else c::(list_non_nulle cs)

let rec list_interval (ns:int list) : int list = 
  match ns with
    []->[]
  | x::xs -> if x>=(-10) && x<=10 then x::(list_interval xs)
      else list_interval xs

let rec list_non_vide (xss:('a list) list) : ('a list) list =
  match xss with
    []->[]
  | y::ys -> if y=[] then list_non_vide ys
      else y::(list_non_vide ys)

let rec list_non_0 (nss:(int list) list) : ('int list) list =
  match nss with
    []->[]
  | x::xs -> if (List.mem 0 x) then list_non_0 xs
      else x::(list_non_0 xs)

let rec list_sum_tuple (cs:(int * int) list) (s:int) : (int * int) list =
  match cs with
    [] -> []
  | x::xs -> let (a,b)=x in 
      if a+b >= s then x::(list_sum_tuple xs s)
      else list_sum_tuple xs s

