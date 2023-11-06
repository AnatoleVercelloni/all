(* GRADE:  100% *)

let rec inverse_f (xs:float list) : float list = 
  match xs with 
    []->[]
  | x::ys-> (1.0/.x)::(inverse_f ys)

let rec inverse_i (ns:int list) : float list =
  match ns with 
    []->[]
  | x::xs-> (1.0/.(float_of_int x))::(inverse_i xs)
                      
let rec ecrete (xs:int list) : int list =
  match xs with
    []-> []
  |x::ys -> if x>10 then 10::(ecrete ys)
      else if x< -10 then (-10)::(ecrete ys)
      else x::(ecrete ys)

let rec dpoints (xs:int list) (a:int) (b:int) : (int*int) list =
  match xs with
    []->[]
  |x::ys -> (x, a*x + b)::(dpoints ys a b)

let rec app_list (f:'a -> 'b) (xs:'a list) : 'b list =
  match xs with
    []->[]
  |x::ys -> (f x)::(app_list f ys)

