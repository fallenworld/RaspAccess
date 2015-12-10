#include <stdio.h>
#include "access.h"

//Open the door
int* open_door_1_svc(int* void_arg, struct svc_req* req)
{
    static int result;
    printf("Door opened\n");
    result = 0;
    return &result;
}

//Close the door
int* close_door_1_svc(int* void_arg, struct svc_req* req)
{    
    static int result;
    printf("Door closed\n");
    result = 0;
    return &result;
}
