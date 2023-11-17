#include <iostream>
#include <vector>
#include <cassert>
#include <cmath>
#include <fstream>
#include <map>
#include "dense_matrix.hpp"
#include "map_matrix.hpp"
#include "vector.hpp"
#include "triangular_matrix.hpp"
#include "richardson.hpp"
#include "lu_solver.hpp"
#include"dense_matrix.hpp"
#include <complex>

using namespace std;
typedef complex<double> Cplx;
typedef Cplx T;


int main(){
	
	vector<T> b0 = {Cplx(3,0), Cplx(4,0), Cplx(2,0)};
	vector<T> v = {Cplx(3,0), Cplx(4,0), Cplx(4,0)};
	const vector<double> c = {2., 3.};
	const vector<double> d = {2., 3.};
	// cout << (b,v) << endl;
	// vector<int> p = {0,2,1};
	
	MapMatrix<T> A1 = LoadMapMatrix<T>("matrix_1.txt");
	cout << "load matrix done" << endl;
	vector<T> b1 = LoadVector("rhs_1.txt", NbRow(A1));
	cout << "load vector b done" << endl;
	vector<T> x1(b1.size());
	cout << "build vector x done" << endl;
	
	MapMatrix<T> A2 = LoadMapMatrix<T>("matrix_2.txt");
	cout << "load matrix done" << endl;
	vector<T> b2 = LoadVector("rhs_2.txt", NbRow(A2));
	cout << "load vector b done" << endl;
	vector<T> x2(b2.size());
	cout << "build vector x done" << endl;
	
	MapMatrix<T> A3 = LoadMapMatrix<T>("matrix_3.txt");
	cout << "load matrix done" << endl;
	vector<T> b3 = LoadVector("rhs_3.txt", NbRow(A3));
	cout << "load vector b done" << endl;
	vector<T> x3(b3.size());
	cout << "build vector x done" << endl;
	
	MapMatrix<T> A4 = LoadMapMatrix<T>("matrix_4.txt");
	cout << "load matrix done" << endl;
	vector<T> b4 = LoadVector("rhs_4.txt", NbRow(A4));
	cout << "load vector b done" << endl;
	vector<T> x4(b4.size());
	cout << "build vector x done" << endl;
	
	MapMatrix<T> A5 = LoadMapMatrix<T>("matrix_5.txt");
	cout << "load matrix done" << endl;
	vector<T> b5 = LoadVector("rhs_5.txt", NbRow(A5));
	cout << "load vector b done" << endl;
	vector<T> x5(b5.size());
	cout << "build vector x done" << endl;
	MapMatrix<T>  A0 = LoadMapMatrix<T>("map_matrix_cplx.txt");
	vector<T> x0(b0.size());
	// cout << A1*b1 << endl;
	// MapMatrix<T> R = LoadMapMatrix<T>("map_matrix_cplx.txt");
	// MapMatrix<Cplx> H(2 + 1,2);
	// cout << A << endl;
	// cout << Arnoldi(A,H,v,2) << endl;
	// cout << "hey" << endl;
	// cout << H << endl;
	// givens(A, Q, R);
	// cout << R << endl;
	// cout << "A = " << A << endl;
	// cout << "B = " << B << endl;
	// cout << b<< endl;
	// cout <<"C = " << C << endl;
	// cout << b*Cplx(3.,0.) << endl;
	// cout << B.Solve(b) <<  endl;
	int restart = 1;
	int maxit = 1e4;
	double tol  = 1e-6;
	vector<Cplx> y;
	
	/* GMRes marche avec resart = 1 et restart grand mais pas entre les deux, 
	je ne sais pas vraiment pourquoi
	je n'ai donc pas pu tracer de courbe en fonction de restart*/
	
	
	y = GMResSolve_restart(A1, x1, b1, restart, tol, maxit, "analysis.txt");
	// y = GMResSolve_restart(A1, x1, b1, restart, tol, maxit);
	cout << "big check " << Norm(b1- A1*y) << endl;
	// cout << "big check " << b1 - A1*y << ": " << Norm(b1 - A1*y) << endl;
	// cout << A << endl;

	
	
	return 0;
}
