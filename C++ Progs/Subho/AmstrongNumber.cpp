#include<iostream>
#include<math.h>
using namespace std;
int main(){
	int n,x,sum=0,rem=0;
	cout<<"Enter a number to check :";
	cin>>n;
	x=n;
	while(n>0){
		rem=n%10;
		sum=sum+pow(rem,3);
		n=n/10;
	}
	if(x==sum)
		cout<<"Entered number is a Amstrong Number";
	else cout<<"Entered number is not a Amstrong Number";	
}
