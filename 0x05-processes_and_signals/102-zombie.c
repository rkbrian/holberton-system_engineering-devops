#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * main - Function to create zomibie processes
 * Return: 0
 */
int main()
{
  pid_t process_id;
  int i;

  for (i = 0; i < 5; i++)
    {
      process_id = fork();
      if (process_id == 0)
	exit(0);
	
      printf("Zombie process created, PID: %d\n", process_id);
    }
  infinite_while();
  return (0);
}

/**
 * infinite_while - the loop function
 * Return: 0
 */
int infinite_while(void)
{
  while (1)
    {
      sleep(1);
    }
  return (0);
}
