#include <iostream>

using namespace std;



int sum(int n){ /*Ex 1*/
    if(n <=0){
        return 0;
    }
    return n + sum(n-1);
}

int pairSum(int a, int b){
    
    return a + b;
}

int pairSumSequence(int n){ /* Ex 2*/
    int sum = 0;
    for (int i = 0; i < n; i ++){
        sum += pairSum(i, i + 1);
    }

    return sum;
}




int main()
{
    cout<<pairSumSequence(5)<<endl;
    return 0;
}