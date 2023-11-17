#ifndef DENSEMATRIX_HPP
#define DENSEMATRIX_HPP
#include <fstream>
#include <iostream>
#include <vector>
#include <cassert>
#include <cmath>
#include "vector.hpp"


using namespace std;
typedef complex<double> Cplx;

template <typename T>
class DenseMatrix{
	int nr;
	int nc;
	vector<T> data;
	public:
	DenseMatrix<T>():nr(0), nc(0), data({}){}
	
	DenseMatrix<T> (const int& nr, const int &nc):
 nr(nr), nc(nc), data(vector<T>(nr*nc)) {}
 
	DenseMatrix<T>(const DenseMatrix<T> &M):
	nr(M.nr), nc(M.nc), data(M.data){}
	
	DenseMatrix<T>& operator=(const DenseMatrix<T> &M){
		nr = M.nr;
		nc = M.nc;
		data = M.data;
		return *this;
	}

	T& operator()(int j ,int k){
		// cout << j << k << endl;
		// cout << nr << nc << endl;
		assert(j<nr && k<nc);
		return data[j*nc + k];
	}
	
	T& operator()(int k){
		assert(k<(nc*nr));
		return data[k];
	}
		
	DenseMatrix<T> operator+(const DenseMatrix<T>& M){
		DenseMatrix<T> nM = M;
		vector<T> ndata = data + M.data;
		nM.data = ndata;
		nM.nc = nc;
		nM.nr = nr;
		return nM;
	}

	void operator+=(DenseMatrix<T> &M){
		data = data + M.data;
	}

	friend ostream &operator<<(ostream &o, const DenseMatrix<T> &M){
		for (int i =0; i<M.nr; i++){
			for (int j = 0; j< M.nc; j++){
				o << "\t" << M.data[i*M.nc + j];
			}
			o << "\n";
		}
		return o;
	}
	


	DenseMatrix<T> operator*(const DenseMatrix<T> &M){
		assert(M.nr == nc);
		// cout << "A*= " << (*this) << endl;
		// cout << "A= " <<  M << endl;
		DenseMatrix<T> nM (nr, M.nc);
		vector<T> ndata ;
		for (int i = 0; i<nr; i++){
			for (int j = 0; j<M.nc ;j++){
				T a{};
				
				for (int k = 0; k<M.nr; k++){
					a = a + data[i*nc+k] * M.data[k*M.nc+j];
					// cout << "(" << i << "," << k << ")*(" << k << "," << j << ")" << endl; 
					// cout << data[i*nc+k]  << "*" << M.data[k*M.nc+j]  << endl;
					// cout << "+= " <<  data[i*nc+k] * M.data[k*M.nc+j] << endl;
					// cout << a << endl;
				}
				// cout << "ducoup: " << a << endl;
				nM(i,j) = a;
			}
		}
		// nM.data = ndata;
		return nM;
	}


	DenseMatrix<T> operator*(const T a){
		DenseMatrix<T> nM(nr,nc);
		vector<T> ndata;
		for (int i = 0; i<nr*nc; i++){
			ndata.push_back(data[i]*a);
		}
		nM.data = ndata;
		return nM;
	}
	
	
	vector<T> operator*(const vector<T> v){
		assert(v.size() == nc);
		// cout << nr << endl;
		vector<T> nv (0);
		// cout << nv << endl;
		for (int k = 0; k<nr; k++){ 
			T x{};
			for (int i = 0; i<v.size(); i++){
				// cout << "v[" << i << "]*A[" << k << "," << i << "]" << endl;
				// cout << v[i] << "*" << data[k*nc+i] << endl;
				x = x+v[i]*data[k*nc+i];
			}
			nv.push_back(x);
		}
		// cout << nv.size() << endl;
		return nv;
	}


	void operator*=(DenseMatrix<T> &M){
		DenseMatrix<T> nM = *this;
		nM = nM * M;
		return ;
	}

	friend int NbRow(const DenseMatrix<T>& M){
		return M.nr;
	}
	friend int NbCol(const DenseMatrix<T>& M){
		return M.nc;
	}
	// friend const vector<T>& Data(const DenseMatrix<T>& M){
		// return M.data;
	// }
	
	DenseMatrix<Cplx> herm(){
		//nr>=nc
		Cplx tmp;
		DenseMatrix<Cplx> A(nc, nr);
		int i ,j;
		for (i = 0; i< nc; i++){
			for (j = 0; j<=i ; j++){
				tmp = conj((*this)(i,j));
				A(i,j) = conj((*this)(j,i));
				A(j,i) = tmp;
			}
		}
		for (int k = i; k< nr; k++){
			for (j = 0; j< nc; j++){
				tmp = conj((*this)(k,j));
				A(j,k) = tmp;
			}
		}
		return A;
	}
	
};

template <typename T>
void matrix_column_permut(DenseMatrix<T>& mat, const vector<int> p){
	int l;
	T v,w;
	for (int i = 0; i<p.size(); i++){
		if (i != p[i]){
			for (int k = 0; k<NbRow(mat); k++){
				v = mat(k,i);
				w = mat(k,p[i]);
				mat(k,i) = w;
				mat(k,p[i]) = v;
			}
			l = p[p[i]];
			p[p[i]] = p[i];
			p[i] = l;
		}
	}
	return ;
}

template <typename T>
void LUFactorize(DenseMatrix<T>& mat){
	cout  << "LUFactorize" << endl;
	int N = NbRow(mat);
	T zero {};
	for (int i = 0; i<N; i++){
			for (int j = i+1; j<N; j++){
				assert(mat(i,i)!= zero);
				mat(j,i) = mat(j,i)/mat(i,i);
				for (int k = i + 1; k<N; k++){
					mat(j,k) = mat(j,k) - mat(j,i)*mat(i,k);
				}
			}
	}
}

template <typename T>
void LUFactorize(DenseMatrix<T>& mat, const vector<int>& pivot){
	int N = NbRow(mat);
	assert(pivot.size() == N);
	matrix_column_permut(mat, pivot);
	for (int i = 0; i<N; i++){
		for (int j = i+1; j<N; j++){
			assert(mat(i,i)!=0);
			mat(j,i) = mat(j,i)/mat(i,i);
			for (int k = i + 1; k<N; k++){
				mat(j,k) = mat(j,k) - mat(j,i)*mat(i,k);
			}
		}
	}
}

template <typename T>
DenseMatrix<T> LoadDenseMatrix(const string& filename){
		ifstream file(filename);
		if (file){
			int nc, nr;
			file >> nc;
			file >> nr;
			T v;
			int i = 0;
			DenseMatrix<T> M(nc, nr);
			string line;
			while (file >> v) {
				M(i) = v;
				// cout << i << endl;
				i++;
			}
			return M;
				
		}else{
			cout << "file opening error\n";
			exit(1);
		}
	}
	

template <>
DenseMatrix<Cplx> LoadDenseMatrix<Cplx>(const string& filename){
		ifstream file(filename);
		if (file){
			int nc, nr;
			file >> nc;
			file >> nr;
			double real;
			double imag;
			int i = 0;
			DenseMatrix<Cplx> M(nc, nr);
			string line;
			while (file >> real) {
				file >> imag;
				Cplx v(real, imag);
				M(i) = v;
				// cout << i << endl;
				i++;
			}
			return M;
				
		}else{
			cout << "file opening error\n";
			exit(1);
		}
	}
	

			
	
	


#endif