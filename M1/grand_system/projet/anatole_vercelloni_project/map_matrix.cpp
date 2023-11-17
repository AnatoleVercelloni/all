#include<map>
#include <iostream>
#include <vector>
#include <cassert>
#include <cmath>
#include <fstream>
#include <vector>


using namespace std;

template <typename T>
class MapMatrix{	

	// using T = DataType;
	int nr;
	int nc;
	typedef tuple<int, int> NxN;
	map<NxN, T> data;
	
	public:
	
	MapMatrix<T> (const int& nr, const int& nc):nr(nr), nc(nc){}
	
	MapMatrix<T> (const MapMatrix<T> &M):nr(M.nr), nc(M.nc), data(M.data){}
	
	MapMatrix<T> &operator=(const MapMatrix<T> &M){
		nr = M.nr;
		nc = M.nc;
		data = M.data;
		return *this;
	}
	
	void insert(const int& i, const int& j, const T& v){
		tuple<int, int> t = {i,j};
		auto elt = data.find(t);
		auto it = data.begin();
		if (elt==data.end()){
			data.insert(it,{t,v});
		}
		else{
			 T w = data[t]+v;
			 data.erase(t);
			 data.emplace(t,w);
		}
	}
	
	friend ostream &operator<<(ostream &o, MapMatrix<T> &M){
		for (int i =0; i<M.nr; i++){
			for (int j = 0; j< M.nc; j++){
				map<NxN, T> data = M.data;
				auto elt = data.find({i,j});
				if (elt == data.end()){
					o << "\t" << "0";
				}else{
					o << "\t" << elt->second;		
				}
			}
			o << "\n";
		}
		return o;
	}
	
	MapMatrix<T> operator+(const MapMatrix<T> &M){
		MapMatrix<T> nM = M;
		nM.nc = nc;
		nM.nr = nr;
		map<NxN, T> ndata = M.data;
		for (auto it = data.begin(); it!=data.end(); ++it){
			tuple<int, int> t = it->first;
			nM.insert(get<0>(t), get<1>(t), it->second);
		}
		return nM;
	}
	
	MapMatrix<T> operator-(const MapMatrix<T> &M){
		MapMatrix<T> nM = M;
		nM.nc = nc;
		nM.nr = nr;
		map<NxN, T> ndata = M.data;
		for (auto it = data.begin(); it!=data.end(); ++it){
			tuple<int, int> t = it->first;
			nM.insert(get<0>(t), get<1>(t), (-1)*it->second);
		}
		return nM;
	}

	MapMatrix<T> operator*(MapMatrix<T> &M){
		assert(M.nr == nc);
		MapMatrix<T> nM(nc,nr);

		for (auto it = data.begin(); it!=data.end(); it++){
			tuple<int, int> t1 = it->first;
			int i1 = get<0>(t1);
			int j1 = get<1>(t1);
			
			for (auto jt = M.data.begin(); jt!=M.data.end(); jt++){
				tuple<int, int> t2 = jt->first;
				int i2 = get<0>(t2);
				int j2 = get<1>(t2);
				
				if (i1==j2){
					cout << i1 << j1 << i2 << j2 << endl;
					nM.insert(i2,j1, it->second*jt->second);
					cout << "A["<<i1<<","<<j2<<"] += "<< it->second <<"*" <<jt->second << endl;
				}
			}
		}
		return nM;
	}
	
	vector<T> operator*(const vector<T> &v){
		assert(v.size() == nc);
		vector<T> nv(nc);
		for (auto it = data.begin(); it!=data.end(); it++){
			tuple<int, int> t = it->first;
			int i = get<0>(t);
			int j = get<1>(t);
			for (int k = 0; k<nc; k++){
				if (j==k){
					nv[i]+=it->second*v[k];
					
				}
			}
		}
		return nv;
	}
	
	void operator+=(MapMatrix<T> &M){
		for (auto it = M.data.begin(); it!=M.data.end(); ++it){
			tuple<int, int> t = it->first;
			(*this).insert(get<0>(t), get<1>(t), it->second);
		}
	}
	// MapMatrix<T> LoadMapMatrix(const string& filename);
	
	
	
};

template <typename T>
MapMatrix<T> LoadMapMatrix(const string& filename){
		ifstream file(filename);
		if (file){
			int nc, nr;
			file >> nc;
			file >> nr;
			T v;
			int i,j;
			MapMatrix<T> M(nc, nr);
			string line;
			while (file >> i) {
				file >> j;
				file >> v;
				M.insert(i,j,v);
			}
			return M;
				
		}else{
			cout << "file opening error\n";
			exit(1);
		}
	}