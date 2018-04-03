#include<stdio.h>
#include<string.h>
void main()
{
  int l=0,i,n;
  printf("enter the number:");
  scanf("%d",&n);
  while(n%2==0)
  {
      i=n/2;
      printf("%d\t",i);
      n=i;
  }
 }
