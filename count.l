%{

int char_count = 0, word_count = 0, sentence_count = 0, line_count = 0;

int tab_count = 0, number_count = 0, blank_count = 0;

%}

%%

[ \t]+ {

int i;

for(i=0; yytext[i]!='\0'; i++) {

if(yytext[i]==' ') blank_count++;

if(yytext[i]=='\t') tab_count++;

}

word_count++;

char_count += yyleng;

}

[0-9]+ { number_count++; char_count += yyleng; }

[.!?] { sentence_count++; char_count += yyleng; }

\n { line_count++; char_count++; }

[a-zA-Z]+ { word_count++; char_count += yyleng; }

. { char_count++; }

%%

int main() {

printf("Enter text (Ctrl+Z to end on Windows):\n");

yylex();

printf("\nCharacters: %d\n", char_count);

printf("Words: %d\n", word_count);

printf("Sentences: %d\n", sentence_count);

printf("Lines: %d\n", line_count);

printf("Tabs: %d\n", tab_count);

printf("Numbers: %d\n", number_count);

printf("Blank spaces: %d\n", blank_count);

return 0;

}

int yywrap() { return 1; }


// To run the code
// flex count.l
// gcc lex.yy.c -o count exe
// count.exe
