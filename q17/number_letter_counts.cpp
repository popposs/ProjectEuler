#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

class Number{
	public:
		Number(){
			num = size = 0;
			name = "";}

		Number(int num, string name){
			this -> size = name.length();
			this -> has_and = false;
			this -> num = num;
			this -> name = name;}

		int get_num(){
			return num;}
	
		int get_size(){
			return size;}

		string get_name(){
			return name;}

		bool get_has_and(){
			return has_and;}

		void set_has_and(bool b){
			this -> has_and = b;}

		void set_size(int s){
			this -> size = s;}
	
	private:
		bool has_and;
		int num, size;
		string name;
};

int split_num(int num, int order){
	string ret = to_string(num);
	char c = ret[ret.length() - 1 - log10(order)];
	return (c - '0') * order;
}

string mod_helper(int index, int order, vector<Number> & v){
	if(order == 0)
		return "";
	int split = split_num(index, order);
	string ret = "";
	if(v[split].get_size() > 0)
		ret += v[split].get_name();
	return ret + mod_helper(index, order / 10, v);
	
}

string mod(int index, vector<Number> & v){
	int order = 0;
	if(index >= 100)
		order = 100;
	else
		order = 10;

	string res = mod_helper(index, order, v);
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

		if(v[i].get_has_and() == false && i % 100 != 0 && i > 100 && i < 1000){
			v[i].set_size(v[i].get_size() + 3);
			v[i].set_has_and(true);}

		res += v[i].get_size();}

	cout << "res: " << res + 36 << endl;

	return 0;
};
