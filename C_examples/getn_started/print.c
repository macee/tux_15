#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <sys/time.h>
#include <unistd.h>

int main(void){
  char line[100];
  int i;
  struct timeval time_now;

    while(fgets(line, 100, stdin) != NULL){

        // Linux time stamp data
            gettimeofday(&time_now, NULL);

        /* remove newline, if present */
            i = strlen(line)-1;
            if( line[ i ] == '\n')
            line[i] = '\0';

    fprintf(stdout, "%ld, %s\n", time_now.tv_sec, line);
    sleep(1);

    }
    return 0;
}