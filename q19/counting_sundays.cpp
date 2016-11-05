/*
1 Jan 1900 was a Monday.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
*/
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
	int day = 0; //monday	
	date = 1;
	month = 1;
	year = 1901;

	while(!(date == 1 && month == 1 && year == 2001)){
		if(date == 1 && day == 6) ++sundays;
		leap = (month == 2 && (year % 100 != 0 || year % 400 == 0) && year % 4 == 0);
		++date;
		day = (day + 1) % 7;
		if(date > m[month] + leap){
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
