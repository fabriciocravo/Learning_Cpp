std::vector<int> values(5);

std::default_random_engine engine;
std::uniform_int_distribution distrib{0, 9};

int main(){
    for (auto &value : values) {
        value = distrib(engine);
    }

    for (auto value : values) {
        std::cout << value << " ";
    }
    std::cout << std::endl;

    return 0;
}
