#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <fstream>
#include <utility> 
#include <sstream>


using namespace std;

typedef string S;
typedef map<S,map<S,int> > Map2;
typedef map<S,Map2> Map1;
typedef vector<S> VS;
typedef stringstream SS;
typedef vector<int> VI;


void rewrite_data()
{

S file="car.csv";
ifstream iff(file);
ofstream off("car_replaced.csv");
	
while(!iff.eof())
{	
	S buying, maint,doors, persons, lug_bot, safety, class_v;	
		
	getline(iff,buying,',');						
	getline(iff,maint,',');
	getline(iff,doors,',');
	getline(iff,persons,',');
	getline(iff,lug_bot,',');
	getline(iff,safety,',');
	getline(iff,class_v,'\n');

	off<<buying<<","<<maint<<","<<doors<<","<<persons<<","<<lug_bot<<","<<safety<<",";
	if(class_v=="unacc") off<<"0"<<endl;
	if(class_v=="acc") off<<"1"<<endl;
	if(class_v=="good") off<<"2"<<endl;
	if(class_v=="vgood") off<<"3"<<endl;
}

}

int main()
{
rewrite_data();
}
