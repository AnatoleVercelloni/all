
#include "dense_matrix.hpp"
#include "vector.hpp"

using namespace std;

DenseMatrix::DenseMatrix():nr(0), nc(0), data({}){}

DenseMatrix::DenseMatrix
(const int& nr, const int &nc):
 nr(nr), nc(nc), data(vector<double>(nr*nc)) {}


DenseMatrix::DenseMatrix
(const DenseMatrix &M):nr(M.nr), nc(M.nc), data(M.data){}

// DenseMatrix::DenseMatrix(MapMatrix &M):nr(M.nr), nc(M.nc){}



DenseMatrix& DenseMatrix::operator=(const DenseMatrix &M){
	nr = M.nr;
	nc = M.nc;
	data = M.data;
	return *this;
}

double& DenseMatrix::operator()(int j ,int k){
	assert(j<nr && k<nc);
	return data[j*nc + k];
}

double& DenseMatrix::operator()(int k){
	assert(k<(nc*nr));
	return data[k];
}

	
	
DenseMatrix DenseMatrix::operator+(DenseMatrix& M){
	DenseMatrix nM = M;
	vector<double> ndata = data + M.data;
	nM.data = ndata;
	nM.nc = nc;
	nM.nr = nr;
	return nM;
}
	
void DenseMatrix::operator+=(DenseMatrix &M){
	data = data + M.data;
}
		
ostream &operator<<(ostream &o, DenseMatrix &M){
	for (int i =0; i<M.nr; i++){
		for (int j = 0; j< M.nc; j++){
			o << "\t" << M.data[i*M.nc + j];
		}
		o << "\n";
	}
	return o;
}

DenseMatrix DenseMatrix::operator*(DenseMatrix &M){
	assert(M.nr == nc);
	DenseMatrix nM = M;
	vector<double> ndata ;
	for (int i = 0; i<nr; i++){
		for (int j = 0; j<M.nc ;j++){
			double a = 0.0;
			for (int k = 0; k<nc; k++){
				a = a + data[i*nc+k] * M.data[k*nc+j];
			}
			ndata.push_back(a);
		}
	}
	nM.data = ndata;
	return nM;
}

DenseMatrix DenseMatrix::operator*(double a){
	DenseMatrix nM(nr,nc);
	vector<double> ndata;
	for (int i = 0; i<nr*nc; i++){
		ndata.push_back(data[i]*a);
	}
	nM.data = ndata;
	return nM;
}


vector<double> DenseMatrix::operator*(vector<double> v){
	assert(v.size() == nc);
	vector<double> nv;
	for (int k = 0; k<nc; k++){ 
		double x = 0.0;
		for (int i = 0; i<nr; i++){
			x = x+v[i]*data[i*nc+k];
		}
		nv.push_back(x);
	}
	return nv;
}

int NbRow(const DenseMatrix& M){
	return M.nr;
	
}

int NbCol(const DenseMatrix& M){
	return M.nc;
}

vector<double> Data(const DenseMatrix& M){
	return M.data;
}

void DenseMatrix::operator*=(DenseMatrix &M){
	DenseMatrix nM = *this;
	nM = nM * M;
	return ;
}


void LUFactorize(DenseMatrix& mat){
	int N = NbRow(mat);
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


void matrix_column_permut(DenseMatrix& mat, vector<int> p){
	int l;
	double v,w;
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
	
				

void LUFactorize(DenseMatrix& mat, vector<int>& pivot){
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


DenseMatrix LoadDenseMatrix(const string& filename){
		ifstream file(filename);
		if (file){
			int nc, nr;
			file >> nc;
			file >> nr;
			double v;
			int i = 0;
			DenseMatrix M(nc, nr);
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