#include <iostream>
#include <random>

int main() {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(0, 1);

    long n = 100000000000;
    long count = 0;
    for (long i = 0; i < n; i++) {
        double x = dis(gen);
        double y = dis(gen);
        if (x * x + y * y <= 1) {
            count++;
        }
        std::cout << i << std::endl;
    }
    std::cout << 4.0 * count / n << std::endl;
}