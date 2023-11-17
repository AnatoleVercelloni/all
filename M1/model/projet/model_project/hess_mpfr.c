#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <gmp.h>
#include <mpfr.h>
#include<time.h>

// We assume that matrices are vector row wise

void init_matrix(mpfr_ptr A,int m, int n, int t, int prec){
	// t = 1 : Id	t = 0: random   t = 2 : specific matrix
	if (t==1){
		for (int i =0; i<m; i++){
			for (int j =0; j<i; j++){
			mpfr_init_set_d((A+i + j*m), 0., MPFR_RNDN);
			mpfr_init_set_d((A + (j + i*m)), 0., MPFR_RNDN);
			}
		mpfr_init_set_d((A + (i + i*m)), 1., MPFR_RNDN);
		}
	}
	if (t == 0){
		double min = -100.0;
		double  max = 100.0;
		for (int i =0; i<m; i++){
			for (int j =0; j<n; j++){
			float x = min + (double)rand() / ((double)RAND_MAX/(max-min));
			mpfr_init_set_d((A+(i + j*m)), x, MPFR_RNDN);
			}
		}
	}
	if (t ==2 && n == 2 && m == 2){
		mpfr_init_set_d((A), -5., MPFR_RNDN);
		mpfr_init_set_d((A+1), 0., MPFR_RNDN);
		mpfr_init_set_d((A+2), 4., MPFR_RNDN);
		mpfr_init_set_d((A+3), 2., MPFR_RNDN);
	}
}


void copy_matrix(mpfr_ptr R, mpfr_ptr A, int m, int n){
		for (int i =0; i<m; i++){
			for (int j =0; j<n; j++){
					mpfr_set(R+i*n+j, A+i*n+j, MPFR_RNDN);
			}
		}
}

void clear_matrix(mpfr_ptr A, int m, int n){
	for (int i =0; i<m; i++){
			for (int j =0; j<n; j++){
				mpfr_clear(A+j*m+i);
			}
	}
	free(A);
}
		


void show_matrix(mpfr_ptr A, int m, int n, int prec){
	for (int i = 0; i<m; i++){
		for (int j = 0; j<n; j++){
			// printf("%f\t", A[i*n + j]);
			mpfr_out_str (stdout, prec, 0, (A+ (i*n + j)), MPFR_RNDN);
			printf("\t");
			
		}
		printf("\n");
	}
	printf("\n");
}
void UpperHessenberg(double *A, int n){
	for (int i = 0; i<n; i++){
		printf("en cours\n");
	}
}



void givens_ij(mpfr_ptr R, mpfr_ptr Q, int i, int j, int m, int n){
	mpfr_t rjj ;
	mpfr_init_set(rjj, R + j*n+j, MPFR_RNDN);
	mpfr_t rij ;
	mpfr_init_set(rij, R + i*n+j, MPFR_RNDN);
	mpfr_t m1;
	mpfr_init(m1);
	mpfr_mul(m1, rjj, rjj, MPFR_RNDN);
	mpfr_t m2;
	mpfr_init(m2);
	mpfr_mul(m2, rij, rij, MPFR_RNDN);
	mpfr_t a;
	mpfr_init(a);
	mpfr_add(a, m1, m2, MPFR_RNDN);
	mpfr_t sq;
	mpfr_init(sq);
	mpfr_sqrt(sq, a, MPFR_RNDN);
	mpfr_t c;
	mpfr_init(c);
	mpfr_div(c, rjj, sq, MPFR_RNDN);
	mpfr_t s;
	mpfr_init(s);
	mpfr_div(s, rij, sq, MPFR_RNDN);
	mpfr_t neg;
	mpfr_init(neg);
	// mpfr_t tmp;
	// mpfr_init(tmp);


	for (int k = 0; k < m; k++) {
		// printf("iteration %d \n", k);
		// show_matrix(R, m , n);
		mpfr_neg(neg, s,  MPFR_RNDN);
		if (k < n) {
			mpfr_mul(m1, c, R+j*n+k , MPFR_RNDN);
			mpfr_mul(m2, s, R+i*n+k , MPFR_RNDN);
			mpfr_add(a, m1, m2 , MPFR_RNDN);
			
			mpfr_mul(m1, neg, R+j*n+k , MPFR_RNDN);
			mpfr_mul(m2, c, R+i*n+k , MPFR_RNDN);
			mpfr_add(R + i * n + k, m1, m2 , MPFR_RNDN);
			mpfr_set(R + j * n + k, a,  MPFR_RNDN);
			
		}
			mpfr_mul(m1, c, Q+k*m+j , MPFR_RNDN);
			mpfr_mul(m2, s, Q+k*m+i , MPFR_RNDN);
			mpfr_add(a, m1, m2 , MPFR_RNDN);
			
			mpfr_mul(m1, neg, Q+k*m+j , MPFR_RNDN);
			mpfr_mul(m2, c, Q+k*m+i , MPFR_RNDN);
			mpfr_add(Q + k * m + i, m1, m2 , MPFR_RNDN);
			mpfr_set(Q + k * m + j, a,  MPFR_RNDN);
	
	}
	mpfr_clear(a);
	mpfr_clear(m1);
	mpfr_clear(m2);
	mpfr_clear(rjj);
	mpfr_clear(rij);
	mpfr_clear(sq);
	mpfr_clear(neg);
	mpfr_clear(c);
	mpfr_clear(s);
	return ;
}


