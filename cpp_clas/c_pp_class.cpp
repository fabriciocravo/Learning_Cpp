#include <iostream>
#include <vector>


void notation(){
    // loops
    std::vector<int> qv1 = {1, 2, 3, 4, 5};

    for ( auto value : qv1 ){
        std::cout << value << " ";
    }
    std::cout << std::endl;
}

int main(){
    notation();
    return 0;
}
