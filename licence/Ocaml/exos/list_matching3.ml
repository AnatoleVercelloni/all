(* GRADE:  100% *)
    
let hd_fst (xs:('a*'b) list) : 'a =
  match xs with
    []-> raise Not_found
  |x::ys -> let (a,b) = x in a
    
let swap_hd_fst (xs:('a*'a) list) : ('a*'a) list =
  match xs with 
    []-> []
  |x::ys -> let (a,b) = x in (b,a)::ys
    
let hd_hd (xs:('a list) list) : 'a =
  match xs with
    []->raise Not_found
  |x::ys -> match x with
      []->raise Not_found
    |y::zs -> y
    
let rem_hd_hd (xs:('a list) list) : (int list) list =
  match xs with
    []->[]
  |y::ys -> match y with
      []->xs
    |y::zs -> zs::ys

  

