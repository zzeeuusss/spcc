%{
    #include<stdio.h>
    int vow_count=0;
    int yywrap();
%}

%%
[aeiouAEIOU] {
    vow_count++;
}
%%

int yywrap(){
    return 1;
}

int main(){
    yylex();
    printf("No of vowels are: %d",vow_count);
    return 0;
}
