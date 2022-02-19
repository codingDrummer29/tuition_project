#include<stdio.h>
int main(){
	char a1[10],a2[10];
	int i,sum=0;
	printf("\nEnter a binary number : ");
	scanf("%s",a1);
	printf("%s",a1);
	
	while(a1[i]!='\0')
	{	if(a1[i]=='1')
			sum++;
		i++;
	}
	
	if(sum%2==0)
		{	printf("\nNo Error present in Sender side");
			
		}
	else printf("\nError Present in Sender side");	
	printf("\n%d",sum);
	
	return 0;
}
