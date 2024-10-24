
#include <iostream>
#include <bits/stdc++.h>

using namespace std;    


char * foo(char *string){
    char* tmp = strdup(string);
    char shift = tmp[1] - tmp[0];

    for(int i = 0; i < strlen(tmp); i++){
        tmp[i] += shift;
    }

    return tmp;
}

int main(){
    char *string = "mnnckdr";
    char *result = foo(string);
    cout << result << endl;
    return 0;
}