Run the following commands on terminal:
 
 sudo apt-get update

sudo apt-get intall flex

sudo apt-get intall byacc

sudo apt-get intall bison


sudo apt-get intall bison++

sudo apt-get intall byacc-j

Compiling and Running LEX Programs:
flex hello.l
gcc lex.yy.c 
./a.out


Compiling and Running YACC Programs:

lex calc. l
yacc calc. y 
calc. y: 39 parser name defined to default : "parse" 
gcc lex.yy.c y.tab.c -w 
. /a.out 

//OUTPUT:
Enter Any Arithmetic Expression which can 
have operations Addition, Subtraction,  Multiplication, Division Modulus and Round brackets
4+5 
Result=9 
Entered arithmetic expression is Valid 


![image](https://github.com/zzeeuusss/spcc/assets/89004033/bd24810b-1444-4f4e-b971-0e60118c3245)


