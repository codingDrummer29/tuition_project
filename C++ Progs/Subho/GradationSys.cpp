#include<iostream>
using namespace std;
int main(){
	int n;
	char c;
	cout<<"Enter a number to check : ";
	cin>>n;
	
	if(n>=91)
		c='O';
	else if(n>=81 && n<=90)
			c='E';
		else if(n>=71 && n<=80)
				c='A';
			else if(n>=61 && n<=70)
					c='B';
				else if(n>=51 && n<=60)
						c='C';
					else if(n>=41 && n<=50)
							c='D';
						else c='F';
						
	cout<<"\n\n";
	switch(c){
		case 'A' :	cout<<"Student has recieved : "<<c<<" grade. Remark -> VERY GOOD.";
		case 'B' :	cout<<"Student has recieved : "<<c<<" grade. Remark -> GOOD.";
		case 'C' :	cout<<"Student has recieved : "<<c<<" grade. Remark -> SATISFACTORY.";
		case 'D' :	cout<<"Student has recieved : "<<c<<" grade. Remark -> PASS.";
		case 'E' :	cout<<"Student has recieved : "<<c<<" grade. Remark -> EXCELENT.";
		case 'F' :	cout<<"Student has recieved : "<<c<<" grade. Remark -> FAIL.";
		case 'O' :	cout<<"Student has recieved : "<<c<<" grade. Remark -> OUTSTANDING.";
	}					
}
