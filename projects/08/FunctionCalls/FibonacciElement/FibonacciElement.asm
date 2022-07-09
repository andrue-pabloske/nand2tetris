//bootstrap code
//SP = 256
@256
D=A
@SP
M=D

//call Sys.init 0
@Sys.init$ret.0
D=A
@SP
AM=M+1
A=A-1
M=D
@LCL
D=M
@SP
AM=M+1
A=A-1
M=D
@ARG
D=M
@SP
AM=M+1
A=A-1
M=D
@THIS
D=M
@SP
AM=M+1
A=A-1
M=D
@THAT
D=M
@SP
AM=M+1
A=A-1
M=D
@SP
D=M
@LCL
M=D
@5
D=D-A
@ARG
M=D
@Sys.init
0;JMP
(Sys.init$ret.0)

//function Main.fibonacci 0
(Main.fibonacci)

//push argument 0
@ARG
D=M
@0
A=D+A
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

//lt
@SP
AM=M-1
D=M
@R15
M=D
@SP
AM=M-1
D=M
@R14
M=D
@logical.0
0;JMP
(logical$TRUE.0)
D=-1
@logical$ret.0
0;JMP
(logical$FALSE.0)
D=0
@logical$ret.0
0;JMP
(logical.0)
@15
D=M
@14
D=M-D
@logical$TRUE.0
D;JLT
@logical$FALSE.0
0;JMP
(logical$ret.0)
@SP
AM=M+1
A=A-1
M=D

//if-goto IF_TRU
@SP
AM=M-1
D=M
@Main.fibonacci$IF_TRU
D;JNE

//goto IF_FALS
@Main.fibonacci$IF_FALS
0;JMP

//label IF_TRU
(Main.fibonacci$IF_TRU)

//push argument 0
@ARG
D=M
@0
A=D+A
D=M
@SP
AM=M+1
A=A-1
M=D

//return
@LCL
D=M
@R14
M=D
@5
A=D-A
D=M
@R15
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@R14
D=M
@1
A=D-A
D=M
@THAT
M=D
@R14
D=M
@2
A=D-A
D=M
@THIS
M=D
@R14
D=M
@3
A=D-A
D=M
@ARG
M=D
@R14
D=M
@4
A=D-A
D=M
@LCL
M=D
@R15
A=M
0;JMP

//label IF_FALS
(Main.fibonacci$IF_FALS)

//push argument 0
@ARG
D=M
@0
A=D+A
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
@SP
AM=M-1
D=M
@R15
M=D
@SP
AM=M-1
D=M
@R14
M=D
@15
D=M
@14
D=M-D
@SP
AM=M+1
A=A-1
M=D

//call Main.fibonacci 1
@Main.fibonacci$ret.1
D=A
@SP
AM=M+1
A=A-1
M=D
@LCL
D=M
@SP
AM=M+1
A=A-1
M=D
@ARG
D=M
@SP
AM=M+1
A=A-1
M=D
@THIS
D=M
@SP
AM=M+1
A=A-1
M=D
@THAT
D=M
@SP
AM=M+1
A=A-1
M=D
@SP
D=M
@LCL
M=D
@6
D=D-A
@ARG
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.1)

//push argument 0
@ARG
D=M
@0
A=D+A
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
@SP
AM=M-1
D=M
@R15
M=D
@SP
AM=M-1
D=M
@R14
M=D
@15
D=M
@14
D=M-D
@SP
AM=M+1
A=A-1
M=D

//call Main.fibonacci 1
@Main.fibonacci$ret.2
D=A
@SP
AM=M+1
A=A-1
M=D
@LCL
D=M
@SP
AM=M+1
A=A-1
M=D
@ARG
D=M
@SP
AM=M+1
A=A-1
M=D
@THIS
D=M
@SP
AM=M+1
A=A-1
M=D
@THAT
D=M
@SP
AM=M+1
A=A-1
M=D
@SP
D=M
@LCL
M=D
@6
D=D-A
@ARG
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.2)

//add
@SP
AM=M-1
D=M
@R15
M=D
@SP
AM=M-1
D=M
@R14
M=D
@15
D=M
@14
D=D+M
@SP
AM=M+1
A=A-1
M=D

//return
@LCL
D=M
@R14
M=D
@5
A=D-A
D=M
@R15
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@R14
D=M
@1
A=D-A
D=M
@THAT
M=D
@R14
D=M
@2
A=D-A
D=M
@THIS
M=D
@R14
D=M
@3
A=D-A
D=M
@ARG
M=D
@R14
D=M
@4
A=D-A
D=M
@LCL
M=D
@R15
A=M
0;JMP

//function Sys.init 0
(Sys.init)

//push constant 4
@4
D=A
@SP
AM=M+1
A=A-1
M=D

//call Main.fibonacci 1
@Main.fibonacci$ret.3
D=A
@SP
AM=M+1
A=A-1
M=D
@LCL
D=M
@SP
AM=M+1
A=A-1
M=D
@ARG
D=M
@SP
AM=M+1
A=A-1
M=D
@THIS
D=M
@SP
AM=M+1
A=A-1
M=D
@THAT
D=M
@SP
AM=M+1
A=A-1
M=D
@SP
D=M
@LCL
M=D
@6
D=D-A
@ARG
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.3)

//label WHIL
(Sys.init$WHIL)

//goto WHIL
@Sys.init$WHIL
0;JMP

