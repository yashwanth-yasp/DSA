#include <bits/stc++.h>

using namespace std;

int main(){
	list <int> line;
	line = {1,2,3,4,5,6,7,8};
	cout << line.size() << endl;
	line.push_back(30);
	for (auto i : line){
		cout << i;
	}
}
