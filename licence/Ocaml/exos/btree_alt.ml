(* GRADE:  100% *)

(* Q1 *)
let rec taille (ubt:'a ubtree) : int =
  match ubt with
    Empty2->0 
  |Leaf x->1 
  |Node2(g,x,d)-> 1+(taille g)+(taille d)
  
(* Q2 *)
let rec hauteur (ubt:'a ubtree) : int =
  match ubt with
    Empty2->0 
  |Leaf x->1
  |Node2(g,x,d)-> 1+(max (hauteur g)(hauteur d))

(* Q3 *)
let rec leaves (ubt:'a ubtree) : 'a list =
  match ubt with
    Empty2->[]
  |Leaf x->[x] 
  |Node2 (g,x,d) -> (leaves g)@(leaves d)
  
(* Q4 *)
let rec bt_to_ubt (bt:'a btree) : 'a ubtree =
  match bt with
    Empty->Empty2
  |Node(x,Empty,Empty)->Leaf x
  |Node(x,g,d)->Node2((bt_to_ubt g),x,(bt_to_ubt d))


  



  

