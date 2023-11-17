#ifndef UPPER_TRIANGULAR_HPP
#define UPPER_TRIANGULAR_HPP

#include <utility>
#include <tuple>
#include <iostream>
#include <vector>
#include <cassert>


using namespace std;

class UpperTriangularMatrix{
  int nr;
  int nc;
  vector<double> data;

  public:
  UpperTriangularMatrix(const int& nr, const int& nc);
  UpperTriangularMatrix(UpperTriangularMatrix& M);
  UpperTriangularMatrix operator=(const UpperTriangularMatrix &M);
  void push_back(const int& j, const int& k, const double &v){
    if (j>k || j>nc || k>nr){
      cout << "erroor push back" << endl;
      exit(1);
    }else{
      data[(j*(j+1))/2+k]+= v;
    }
  }
  double& operator()(const int& j, const int& k);
  friend ostream& operator<<(ostream &o, UpperTriangularMatrix& M);
  
  vector<double> Solve(const vector<double>& b){
	  assert(b.size() == nc);
	  vector<double> x(nc);
	  int j = 0;
	  for (int i=nc; i>0; i--){
		double s = .0;
		for (j = nc; j>i-1; j--){
		  s += (*this)(j,i)*x[j];
		}
		x[i]= b[i]/(*this)(i,i);
	  }
	  return x;
	}
	
	friend int NbRow(const UpperTriangularMatrix& M);
	friend int NbCol(const UpperTriangularMatrix& M);
  
};

#endif