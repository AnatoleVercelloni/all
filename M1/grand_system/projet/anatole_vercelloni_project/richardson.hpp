#ifndef RICHARDSONSOLVER_HPP
#define RICHARDSONSOLVER_HPP

#include<map>
#include <iostream>
#include <vector>
#include <cassert>
#include <cmath>
#include <fstream>
#include "map_matrix.hpp"
#include "vector.hpp"


using namespace std;

class RichardsonSolver{
	double alpha;
	int maxit;
	double tol;
	vector<double> x0;
	
	public:
	RichardsonSolver (const double& alpha, const int& maxit, const double& tol, const vector<double>& x0);
	RichardsonSolver(RichardsonSolver& S);
	RichardsonSolver operator=(const RichardsonSolver& S);
	friend void CallBack(vector<double>& r, const vector<double>& b, int& n);
	void SetParam(const double& a, const int& m, const double& t);
	void SetInitialGuess(const vector<double>& x);
	vector<double> Solve( MapMatrix<double>& M, const vector<double>& b );
	vector<double> operator()(MapMatrix<double>& m, const vector<double>& b);
	
	
	
};
	
	


	
	
	
#endif