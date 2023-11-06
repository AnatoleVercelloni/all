(* GRADE:  100% *)
let rec intercale1 (z:'a) (xs:'a list) : 'a list =
  match xs with
    []->[]
  |x::[]-> xs
  |x::ys-> x::z::(intercale1 z ys)
    
let rec intercale2 (z:'a) (xs:'a list) : 'a list =
  match xs with
    []->z::[]
  |x::[]-> z::x::z::[]
  |x::ys-> z::x::(intercale2 z ys)
    
let rec begaie (xs:'a list) : ('a list) =
  match xs with
    []->[] 
  |x::ys-> x::x::(begaie ys)

let rec oublie1 (xs:'a list) : ('a list) =
  match xs with
    []->[]
  |x::[]->xs
  |x::y::ys -> x::(oublie1 ys)

let rec oublie2 (xs:'a list) : ('a list) =
  match xs with
    []->[]
  |x::[]->[]
  |x::y::ys -> y::(oublie2 ys)



  

