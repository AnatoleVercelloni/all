(* GRADE:  100% *)

let rec prod (xs:float list) : float =
  match xs with
    []->1.0
  |x::ys -> x *. (prod ys)

let rec sum_round (xs:float list) : int =
  match xs with
    [] -> 0
  |x::ys -> (int_of_float x) + (sum_round ys)

let rec parenthese (xs:string list) : string =
  match xs with 
    [] -> ""
  |x::ys -> "("^x^")"^(parenthese ys)

let rec flatten (xss:('a list) list) : 'a list =
  match xss with
    []->[]
  | x::ys -> x @ (flatten ys)

let rec sum_tuple (cs:(int*int) list) : int =
  match cs with
    []->0
  |x::xs -> let (a,b) = x in a + b + (sum_tuple xs)

let rec reduce (f:'a -> 'b -> 'b) (xs:'a list) (b:'b) : 'b =
  match xs with
    [] ->b
  |x::ys -> (f x (reduce f ys b))
  


