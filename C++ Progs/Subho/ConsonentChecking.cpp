#include<iostream>
using namespace std;
int main(){
	char c;
	cout<<"Enter a charecter to check : ";
	cin>>c;
	if(c!='u'&& c!='o' && c!='i' && c!='e' && c!='a' && c!='U' && c!='O' && c!='I' && c!='E' && c!='A')
		cout<<"Entered charecter "<<c<<" is a CONSONENT";
	else cout<<"Entered charecter "<<c<<" is not a CONSONENT";
}
