#include <stdio.h>

int main() {
    printf("%s\n", "Hello, World!");

    /* Defining variables */
    int foo;
    int bar = 1;

    /* Mathematical Operation */
    int a = 0, b = 1, c = 2, d = 3, e = 4;
    a = b - c + d * e;

    printf("%d\n", a);

    /* Defining Boolean variables */
    #define BOOL char
    #define FALSE 0
    #define TRUE 1

    /* Define an array of 10 ints */
    int numbers[10];

    /* Populating the array */
    numbers[0] = 1;
    numbers[1] = 2;
    numbers[2] = 3;
    numbers[3] = 4;
    numbers[4] = 5;
    numbers[5] = 6;
    numbers[6] = 7;
    numbers[7] = 8;
    numbers[8] = 9;
    numbers[9] = 10;

    printf("The 7th number in the array is %d\n", numbers[6]);

    /* Multidimensional Array */

    // Defining 3D array?
    int myM3DArray[1][2][3];

    // Defining 2D array
    char vowels[1][5] = {
        {'a', 'e', 'i', 'o', 'u'}
    };

    /* 
    * 2D arrays follow this structure:
    * type arrayName[x][y]
    * However, you don't necessarily need an x co-ord, as shown here:
    */

   char voWels[][5] = {
       {'A', 'E', 'I', 'O', 'U'},
       {'a', 'e', 'i', 'o', 'u'}
   };
}
