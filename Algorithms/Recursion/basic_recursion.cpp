
#include <iostream>

using namespace std;

int count = 0;

int recursion(){
    if (count == 3){
        return 0;
    }
    cout << count <<endl;
    count++;
    recursion();
}

int main(){
    recursion();
}