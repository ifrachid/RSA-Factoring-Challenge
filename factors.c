#include <stdio.h>

void factorize_number(int n) {
    for (int i = 2; i <= n / 2; ++i) {
        if (n % i == 0) {
            printf("%d=%d*%d\n", n, i, n / i);
            return;  // Assuming you only want one factorization per line
        }
    }
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <file>\n", argv[0]);
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    int number;
    while (fscanf(file, "%d", &number) == 1) {
        factorize_number(number);
    }

    fclose(file);

    return 0;
}
