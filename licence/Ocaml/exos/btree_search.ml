(* GRADE:  100% *)
(* Q1 *)
let rec lt_btree (bt:'a btree) (x:'a) : bool =
  match bt with
    Empty->true
  |Node(y,g,d)->if y<x then (lt_btree g x)&&(lt_btree d x)
      else false

(* Q2 *)
let rec ge_btree (bt:'a btree) (x:'a) : bool =
  match bt with
    Empty -> true
  |Node(y,g,d) -> if y>=x then (ge_btree g x)&&(ge_btree d x)
      else false

(* Q3 *)
let rec is_abr (bt:'a btree) : bool =
  match bt with
    Empty->true
  |Node(x,g,d)->if (lt_btree g x)&&(ge_btree d x) then (is_abr g)&&(is_abr d)
      else false

(* Q4 *)
let rec mem (bt:'a btree) (x:'a) : bool =
  match bt with
    Empty->false
  |Node(y,g,d)->if x=y then true 
      else if x<y then (mem g x)
      else (mem d x)
  

