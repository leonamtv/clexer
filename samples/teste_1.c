#include <stdio.h>
#include <assert.h>
#include <ctype.h>

#define BATATA 12312312

#pragma startup func1  
#pragma exit func2  

/*
    Teste de bloco de comentário
*/
int main() {
    char c;
    int lowercase_vowel, uppercase_vowel;
    int i = 0;

    printf("Enter an alphabet: ");
    scanf("%c", &c);

    // evaluates to 1 if variable c is a lowercase vowel
    lowercase_vowel = (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');

    // evaluates to 1 if variable c is a uppercase vowel
    uppercase_vowel = (c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U');


    for ( i = 0; i < 10; ++i ) {
        do {
            i += 0;
        } while ( i < 2 );
    }

    // evaluates to 1 (true) if c is a vowel
    if (lowercase_vowel || uppercase_vowel)
        printf("%c is a vowel.", c);
    else
        printf("%c is a consonant.", c);
    return 0;
}