void givens(mpfr_ptr A, mpfr_ptr Q, mpfr_ptr R, int m, int n){

	// printf("Ab\n");
	// show_matrix(A, m, n, 10);
	// memcpy(R,A,m*n*sizeof(mpfr_t));
	copy_matrix(R, A, m, n);
	for (int j = 0; j<n; j++){
		for (int i = j+1; i<m; i++){
			// printf("tour %d\n", i);
			givens_ij(R, Q, i, j, m, n);
			// printf("Aa\n");
			// show_matrix(A, m, n, 10);
		}
	}
	return ;
}

double max_norm_sub_diag(mpfr_ptr A, int m, int n){
	double p = 0.;
	double a;
	for (int i = 0; i< n-1; i++){
		a = fabs(mpfr_get_d(A + (i+1) * n + i, MPFR_RNDN));
		if (a>p){
			p = a;
		}
	}
	// printf("max_norm = %f\n", p);
	return p;
}


void naiv_matrix_product(mpfr_ptr C, mpfr_ptr A, mpfr_ptr B, int m, int n, int l){
	
	mpfr_t a;
	mpfr_t m1;
	mpfr_t c;
	mpfr_init(a);
	mpfr_init(m1);
	mpfr_init(c);
	for (int i = 0; i<m; i++){
			for (int j = 0; j<l ;j++){
				mpfr_set_d(c, 0., MPFR_RNDN);
				mpfr_set_d(a, 0., MPFR_RNDN);
				for (int k = 0; k<n; k++){
					mpfr_mul(m1, A + i*n + k, B + k*l+j, MPFR_RNDN);
					mpfr_add(c, a, m1, MPFR_RNDN);
					mpfr_set(a,c,MPFR_RNDN);
					
					// a = a + A[i*n+k] * B[k*l+j];
				}
				mpfr_set(C + i*m+j, c, MPFR_RNDN);
				// C[i*m+j] = a;
			}
	}
	mpfr_clear(a);
	mpfr_clear(m1);
	mpfr_clear(c);
	return ;
}

void transpose_square (mpfr_ptr T, mpfr_ptr A, int n){
	// printf("debut transpose\n");
	mpfr_t tmp;
	mpfr_init(tmp);
	for (int i =0; i<n; i++){
		// mpfr_out_str (stdout, 2, 0, T, MPFR_RNDN);
		// mpfr_set(tmp, A + i*n+i, MPFR_RNDN);
		// printf("maiiiis\n");
		// mpfr_out_str (stdout, 2, 0, tmp, MPFR_RNDN);
		
		mpfr_set(T + i*n + i, A + i*n+i, MPFR_RNDN);
		// mpfr_set(T + i*n + i, A + i*n+i, MPFR_RNDN);
		for (int j = 0; j<i; j++){
			// printf("tour %d \n",j);
			mpfr_set(tmp, A + i*n+j, MPFR_RNDN);
			mpfr_set(T + i*n + j, A + j*n+i, MPFR_RNDN);
			mpfr_set(T + j*n + i, tmp, MPFR_RNDN);
		
		}
		// printf("tour %d \n",i);
	}
	mpfr_clear(tmp);
	return ;
}
	

