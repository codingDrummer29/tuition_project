#include<iostream>
using namespace std;

int main(){
	
	int i,j,k,n=4;
	
	for(i=1;i<=n;i++){ //to control rows
		k=i;
		for(j=1;j<=n;j++){ //to control cols
			
			if(k>n){ //resetting the value of k
				k=1;
				cout<<k;
				k++;
			}
				
			else if(j==1){ //controlling the first o/p of each row
					cout<<k;
					k++;
				 } 
				
				else { // gen. print
					cout<<k;
					k++;
				}
		} //end of col loop
		
		cout<<"\n"; // row changing
	} // end of row loop
	
}
