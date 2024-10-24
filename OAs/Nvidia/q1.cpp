#include <iostream>
#include <vector>

using namespace std;

vector<int> my_func(string s) {
    int n = s.size();
    vector <int> a(n);
    for (int i = 0; i < n; i++) {
        while(i + a[i] < n && s[a[i]] == s[i + a[i]]) {
            a[i]++;
        }
    }
    return a;
}


int main() {
    string s;
    cin >> s;
    vector <int> a = my_func(s);
    for (int i = 0; i < a.size(); i++) {
        cout << a[i] << " ";
    }
    return 0;
}