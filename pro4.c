#include<stdio.h>
#include<conio.h>
int main()
{
int a[10]={3,2,6,5,4,1,8,7,9};
int i,j,temp,b;
 clrscr();
 for(i=0;i<10;i++)
 {
 for(j=i+1;j<10];j++)
 {
 if(a[i]<a[j])
 {
  temp=a[i];
   a[i]=a[j];
   a[j]=temp;
 }
  for(i=0;i<10;i++)
  {
    printf("%d",a[i]);
  }
  b=10/2;
  printf("the minimum number is :%d",a[b]);
  getch();
 }
