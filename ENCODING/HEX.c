#include <stdio.h>
#define ascii0 48
#define ascii9 57
#define asciia 97
#define asciif 102

// Convert a single hexadecimal character to its integer value and add it to the current number
int addHexDigitToNumber(int num, char hex){    
    num *= 16; //Shift the current number left by 4 bits (equivalent to multiplying by 16)
    //convert stringHex to dec
    if (hex >= ascii0 && hex <= ascii9) num += (int)(hex - ascii0);
    else if (hex >= asciia && hex <= asciif) num += (int)(hex - asciia + 10);

    return num;
}

//take text similar to [a,b , c, ... ,n,]
void HexToASCIIprint(char* str){
    
    if (str == NULL) return;
    
    char asciiInt[2]; //ascii have only to digits
    int i = 0;
    int j = 0;

    while(str[i] != '\0'){

        asciiInt[j] = str[i];

        if (j == 1){
            int num = addHexDigitToNumber(0, asciiInt[0]);
            num = addHexDigitToNumber(num, asciiInt[1]);
            asciiInt[0] = ' ';
            asciiInt[1] = ' ';
            j = 0;
            i++;
            printf("%c", num);
            continue;
        }

        j++;
        i++;
    }
    printf("\n");
    return;
}


int main (int argc, char* argv[]){
    char* str;
    printf("Give a hex number: ");
    scanf("%s", str); //63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d

    HexToASCIIprint(str);
    return 0;
}