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

//function Sys.init 0
(Sys.init)

//push constant 4000
@4000
D=A
@SP
AM=M+1
A=A-1
M=D

//pop pointer 0
@3
D=A
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

//push constant 5000
@5000
D=A
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

//call Sys.main 0
@Sys.main$ret.0
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
@Sys.main
0;JMP
(Sys.main$ret.0)

//pop temp 1
@5
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

//label LOO
(Sys.init$LOO)

//goto LOO
@Sys.init$LOO
0;JMP

//function Sys.main 5
(Sys.main)
@0
D=A
@SP
AM=M+1
A=A-1
M=D
@0
D=A
@SP
AM=M+1
A=A-1
M=D
@0
D=A
@SP
AM=M+1
A=A-1
M=D
@0
D=A
@SP
AM=M+1
A=A-1
M=D
@0
D=A
@SP
AM=M+1
A=A-1
M=D

//push constant 4001
@4001
D=A
@SP
AM=M+1
A=A-1
M=D

//pop pointer 0
@3
D=A
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

//push constant 5001
@5001
D=A
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

//push constant 200
@200
D=A
@SP
AM=M+1
A=A-1
M=D

//pop local 1
@LCL
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

//push constant 40
@40
D=A
@SP
AM=M+1
A=A-1
M=D

//pop local 2
@LCL
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

//push constant 6
@6
D=A
@SP
AM=M+1
A=A-1
M=D

//pop local 3
@LCL
D=M
@3
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

//push constant 123
@123
D=A
@SP
AM=M+1
A=A-1
M=D

//call Sys.add12 1
@Sys.add12$ret.1
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
@Sys.add12
0;JMP
(Sys.add12$ret.1)

//pop temp 0
@5
D=A
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

//push local 1
@1
D=A
@LCL
A=M
A=A+D
D=M
@SP
AM=M+1
A=A-1
M=D

//push local 2
@2
D=A
@LCL
A=M
A=A+D
D=M
@SP
AM=M+1
A=A-1
M=D

//push local 3
@3
D=A
@LCL
A=M
A=A+D
D=M
@SP
AM=M+1
A=A-1
M=D

//push local 4
@4
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

//function Sys.add12 0
(Sys.add12)

//push constant 4002
@4002
D=A
@SP
AM=M+1
A=A-1
M=D

//pop pointer 0
@3
D=A
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

//push constant 5002
@5002
D=A
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

//push constant 12
@12
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

