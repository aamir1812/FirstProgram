#include <stdio.h>

int main(){
    int i = 10;
    int j= i;
    printf("the value of i is %d and the value of j is %d\n", i, j);

    // put value in 1 line.
    int a= 5, b=2,c=3;
    printf("%d\n",a);
    printf("%d\n",b);
    printf("%d\n",c);

    // +,-,*,a%b,/ is opreters.
    int a2=4;
    int a3=5;
    int a1= a2+a3;  
    printf("the value of a1 is %d\n",a1);
    printf("the value of Remainder is%d\n",a2%a3); // a%b is using for Remainder.

    // int+int=int, int+float=float, float+float= float.
    int b1 = 5;
    int b2 = 2;
    float b3 = b1/b2;
    printf("%f\n",b3);   // out-put show 2 becouse int and int always be int.

    int c1= 5;
    float c2= 2;
    float c3= c1/c2;
    printf("%f\n",c3); //  out-put show 2.5 becouse int and float always be float.

    float e1 = 5;
    float e2 = 2;
    float e3= e1/e2;
    printf("%f\n",e3);  //  out-put show 2.5 becouse float and float always be float.

    // calculation in c.

    int f1 = 2;
    int f2 = 3;
    int f = 5;
    printf("%d\n", f1*f2/f); // sequens flow left to right.
    printf("%d\n", f1*f2+f/f1); // now sequance follow first */% then +-.

    // change data type.

    float g= 4.5;
    int h= (int) g;
    printf("%d",h);

    return 0;
}