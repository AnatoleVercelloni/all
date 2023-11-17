#ifndef LU_SOLVER_HPP
#define LU_SOLVER_HPP

#include <utility>
#include <tuple>
#include <iostream>
#include <vector>
#include <cassert>
#include "map_matrix.hpp"
#include "vector.hpp"


using namespace std;

template <typename T>
class LUSolver{
  int nr;
  int nc;
  MapMatrix<T> LU;
  
  public:
	LUSolver(DenseMatrix<T> &M){
		nr = NbRow(M);
		nc = NbCol(M);
		LUFactorize(M);
		LU = M;
	}
	
	LUSolver(const LUSolver<T>& S):
	nc(S.nc), nr(S.nr), LU(S.LU){}
	
	LUSolver operator=(const LUSolver<T>& S){
	  nr = S.nr;
	  nc = S.nc;
	  LU = S.LU;
	  return *this;
	}
	
	T& operator()(const int j ,const int k){
		assert(j<nr && k<nc);
		return Data(LU)[j*nc + k];
	}
	
	// friend T& DenseMatrix::operator()(int j ,int k){
		// assert(j<nr && k<nc);
		// return data[j*nc + k];
	// }
	
	friend ostream &operator<<(ostream &o, const LUSolver<T> &S){
		o << S.LU;
		return o;
	}

	vector<T> Solve(const vector<T>& b){
		assert(b.size() == nr);
		vector<T> y(nr);
		vector<T> x(nr);
		int i,j;
		cout << "b  = " << b << endl;
		for (i = 0; i < nr; i++){
			for (j = 0; j<i; j++){
				y[i] = y[i] - LU(i,j)*y[j];
			}
			y[i] = y[i] + b[i];
		}
		
		// cout << "yint = " << y << endl;
		for (i = nr-1; i >=0; i--){
			for (j = nr-1; j>i; j--){
				x[i] = x[i] - LU(i,j)*x[j];
			}
			// cout << "i = " << i << endl;
			x[i] = (x[i] + y[i])/LU(i,i);
			// cout << "x[i] = " << x[i] << endl;
		}
		// cout << "xint = " << x << endl;
		return x;
	}
	
  
};

void NormalSolve(DenseMatrix<Cplx>& A, vector<Cplx>& x, const vector<Cplx>& b){
	DenseMatrix<Cplx> _A = A.herm();
	// cout << "A* = " << _A << endl;
	vector<Cplx> _b = _A*b;
	cout << "b*= " << _b << endl;
	DenseMatrix<Cplx> M (NbRow(A), NbRow(A));
	M =  _A*A;
	cout << "_A*A = " << M << endl;
	LUSolver<Cplx> S(M);
	cout << "LU = " << M << endl;
	x = S.Solve(_b);
}


void NormalSolve(MapMatrix<Cplx>& A, vector<Cplx>& x, const vector<Cplx>& b){
	MapMatrix<Cplx> _A = A.herm();
	// cout << "A* = " << _A << endl;
	vector<Cplx> _b = _A*b;
	cout << "b*= " << _b << endl;
	MapMatrix<Cplx> M (NbRow(A), NbRow(A));
	M =  _A*A;
	cout << "_A*A = " << M << endl;
	LUSolver<Cplx> S(M);
	cout << "LU = " << M << endl;
	x = S.Solve(_b);
}

#endif