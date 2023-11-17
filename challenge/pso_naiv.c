#include<stdlib.h>
#include<stdio.h>
#include <time.h>

Omega = 1.;
c1 = 1.;
c2 = 1.;

double dot_product(int N, double *x, double *y){
	double *res = 0.;
	for (int i = 0; i<N; i++){
		res+= x[i]*y[i];
	}
	
	return res;
}

double diff(double *res, , int N, double *x, double *y){
	for (int i = 0; i<N; i++){
		res[i]= x[i]-y[i];
	}
}
	

double f(double *X, int D){
	double res = 0.;
	for (int i = 0; i<D; i++){
		res+=X[i]*X[i];
	}
	return res;
}

double rand_naiv(double *v_i, int D, int LB, int UB){
	for (int i=0; i<D; i++){
		v_i[i] =  LB + (rand()/(RAND_MAX/(UB-LB)));
}

double best_naiv(int D, int N, double *x){
	double gbest = f(x[0]);
	double gcur = 0;
	for (int i = 1; i<N; i++){
		gcur = f(x[i])
		if (gcur < gbest){
			gbest = gcur;
		}
	}
	
	return gbest;
}
	
	
	
void update_v_naiv(int N, int D, double *v, double *x, int i, double *r_1, double *r_2, double *p, double g){
	
	double s1 = 0.;
	double s2 = 0.;
	double s3 = 0.;
	s1+=Omega*v[i];
	
	for (int k=0; k<D; k++){	
		double *diff1 = malloc(D*sizeof(double)); 
		double *diff2 = malloc(D*sizeof(double)); 
		
		s2+=c1*dot_product(r1, diff(diff1, N, p[i], x[i]));
		s3+= c2*dot_product(r2, diff(diff2, N, g[i], x[i]);		
	}
	
	v[i] = s1 + s2 + s3;	
	return ;
}

void update_xi_naiv(double *x, double *v){
	
	x[i] = x[i] + v[i];
	return ;
}
	

double pso(int N, int D, int T, int LB, int UB){
	
	double *v = malloc(N*sizeof(double*));
	double *x = malloc(N*sizeof(double*));
	double *p = malloc(N*sizeof(double*));
	
	for (int i=0; i<N; i++){
		
		double *v_i = malloc(D*sizeof(double)); 
		double *x_i = malloc(D*sizeof(double)); 
		
		rand_naiv(v_i, D, LB, UB);
		rand_naiv(x_i, D, LB, UB);
		rand_naiv(p_i, D, LB, UB);
		
		v[i] = v_i;
		x[i] = x_i;
		p[i] = x_i;
	}
	
	double g = best_naiv(x) 
	int t = 1;
	
	while (t<=T){
		for (i=0; i<N; i++){
			double *r_1 = malloc(D*sizeof(double)); 
			double *r_2 = malloc(D*sizeof(double)); 
			
			rand_naiv(r_1, D, 0, 1);
			rand_naiv(r_2, D, 0, 1);
			
			update_vi_naiv(N, D, v, x, i, r_1, r_2, p, g);
			update_xi_naiv(x, v);
			
			if (f(x)<f(p){
				p = f(x);
			}
		}
		
		g = best_naiv(x);
		t = t + 1;
	}
	
	return g;
}
				
			
	
	
	
	
int main(){
	srand(time(NULL));
	return 0;
}
	