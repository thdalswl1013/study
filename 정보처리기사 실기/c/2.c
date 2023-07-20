#include <stdio.h>

int main()
{
	int number = 1234;
	int div = 10, result = 0;

	while (number > 0)
	{
		result *= div; 
		printf("%d\n", result);

		result = result + number % div;
		printf("%d\n", result);

		number /= div;
		printf("%d\n", result);

		printf("-------------------------------------------------\n");
	}

	printf("\n\n%d\n\n", result);
}