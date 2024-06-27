#include <iostream>

using namespace std;

template<typename ...Is>
int sum(Is... is)
{
    return (is + ...);
}


int main()
{
    cout << sum(1, 2, 3, 4, 5) << endl;
    cout << "Hello, World!" << endl;
    return 0;
}