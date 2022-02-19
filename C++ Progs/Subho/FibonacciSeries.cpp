#include<iostream>
using namespace std;
int main(){
	int n,a,b,c,count=0;
	cout<<"Enter how many terms you want : ";
	cin>>n;
	a=0;
	b=1;
	n-=2;
	cout<<"\nFIBONACCI SERIES\n";
	cout<<a<<"\t"<<b<<"\t";
	while(count<n){
		c=a+b;
		cout<<c<<"\t";
		a=b;
		b=c;
		count+=1;
	}
}
