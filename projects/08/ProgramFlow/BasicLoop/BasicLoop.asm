//push constant 0
@0
D=A
@SP
AM=M+1
A=A-1
M=D

//pop local 0
@LCL
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

//label LOOP_STAR
(dummyfunction$LOOP_STAR)

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

//push local 0
@0
D=A
@LCL
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

//pop local 0
@LCL
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

//if-goto LOOP_STAR
@SP
AM=M-1
D=M
@dummyfunction$LOOP_STAR
D;JNE

//push local 0
@0
D=A
@LCL
A=M
A=A+D
D=M
@SP
AM=M+1
A=A-1
M=D

