Run the following commands on terminal:
 
 sudo apt-get update

sudo apt-get intall flex

sudo apt-get intall byacc

sudo apt-get intall bison


sudo apt-get intall bison++

sudo apt-get intall byacc-j

Compiling and Running LEX Programs:
flex hello.I 
gcc lex.yy.c
./a.out

Compiling and Running YACC Programs:
flex hello.I
bison -d hello.y 
gcc lex.yy.c y.tab.c
./a.out