void make_presque_triangular(mpfr_ptr A, mpfr_ptr Q, mpfr_ptr R, int m, int n, double tol, int maxit){
	int k =0;
	mpfr_ptr T = malloc(n*n*sizeof(mpfr_t));
	//printf("allocation T ok\n");
	init_matrix(T, n, n, 1, 5); 
	//printf("init T ok\n");
	mpfr_ptr nA = malloc(m*n*sizeof(mpfr_t));
	init_matrix(nA, m, n, 1, 5); 
	mpfr_ptr nnA = malloc(m*n*sizeof(mpfr_t));
	init_matrix(nnA, m, n, 1, 5); 
	//printf("all alloc and init ok\n");
	
	//show_matrix(A, m, n, 10);
	while (max_norm_sub_diag(A, m ,n)> tol && k<maxit){
		// show_matrix(A, m, n, 10);
		// printf("A\n");
		// show_matrix(A, m, n, 10);
		givens(A, Q, R, m, n);
		// printf("Q\n");
		// show_matrix(Q, m, n, 10);
		// printf("R\n");
		// show_matrix(R, m, n, 10);
		// printf("givens ok\n");
		transpose_square(T, Q, m);
		// show_matrix(T, m, n, 10);
		// printf("transpose ok\n");
		 // show_matrix(nA, m, n, 10);
		 // show_matrix(Q, m, n, 10);
		 // show_matrix(A, m, n, 10);
		naiv_matrix_product(nA, Q, A, m, m, n);
		// printf("na\n");
		 // show_matrix(nA, m, n, 10);
		// printf("matrix_product ok ok\n");
		naiv_matrix_product(nnA, nA, T, m, n, n);
		// printf("nna\n");
		 // show_matrix(nnA, m, n, 10);
		// printf("matrix_product2 ok ok\n");
		copy_matrix(A, nnA, m, n);
		k++;
		
	}
	clear_matrix(T, n, n);
	clear_matrix(nA, m, n);
	clear_matrix(nnA, m, n);
	//printf("nombre d'itération: %d\n", k);
	return ;
}


void eigenvalues(mpfr_ptr A, int n){
	printf("eigenvalues:     \n");
	for (int i = 0; i<n; i++){
		mpfr_out_str (stdout, 10, 0, A+ i*n+i,  MPFR_RNDN);
		printf("\n");
		// mpfr_set(ev + i, A+ i*n+i, MPFR_RNDN);
		// ev[i] = A[i * n + i];
	}
	printf("\n\n\n");
}
		
			
	int main(int argc, char ** argv) {
		srand(time(NULL));
		clock_t start,end;
		double time;
		int M = 100;
		int N = 100;
		int m = 2;
		int n = 2;
		mpfr_ptr A = malloc(m*n*sizeof(mpfr_t));
		init_matrix (A, m, n, 2, 5);
		//show_matrix(A, m, n, 10);
		mpfr_ptr Q = malloc(M*M*sizeof(mpfr_t));
		//init_matrix (Q, m, m, 1, 5);
		mpfr_ptr R = malloc(M*N*sizeof(mpfr_t));
		//init_matrix (R, m, n, 1, 5);
		// mpfr_ptr ev = malloc(n*sizeof(mpfr_t));
		// init_matrix (ev, 1, n, 1, 5);
		
		for (int i = 10; i<M; i=i+10){
			mpfr_ptr _A = malloc(i*i*sizeof(mpfr_t));
			init_matrix (_A, i, i, 0, 5);
			mpfr_ptr Q = malloc(i*i*sizeof(mpfr_t));
			init_matrix (Q, i, i, 0, 5);
			mpfr_ptr R = malloc(i*i*sizeof(mpfr_t));
			init_matrix (R, i, i, 0, 5);
			//printf("start\n");
			start = clock();
			make_presque_triangular(_A, Q, R, i, i, 0.002, 1000);
			end = clock();    
			printf("time for n = %d: %f\n", i, (double)(end - start)/ CLOCKS_PER_SEC);
			//printf("fin: \n");
		}
		
		//show_matrix(A, m, n, 10);
		//eigenvalues(A, n);
		//printf("eigenvalue ok\n");
		// show_matrix(ev, 1, n, 5);
		clear_matrix(A, m, n);
		clear_matrix(Q, m, m);
		clear_matrix(R, m, n);
		// clear_matrix(ev, m, n);
		
		mpfr_free_cache();
		return 0;
	}
