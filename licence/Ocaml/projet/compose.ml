(*Je met ici seulement la fonction compose que vous m'avez demandé d'ajouter
sinon, tout est sur learnOcaml*) 





let f  : sexpr =
  Call[Special Lambda; Call [Symbol "+"];
       Call [Atom (Primitive Add); Symbol "+"; Symbol "a"]];;


let g : sexpr =
  Call[Special Lambda; Call [Symbol "x"];
       Call [Atom (Primitive Mul); Symbol "x"; Symbol "a"]];;

let compose (f:sexpr) (g:sexpr) (env:env) (x:sexpr): sexpr= 
  eval env (Call [f; eval env (Call [g;x])]);;
  