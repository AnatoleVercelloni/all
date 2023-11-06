let initial_env : env = []

let rec eval (env : env) (e : sexpr) : sexpr = match e with
  |Atom a -> e
  |Symbol x -> List.assoc x env
  |Call c -> eval_call env c
  |Special s -> failwith"special" 
  (* si e est un atome, alors retourner simplement e *)
  (* sinon, si e est un symbole x, chercher le couple (x,v) dans l'environnement, 
   *                        et retourner simplement la valeur v. 
   *                        PS: on pourra utiliser la fonction List.assoc *)
  (* sinon, si e est une application (Call), alors évaluer l'application (cf. eval_call) *)
and is_special (e : sexpr) : bool = match e with
  |Special e -> true
  |_ -> false
    
and fonction (env : env) (es : sexpr list) : (env*sexpr) list = 
  let rec aux env es l =
    match es with
    |[] -> l
    |hd::tl -> aux env tl ((env,hd)::l)
  in aux env es []
  
  
and eval_call (env : env) (es : sexpr list) : sexpr = match es with
  |f::tl-> if is_special f then eval_special env (f::tl)
      else apply (List.map (function (e,se) -> eval e se) (List.rev (fonction env es)))
  |[]-> failwith"evalcall"
  
  (* `(f a1 a2 ... an)` *)
  (* si l'expression f à appliquer est une forme spéciale (cf. is_special), évaluer la forme speciale (cf. eval_special). *)
  (* sinon, évaluer tout les éléments f, a1, a2, a3 ... de l'application ; on obtient les valeurs vf, va1, va2, ... vn ; 
   * puis appeler la fonction apply. *)

and eval_special (env : env) (es : sexpr list) : sexpr = match es with
  | [Special If;e1;e2;e3] -> (match eval env e1 with
      |Atom(Bool true) ->eval env e2
      |Atom(Bool false)-> eval env e3
      |_ -> failwith"evalspecial")
      
  (* 1) si c'est une alternative (If), évaluer la condition.
   *     - si la condition est (Atom(Bool true)), alors, évaluer la conséquence (l'expression <then>).
   *     - sinon, évaluer l'alternant (l'expression <else>).
   * si c'est une fonction anomyme (lambda),
*)
  | [Special Lambda;Call args;body] ->Atom (Fun (env,(List.map (function Symbol name -> name | _ -> assert false) args,body)))
  | [Special Let;Call[name;e1];e2] -> 
      let es' = Call [Call [Special Lambda;Call [name];e2];e1] in 
      eval env es'
  (* Remarquez que l'expression   (let (x e1) e2)    est réécrit en   ((lambda (x) e2) e1)   *)
  | _ -> failwith "eval_special"
  
and apply (es : sexpr list) : sexpr = match es with
  |Atom(Primitive p)::tl -> apply_primitive p tl 
  |Atom(Fun (e,c))::tl -> apply_function (e,c) tl
  |_ -> failwith"apppply" 
   (* `(vf va1 va2 ... vn)`
    * --> si vf est une primitive, appliquer la primitive vf à la liste d'arguments va1, va2, ... vn (cf. apply_primitive)
    * --> si vf est une fonction (Fun), appliquer la fonction vf à la liste d'arguments va1, va2, ... vn (cf. apply_function)
*)

and apply_primitive (p : primitive) (args : sexpr list) : sexpr = 
  match p,args with
  |Add,[Atom (Int n);Atom (Int m)] -> Atom (Int (n+m)) (* PS: on pourrait aussi faire un (+) n-aire, avec fold_left *)
  |Sub,[Atom (Int n);Atom (Int m)] -> Atom (Int (n-m))
  |Mul,[Atom (Int n);Atom (Int m)] -> Atom (Int (n*m))
  |Div,[Atom (Int n);Atom (Int m)] -> Atom (Int (n/m))
  |Eq,[Atom (Int n);Atom (Int m)] -> if m==n then Atom (Bool true) else Atom (Bool false)
  |Eq,[Atom (Bool n);Atom (Bool m)] -> if m==n then Atom (Bool true) else Atom (Bool false)
  |Lt,[Atom (Int n);Atom (Int m)] -> if n<m then Atom (Bool true) else Atom (Bool false)
          (*|Lt,[Atom(Int n);Atom (Int m)] -> if (n/m*m)==n then Atom (Bool true) else Atom (Bool false)*)
  |Cons,[x; Atom (List y)] -> Atom (List (x::y))
  |Car,[Atom (List (x::y))] -> x
  |Cdr,[Atom (List (x::y))] -> Atom (List y)
  | _ -> failwith "applyprimitive"

and apply_function (vf : env * code) (args : sexpr list) : sexpr =
  match vf with
  |(env, (xs,e)) ->(*if (List.length env+List.length args)!= (List.length xs) then failwith "apply_function m!=n"
                   else *)eval (extend_env env xs args) e

  (* `(vf va1 va2 ... vn)`
   * Décomposer la valeur fonctionnelle vf : c'est un couple (env',code) où :
   * - env' est l'environnement de la fermeture,
   * - code est le code de la fonction : c'est un couple (xs,e) ou 
   *                                      - xs = x1,x2,...,xm est la liste des arguments formels de vf  
   *                                      - l'expression e est le corps de la fonction
   * 
   * Lancer une exception si m est différent de n (il n'y a pas d'application partielle en Scheme).
   *
   * Enrichir l'environnement env' en liant les argument formels xk aux arguments effectifs vak (cf. extend_env), 
   * appelons `lenv` ce nouvel environnement.
   *
   * Enfin, évaluer le corps `e` de la fonction dans l'environnement `lenv` (cf. eval).
*)


and extend_env (env : env) (xs : string list) (vs : sexpr list)  : env = 
  match xs, vs with
  |xs,vs -> ((List.combine xs vs)@env) ;;
  (* Posons xs = x1,x2, ...,xn et vs = v1, v2, ..., vn.
   * 
   * Enrichir l'environnement local env, en liant chaque variable xi à la valeur vi : 
   * 1) construire la liste de couple [(x1,v1);(x2,v2); ...;(xn,vn)] 
   *    (PS: on pourra utiliser la fonction List.combine) 
   *    On obtient une liste l.
   * 2) concaténer l à la tête de env. On obtient l'environnement souha*)

