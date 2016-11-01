/*
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
*/

#include <iostream>
#include <vector>
using namespace std;

class Number{
	public:
		Number(){
			num = size = 0;
			name = "";}

		Number(int num, string name){
			this -> num = num;
			this -> name = name;
			this -> size = name.length();
			//TODO: don't count spaces
		}
	
		int get_num(){
			return num;}
	
		int get_size(){
			return size;}

		string get_name(){
			return name;}
	
	private:
		int num, size;
		string name;
};

string mod_helper(int index, int order, vector<Number> & v){
	int new_index = (index / order) % 10 * order;
	if(v[index].get_size() > 0)
		return v[index].get_name();

	return mod_helper(index - new_index, order * 10, v) + v[new_index].get_name();
}

string mod(int index, vector<Number> & v){
	string res = mod_helper(index, 1, v);
	if(index > 100 && index < 1000 && res.find("and") == string::npos)
		res += "and";	//hacky; British compliance
	return res;
}


int main(){
	//init	
	vector<Number> v;
	for(int i = 0; i <= 1000; i++)
		v.push_back(Number());

	v[0] = Number();
	v[1] = Number(1, "one");
	v[2] = Number(2, "two"); 
	v[3] = Number(3, "three");
	v[4] = Number(4, "four");
	v[5] = Number(5, "five");
	v[6] = Number(6, "six");
	v[7] = Number(7, "seven");
	v[8] = Number(8, "eight");
	v[9] = Number(9, "nine");
	
	v[11] = Number(11, "eleven");
	v[12] = Number(12, "twelve");
	v[13] = Number(13, "thirteen");
	v[14] = Number(14, "fourteen");
	v[15] = Number(15, "fifteen");
	v[16] = Number(16, "sixteen");
	v[17] = Number(17, "seventeen");
	v[18] = Number(18, "eighteen");
	v[19] = Number(19, "nineteen");

	v[10] = Number(10, "ten");
	v[20] = Number(20, "twenty");
	v[30] = Number(30, "thirty");
	v[40] = Number(40, "forty");
	v[50] = Number(50, "fifty");
	v[60] = Number(60, "sixty");
	v[70] = Number(70, "seventy");
	v[80] = Number(80, "eighty");
	v[90] = Number(90, "ninety");
	v[100] = Number(100, "onehundred");

	v[200] = Number(200, "twohundred");
	v[300] = Number(300, "threehundred");
	v[400] = Number(400, "fourhundred");
	v[500] = Number(500, "fivehundred");
	v[600] = Number(600, "sixhundred");
	v[700] = Number(700, "sevenhundred");
	v[800] = Number(800, "eighthundred");
	v[900] = Number(900, "ninehundred");

	v[1000] = Number(1000, "onethousand");

	int res = 0;
	int upper = v.size();

	for(int i = 1; i < upper; i++){
		if(v[i].get_size() == 0)
			v[i] = Number(i, mod(i, v));
		res += v[i].get_size();
		cout << v[i].get_name() << endl;
	}
	cout << "res: " << res << endl;
	return 0;
};
