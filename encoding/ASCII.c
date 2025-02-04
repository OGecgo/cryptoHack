#include <stdio.h>

//48 -> 0
int addNumLeft(int num, char strNum){
    num *= 10;
    strNum -= 48;
    int addNum = (int)(strNum);

    return num + strNum;
}

int addStrToNum(int num, char* str){
    if (str == NULL) return -1;

    int i = 0;
    while(str[i] != '\0'){
        num += addNumLeft(num, str[i]);
        i++;
    }

    return num;
}

//take text similar to [a,b , c, ... ,n,]
void strIntToASCIIprint(char* str){
    
    if (str == NULL && str[0] != '[') return;
    
    char asciiInt[3];
    int i = 1;
    int j = 0;

    while(str[i] != ']'){
        if (str[i] == '\0') return; //not end propertly
        if (str[i] == ' '){ i++; continue; } // dont consider the spaces
        
        if (str[i] == ','){ //for every block on [a,b , c, ... ,n,]

            int numBlock = 0;
            int k = 0;
            while (k < j){
                numBlock = addNumLeft(numBlock, asciiInt[k]);
                k++;
            }
            j = 0;
            i++;
            printf("%c", numBlock);
            continue;
        }
        asciiInt[j] = str[i];
        j++;
        i++;
    }
    return;
}


int main (){
    char* str;
    printf("Give a text similar [a,b , c, ...]: ");
    scanf("%[^\n]", str); //[99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125,]

    strIntToASCIIprint(str);

    return 0;
}