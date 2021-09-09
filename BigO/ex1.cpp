#include <iostream>
#include <array>
using namespace std;


void foo(int[] array) {
        int sum = 0;
        int product = 1;
        for (int i = 0; i < array.length; i++){
            sum += array[i];
        }
        for (int i = 0; i < array.length; i++){
            product *= array[i];
        }
        cout << sum << ", " << product << endl;
    }
int main(){

    int arr [] = {1,2,3,4,5};
    foo(arr);
    
    return 0;
}
