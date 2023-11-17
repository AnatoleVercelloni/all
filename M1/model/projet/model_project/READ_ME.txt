

2 .c file:
	- hess.c which contains 
				-the given algorithm, and the algorithm to compute eigenvalues based on given
				-thealgorithm to make a matrice upper hessenberg
	  -hess_mpfr.c which contatins
				-the given algorithm, and the algorithm to compute eigenvalues based on given with the mpfr library
				

to compile hess.c                gcc -Wall -o hess hess.c -lmpfr -lgmp -lm
to compile hess_mpfr.c       gcc -Wall -o hess_mpfr hess_mpfr.c -lmpfr -lgmp -lm


the execution of this code run in a little matrix A and displays the computed eigenvalues and the hessenberg matrix (for hess.c)

for hess_mpfr.c there is the test of time (we did it also in hess.c)
