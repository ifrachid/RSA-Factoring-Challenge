#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(int argc, char* argv[])
{
	if (argc != 2)
	{
		printf("Usage: factors <file>\n");
		return 1;
	}
	// Open the input file
	FILE* fp = fopen(argv[1], "r");
	if (!fp)
	{
    		printf("Error: Could not open file %s\n", argv[1]);
    		return 1;
	}

	// Read and process each number in the file
	int n;
	while (fscanf(fp, "%d", &n) == 1)
	{
    		int limit = sqrt(n);
    		for (int i = 2; i <= limit; i++)
		{
        		if (n % i == 0)
			{
            			printf("%d=%d*%d\n", n, i, n / i);
            			break;
        		}
    		}
	}

	// Close the file
	fclose(fp);
	return 0;
}
