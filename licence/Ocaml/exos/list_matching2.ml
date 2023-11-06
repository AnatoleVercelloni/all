(* GRADE:  100% *)
let snd (xs:'a list) : 'a =
  match xs with
    []-> raise Not_found
  |x::[]->raise Not_found
  |x::y::ys -> y
    
let swap_hd_snd (xs:'a list) : 'a list =
  match xs with 
    []-> xs
  |x::[]->xs
  |x::y::ys -> y::x::ys 
    
let hd_0 (xs:int list) : bool =
  match xs with
    []->false
  |x::ys-> x = 0
    
let eq_hd (x:'a) (xs:'a list) : bool =
  match xs with 
    []->false
  |y::ys -> y = x
     
    

  

