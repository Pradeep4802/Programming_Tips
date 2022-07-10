// 1. WAP to print linearly from 1 to N(But by backtracking)
// 2. WAP to print linearly from N to 1(But by backtracking)

#include<iostream>
using namespace std;

// void printNumber1 (int n ) {
//     if(n <= 0)
//         return;
//     printNumber1(n-1);
//     cout << n << endl;
// }

void printNumber2 (int n, int m ) {
    if(n <= 0)
        return;
    printNumber2(n-1,m+1);
    cout << m << endl;
}

int main() {
    int n,m=1;
    cout << "Enter the N: ";
    cin >> n;
    // printNumber1(n);
    printNumber2(n,m);
    return 0;
}