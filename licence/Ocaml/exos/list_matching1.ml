(* GRADE:  100% *)
let len_eq_3 (xs:'a list) : bool =
  match xs with
    x::y::z::[ ] -> true 
  | _ ->false
    

let len_ge_3 (xs:'a list) : bool =
  match xs with
    [ ] -> false
  |x::[]->false
  |x::y::[ ]->false
  |x::y::ys->true 
  
let len_lt_3 (xs:'a list) : bool =
  match xs with 
    [ ] -> true
  |x::[]->true
  |x::y::[ ]->true
  |_->false
    
let len_comp_3 (xs:'a list) : int =
  let a = (len_ge_3 xs) in
  match a with
    false-> -1
  |true->let b = (len_eq_3 xs) in
      match b with
        true->0
      |false -> 1
    

  

