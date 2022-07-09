// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

//LOOP:
//if(KBD!=0) goto FILL
//ERASE
//goto LOOP
//FILL
//goto LOOP

(LOOP)
	@i
	M=0
	//if(KBD!=0) goto FILL
	@KBD
	D=M
	@FILL
	D;JNE
(ERASE)
	//RAM[SCREEN+i] = 0
	@SCREEN
	D=A
	@i
	D=D+M
	A=D
	M=0
	@i
	M=M+1
	//if(i>8191)goto LOOP
	//else goto ERASE
	@8191
	D=A
	@i
	D=M-D
	@LOOP
	D;JGT
	@ERASE
	0;JMP
(FILL)
	//RAM[SCREEN+i] = -1
	@SCREEN
	D=A
	@i
	D=D+M
	A=D
	M=-1
	@i
	M=M+1
	//if(i>8191)goto LOOP
	//else goto FILL
	@8191
	D=A
	@i
	D=M-D
	@LOOP
	D;JGT
	@FILL
	0;JMP