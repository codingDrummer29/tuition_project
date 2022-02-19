#include<stdio.h>
int main()
{
int data[10],i,count=0,rec[10],count1=0;
printf("\n enter 7 bit one by one:\n");
for(i=0;i<7;i++)
{
scanf("%d",&data[i]);
}
for(i=0;i<7;i++)
if(data[i]==1)
{
count++;
}
if(count%2==0)
data[7]=1;
else
data[7]=1;
printf("enter the reciever data\n");
for(i=0;i<7;i++)
{
scanf("%d",&rec[i]);
}
for(i=0;i<7;i++)
{
if(rec[i]==1)
count++;
}
if(count1%2==0)
printf("message is recived\n");
else
printf("error occured\n");
return 0;
}
