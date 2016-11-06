#include <iostream>
#include <vector>
#include <map>
#include <fstream>
#include <string>
using namespace std;

int get(int level, int elem, vector<int> & v){
	if(level >= v.size())
		return -1;
	return v[level] + elem;
}

int main(){
//init
	vector<int> triangle;	//triangle
	vector<int> vi;	//elem at each level
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
		int val = std::stoi(token);
		triangle.push_back(val);
   		readin.erase(0, pos + delimiter.length());
	}


	vi.push_back(0);
	int i;
	for(i = 1; i < 100; i++)
		vi.push_back(i + vi[i-1]);

//solve
	int level = i - 2;
	int num_elems = level + 1;
	int elem;
	int curr_index, first_index, second_index;
	while(level >= 0){
		for(elem = 0; elem < num_elems; elem++){
			curr_index = get(level, elem, vi);
			first_index = get(level + 1, elem, vi);
			second_index = get(level + 1, elem + 1, vi);

			if(triangle[first_index] > triangle[second_index])
				triangle[curr_index] += triangle[first_index];
			else
				triangle[curr_index] += triangle[second_index];
			cout << triangle[first_index] << "\t";	
		}
		cout << triangle[second_index] << endl;

		--level;
		--num_elems;
	}
	cout << triangle[get(0,0,vi)] << endl;
	

return 0;}
