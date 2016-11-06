#include <iostream>
#include <vector>
#include <map>
using namespace std;

int main(){
	map<int, int> m;
	m[2] = 28;
	m[1] = m[3] = m[5] = m[7] = m[8] = m[10] = m[12] = 31;
	m[4] = m[6] = m[9] = m[11] = 30;

	int sundays = 0;
	int date, month, year;
	bool leap = false;
	int day = 1;
	date = 1;
	month = 1;
	year = 1901;

	while(!(date == 1 && month == 1 && year == 2001)){
		if(date == 1 && day == 6) ++sundays;
		leap = (month == 2 && (year % 100 != 0 || year % 400 == 0) && year % 4 == 0);
		day = (day + 1) % 7;
		if(++date > m[month] + leap){
			date = date % (m[month] + leap);
			if(month < 12)
				++month;
			else{
				month = 1;
				++year;}
		}
	}
	cout << sundays << endl;

return 0;}
