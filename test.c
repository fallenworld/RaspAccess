#include <stdlio.h>
#include "test.h"

int* print_1(char** str, struct svc_req* req)
{
    static int result;
    printf("%s\n", *str);
    result = 1;
    return result;
}
