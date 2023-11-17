#include "richardson.hpp"

RichardsonSolver::RichardsonSolver(const double& alpha, const int& maxit, const double& tol, const vector<double>& x0):
alpha(alpha), maxit(maxit), tol(tol), x0(x0){}


RichardsonSolver::RichardsonSolver(RichardsonSolver& S):
alpha(S.alpha), maxit(S.maxit), tol(S.tol), x0(S.x0){}


RichardsonSolver RichardsonSolver::operator=(const RichardsonSolver& S){
  alpha = S.alpha;
  maxit = S.maxit;
  tol = S.tol;
  x0 = S.x0;
  return *this;
}

void CallBack(vector<double>& r, const vector<double>& b,int& n){
	cout << "number of iteration: "<< n 
	<< "  relativequadrative norm:" << Norm(r)/Norm(b) << endl;
}

void RichardsonSolver::SetParam(const double& a, const int& m, const double& t){
		alpha = a;
		maxit = m;
		tol = t;
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

	
void RichardsonSolver::SetInitialGuess(const std::vector<double>& x){
	x0 = x;
}


vector<double> RichardsonSolver::operator()(MapMatrix<double> & m, const vector<double>& b){
		int i = 0;
		vector<double> r = x0;
		vector<double> x = x0;
		cout << x << endl;
		while(i<maxit && Norm(r)>tol){
			r = b-m*x;
			x = x + r*alpha;
			CallBack(r, b, i);
			i++;
		}
		return x;
	}







		
	
	