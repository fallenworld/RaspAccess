#include <stdio.h>
#include <string.h>
#include "access.h"

int main(int argc, char* argv[])
{
    //Check the arguments counts
    if (argc != 3)
    {
        printf("Two arguments are required\n");
        exit(1);
    }
    //Create client
    char* server_address = argv[1];
    CLIENT* client = clnt_create(server_address, ACCESSPROG, ACCESSVERS, "tcp");
    //Check if client successfully created
    if (client == NULL)
    {
        clnt_pcreateerror(server_address);
        exit(1);
    }
    //Excute the function
    int arg = 0;
    int* result = NULL;
    char* command = argv[2];
    if (strcmp(command, "open") == 0)
    {
        result = open_door_1(&arg, client);
    }
    else if (strcmp(command, "close") == 0)
    {
        result = close_door_1(&arg, client);
    }
    else
    {
        printf("Wrong argument\n");
        exit(1);
    }
    //Check the result from the remote
    if (result == NULL)
    {
        clnt_perror(client, server_address);
        exit(1);
    }
    else if (*result == 0)
    {
        printf("Success\n");
    }
    clnt_destroy(client);
    return 0;
}


