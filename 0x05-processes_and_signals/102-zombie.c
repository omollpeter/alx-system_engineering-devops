#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * infinite_while - Creates an infinite loop
 *
 * Return: 0 (Success)
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Creates zombie processes
 *
 * Return: 0 (Success)
 */
int main(void)
{
	int count = 0;
	pid_t pid;

	while (count < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %u\n", pid);
		}
		else
			exit(0);
		count++;
	}

	infinite_while();
	return (0);
}
