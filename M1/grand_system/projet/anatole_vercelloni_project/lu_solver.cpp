#include "lu_solver.hpp"
#include "dense_matrix.hpp"

using namespace std;


LUSolver::LUSolver(DenseMatrix &M){
	nr = NbRow(M);
	nc = NbCol(M);
	LUFactorize(M);
	LU = M;
}

LUSolver::LUSolver(LUSolver& S):
nc(S.nc), nr(S.nr), LU(S.LU){}


LUSolver LUSolver::operator=(const LUSolver& S){
  nr = S.nr;
  nc = S.nc;
  LU = S.LU;
  return *this;
}


double& LUSolver::operator()(int j ,int k){
	assert(j<nr && k<nc);
	return Data(LU)[j*nc + k];
}

ostream &operator<<(ostream &o, LUSolver &S){
	o << S.LU;
	return o;
}

vector<double> LUSolver::Solve(vector<double>& b){
	vector<double> y(nr);
	vector<double> x(nr);
	
	for (int i = 0; i < nr; i++){
		for (int j = 0; j<i; j++){
			y[i] -= Data(LU)[i*nc + j];
		y[i] += b;
		}
	}
	
	for (int i = nr; i >0; i--){
		for (int j = i; j>0; j--){
			y[i] -= Data(LU)[i*nc + j];
		y[i] += b/Data(LU)[i*nc + i];
		}
	}
	return x;
}
	
	
			
			
		
}
	
	