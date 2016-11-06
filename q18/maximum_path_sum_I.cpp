#include <iostream>
#include <vector>
#include <map>
#include <fstream>
using namespace std;

int get(int level, int elem, vector<int> & v){
	if(level >= v.size())
		return -1;
	return v[level] + elem;
}

int main(){

	vector<string> vs;
	vector<int> vi;
	string readin = "";

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


	vi.push_back(0);
	for(int i = 1; i < 15; i++)
		vi.push_back(i + vi[i-1]);

	

return 0;}
