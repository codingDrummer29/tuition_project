#include<stdio.h>
int main(){
    int a[4],b[4],r[3], s[3],i,q[3];
    printf("\nenter 4 bit data word:\n");
    for(i=3;i>=0;i--){
scanf("%d",&a[i]);
    }
    r[0]=(a[2]+a[1]+a[0])%2;
    r[1]=(a[2]+a[1]+a[3])%2;
    r[2]=(a[0]+a[1]+a[3])%2;
    printf("\n\nthe 7bit hamming code word: \n");
    for(i=3;i>=0;i--){
printf("%d\t",a[i]);
    }
    for(i=2;i>=0;i--){
printf("%d\t",r[i]);
    }
    printf("\n");
    printf("\nenter the 4bit recieved word: ");
    for(i=3;i>=0;i--)
scanf("%d",&b[i]);
    //calculating syndrome bits
    s[0]= (b[2]+b[1]+b[0]+r[0])%2;
    s[1]= (b[3]+b[2]+b[1]+r[1])%2;
    s[2]= (b[0]+b[1]+b[3]+r[2])%2;
    printf("\nsyndrome is: \n");
    for(i=2; i>=0;i--){
printf("%d",s[i]);
    }
    if((s[2]==0) && (s[1]==0) && (s[0]==0))
printf("\n RECIEVED WORD IS ERROR FREE\n");
    if((s[2]==1) && (s[1]==0) && (s[0]==1))
printf("\nrecieved word is error with error in 1bit(b0) position from right\n");
    if((s[2]==1) && (s[1]==1) && (s[0]==1))
printf("\nrecieved word is error with error in 2bit(b1) position from right\n");
    if((s[2]==0) && (s[1]==1) && (s[0]==1))
printf("\nrecieved word is error with error in 3bit(b2) position from right\n");
    if((s[2]==1) && (s[1]==1) && (s[0]==0))
printf("\nrecieved word is error with error in 4bit(b3) position from right\n");
    return(1);
}

