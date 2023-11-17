#include "triangular_matrix.hpp"

using namespace std;

UpperTriangularMatrix::UpperTriangularMatrix(const int& nr,const int& nc):
  nr(nr), nc(nc), data((nc+1)*nc/2,0.){};

UpperTriangularMatrix::UpperTriangularMatrix(UpperTriangularMatrix &M):
  nr(M.nr), nc(M.nc), data(M.data){};

UpperTriangularMatrix UpperTriangularMatrix::operator=(const UpperTriangularMatrix& M){
  nc = M.nc;
  nr = M.nr;
  data = M.data;
  return *this;
}

double& UpperTriangularMatrix::operator()(const int& j, const int& k){
  if (j<k || j>nc || k>nr){
    cout << "erroor" << endl;
    exit(1);
  }else{
    return data[(j*(j+1))/2+k];
  }
}

void push_back(const int& j, const int& k, const double &v);

ostream& operator<<(ostream &o, UpperTriangularMatrix& M){
  for (int i =0; i<M.nc; i++){
    for (int j= 0; j<M.nc; j++){
		if (i>=j){
      o << M(i,j) << "\t";
		}else{
			o << "\t";
		}
    }
    o << endl;
  }
  return o;
}


int NbRow(const UpperTriangularMatrix& M){
	return M.nr;
	
}

int NbCol(const UpperTriangularMatrix& M){
	return M.nc;
}

// vector<double> Solve(const vector<double>& b);