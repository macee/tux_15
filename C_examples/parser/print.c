#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <sys/time.h>
#include "line_parser.h"

int main(void){
  char line[100];
  uint8_t i;
  uint8_t num_fields;
  uint8_t num_char_in_field;
  struct timeval time_now;

    while(fgets(line, 100, stdin) != NULL){

        // Linux time stamp
            gettimeofday(&time_now, NULL);

        /* remove newline, if present */
            i = strlen(line)-1;
            if( line[ i ] == '\n')
            line[i] = '\0';

        /* FIXME after you have program working */
            sprintf(line, "%s", "$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47");


        num_fields = line_parser(line, ',');


        /* Operate on the GGA strings */
            get_field(line, 1);
            if(strncmp(line, "$GPGGA", 6))
                continue;


        /* Verify line has correct number of fields*/
            if (num_fields != 15)
                continue;


        /* FIXME after you have program working */
            printf("\nThe string \"%s\" contains %d fields.  The individual fields are: \n", line, num_fields);
            for (i = 1; i <= num_fields; i++){
                num_char_in_field = get_field(line, i);
                fprintf(stdout, "\tfield %d with length %d = %s\n",i, num_char_in_field, line );
            }

    // fprintf(stdout, "%ld, %s\n", time_now.tv_sec, line);

    }
    return 0;
}