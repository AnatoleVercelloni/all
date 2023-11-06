(* GRADE:  100% *)
(* Q.2 *)

let xor (a : bit) (b : bit) : bit =
  if a = b then false 
  else true

(* Q.3 *)

let half_adder (a : bit) (b : bit) : (bit * bit) =
  ((xor a b), a && b)

(* Q.4 *)

let adder (a : bit) (b : bit) (c : bit) : (bit * bit) =
  let (s1, r1) = (half_adder a b ) in 
  let (s2, r2) = (half_adder c s1) in 
  (s2, r1||r2) 
  
  
(* Q.5 *)
let _ = assert ((adder false false false) = (false, false)) 
let _ = assert ((adder false false true) = (true, false)) 
let _ = assert ((adder false true false) = (true, false)) 
let _ = assert ((adder false true true) = (false, true)) 
let _ = assert ((adder true false false) = (true, false)) 
let _ = assert ((adder true false true) = (false, true)) 
let _ = assert ((adder true true false) = (false, true)) 
let _ = assert ((adder true true true) = (true, true)) 
  
(* Q.6 *)

let duet_adder (a : duet) (b : duet) (c : bit) : (duet * bit) =
  let (e, f) = a in
  let (g, h) = b in
  let (s1, r2) = (adder f h c) in
  let (s2, r3) = (adder e g r2) in
  ((s2, s1) , r3)

(* Q.7 *)

let quartet_adder (a : quartet) (b : quartet) (c : bit) : (quartet * bit) =
  let (a1, a2, a3, a4) = a in
  let (b1, b2, b3, b4) = b in
  let ((s2, s1), c2) = duet_adder (a3, a4) (b3, b4) c in
  let ((s4, s3), c3) = duet_adder (a1, a2) (b1, b2) c2 in
  ((s4, s3, s2, s1), c3)

(* Q.8 *)

let to_quartet (i : int) : quartet =
  let (i2, r1) = (i/2, (i mod 2) = 1) in
  let (i3, r2) = (i2/2, (i2 mod 2) = 1) in
  let (i4, r3) = (i3/2, (i3 mod 2) = 1) in
  let r4 = ( (i4 mod 2) = 1) in
  (r4, r3, r2, r1) 
  
let _ = 
  let (a, r)= quartet_adder (to_quartet 4) (to_quartet 5) false in
  assert (a= (to_quartet 9))
  

