#include <iostream>
#include <vector>
#include <map>
#include <fstream>
using namespace std;

int get(int level, int elem, vector<int> & v){
	//for debug
	if(level >= v.size())
		return -1;
	return v[level] + elem + 1;
}

int main(){
	vector<string> vs;
	vector<int> vi;
	string readin = "";

	vi.push_back(0);

	ifstream wordsFile("triangle.txt");
	string words;
	if (wordsFile.is_open()){
    	while (getline(wordsFile, words, '\n')){
			readin += words + " ";
		}
	}

string delimiter = " ";
size_t pos = 0;
string token;
while ((pos = readin.find(delimiter)) != string::npos) {
    token = readin.substr(0, pos);
	vs.push_back(token);
    readin.erase(0, pos + delimiter.length());
}

for(int i = 0; i < 15; i++)
	vi.push_back(i);

cout << "(0, 0) " << vs[get(0,0, vi)] << endl;
cout << "(1, 1) " << vs[get(1,1, vi)] << endl;
cout << "(2, 3) " << vs[get(2,3, vi)] << endl;
cout << "(3, 5) " << vs[get(3,5, vi)] << endl;
cout << "(4, 4) " << vs[get(4,4, vi)] << endl;

return 0;}
