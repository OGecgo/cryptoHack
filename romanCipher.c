#include <stdio.h>
#include <stdlib.h>

int strLength (unsigned char * text){
    if (text == NULL) return 0;

    int i = 0;
    while (text[i] != '\0'){
        i++;
    }
    return i;
}

// Function only for uppercase letters
void romanCipher (unsigned char* codedText){

    int length = strLength(codedText);

    for (int i = 65; i < 91; i++){
        int letterKey = i - 65;
        for (int j = 0; j < length; j++){
            if (codedText[j] == ' '){
                printf("%c", ' ');
                continue;
            }

            int character = codedText[j] + letterKey;
            if (character > 90) character -= 26;

            printf("%c", character);//just look for real words
        }
        printf("\n");
    }

}

int main (){
    unsigned char *text;
    scanf("%[^\n]", text);
    
    romanCipher(text);
    return 0;
}