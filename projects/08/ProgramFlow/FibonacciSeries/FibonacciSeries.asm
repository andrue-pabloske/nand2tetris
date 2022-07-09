//push argument 1
@1
D=A
@ARG
A=M
A=A+D
D=M
@SP
AM=M+1
A=A-1
M=D

//pop pointer 1
@3
D=A
@1
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

//push constant 0
@0
D=A
@SP
AM=M+1
A=A-1
M=D

//pop that 0
@THAT
D=M
@0
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

//push constant 1
@1
D=A
@SP
AM=M+1
A=A-1
M=D

//pop that 1
@THAT
D=M
@1
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

//push argument 0
@0
D=A
@ARG
A=M
A=A+D
D=M
@SP
AM=M+1
A=A-1
M=D

//push constant 2
@2
D=A
@SP
AM=M+1
A=A-1
M=D

//sub
@15
D=A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
@14
D=A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
@15
D=M
@14
D=M-D
@SP
AM=M+1
A=A-1
M=D

//pop argument 0
@ARG
D=M
@0
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

//label MAIN_LOOP_STAR
(dummyfunction$MAIN_LOOP_STAR)

//push argument 0
@0
D=A
@ARG
A=M
A=A+D
D=M
@SP
AM=M+1
A=A-1
M=D

//if-goto COMPUTE_ELEMEN
@SP
AM=M-1
D=M
@dummyfunction$COMPUTE_ELEMEN
D;JNE

//goto END_PROGRA
@dummyfunction$END_PROGRA
0;JMP

//label COMPUTE_ELEMEN
(dummyfunction$COMPUTE_ELEMEN)

//push that 0
@0
D=A
@THAT
A=M
A=A+D
D=M
@SP
AM=M+1
A=A-1
M=D

//push that 1
@1
D=A
@THAT
A=M
A=A+D
D=M
@SP
AM=M+1
A=A-1
M=D

//add
@15
D=A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
@14
D=A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
@15
D=M
@14
D=D+M
@SP
AM=M+1
A=A-1
M=D

//pop that 2
@THAT
D=M
@2
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

//push pointer 1
@1
D=A
@3
A=A+D
D=M
@SP
AM=M+1
A=A-1
M=D

//push constant 1
@1
D=A
@SP
AM=M+1
A=A-1
M=D

//add
@15
D=A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
@14
D=A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
@15
D=M
@14
D=D+M
@SP
AM=M+1
A=A-1
M=D

//pop pointer 1
@3
D=A
@1
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

//push argument 0
@0
D=A
@ARG
A=M
A=A+D
D=M
@SP
AM=M+1
A=A-1
M=D

//push constant 1
@1
D=A
@SP
AM=M+1
A=A-1
M=D

//sub
@15
D=A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
@14
D=A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
@15
D=M
@14
D=M-D
@SP
AM=M+1
A=A-1
M=D

//pop argument 0
@ARG
D=M
@0
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

//goto MAIN_LOOP_STAR
@dummyfunction$MAIN_LOOP_STAR
0;JMP

//label END_PROGRA
(dummyfunction$END_PROGRA)