let consintlist (l: int list) : sexpr =
  let rec aux (l: int list) (res: sexpr) : sexpr =
    match l with 
    |[] -> res
    |(x::xs) -> aux xs (eval [("cons",Atom(Primitive Cons))] (Call [Symbol "cons";Atom(Int x);res])) 
  in aux (List.rev l) (Atom(List[]));;

let multete (m:int) (l: int list): sexpr = 
  eval [("tete",Atom(Primitive Car));"mult",Atom(Primitive Mul)]
    (Call [Symbol "mult";Atom(Int m);
           (Call [Symbol "tete";(consintlist l)])]) ;;

let divise (x: int)  (m: int): sexpr =
  eval [("d",Atom(Primitive Lt))] ( Call [Symbol "d"; Atom (Int x);Atom (Int m)]);;

let testpremier (x: int): sexpr = 
  let rec aux x i=
    match x,i with 
    |(0,i)|(1,i) -> Atom(Bool false)
    |x,0 -> Atom(Bool false)
    |(x,(-1)) -> eval [] 
                   (Call[Special If;
                         (divise x 2);
                         Atom(Bool false);(*Atom(Bool true)])*)
                         (aux x (x/2))])
    |(x,1) -> Atom(Bool true)
                
    |_,_-> eval [] 
             (Call[Special If;
                   (divise x i);
                   Atom(Bool false);
                   (aux x (i-1))]) 
  in aux x (-1);;
  
let lambda (a: int) : sexpr= 
  eval [("a", Atom (Int a))] (Call
                                [Call
                                   [Special Lambda; Call [Symbol "x"];
                                    Call [Atom (Primitive Mul); Symbol "x"; Symbol "a"]];
                                 Atom (Int 7)]);;