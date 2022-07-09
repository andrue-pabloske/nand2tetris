import os
import sys

#helper methods
def push_segment(segment, index):
    code = ""
    #D=segment[index]
    code += "@%s\n" %index
    code += "D=A\n"
    code += "@%s\n" %segment
    code += "A=M\n"
    code += "A=A+D\n"
    code += "D=M\n"
    #SP++
    code += "@SP\n"
    code += "AM=M+1\n"
    #RAM[--SP]=D
    code += "A=A-1\n"
    code += "M=D\n"
    return code

def push_fixed_segment(addr, index):
    code = ""
    #D=segment[index]
    code += "@%s\n" %index
    code += "D=A\n"
    code += "@%s\n" %addr
    code += "A=A+D\n"
    code += "D=M\n"
    #SP++
    code += "@SP\n"
    code += "AM=M+1\n"
    #RAM[--SP]=D
    code += "A=A-1\n"
    code += "M=D\n"
    return code

def push_const(value):
    code = ""
    #D=value
    code += "@%s\n" %value
    code += "D=A\n"
    #SP++
    code += "@SP\n"
    code += "AM=M+1\n"
    #RAM[--SP]=D
    code += "A=A-1\n"
    code += "M=D\n"
    return code

def pop_segment(segment, index):
    code = ""
    #RAM[13] = segmentBase + index
    code += "@%s\n" %segment
    code += "D=M\n"
    code += "@%s\n" %index
    code += "D=D+A\n"
    code += "@R13\n"
    code += "M=D\n"
    #SP--
    code += "@SP\n"
    code += "AM=M-1\n"
    #D=RAM[SP]
    code += "D=M\n"
    #RAM[segmentBase + index]=D
    code += "@R13\n"
    code += "A=M\n"
    code += "M=D\n"
    return code

def pop_fixed_segment(addr, index):
    code = ""
    #RAM[13] = addr + index
    code += "@%s\n" %addr
    code += "D=A\n"
    code += "@%s\n" %index
    code += "D=D+A\n"
    code += "@R13\n"
    code += "M=D\n"
    #SP--
    code += "@SP\n"
    code += "AM=M-1\n"
    #D=RAM[SP]
    code += "D=M\n"
    #RAM[addr + index]=D
    code += "@R13\n"
    code += "A=M\n"
    code += "M=D\n"
    return code

def pop_register(register):
    code = ""
    #RAM[13] = register
    code += "@%s\n"%register
    code += "D=A\n"
    code += "@R13\n"
    code += "M=D\n"
    #SP--
    code += "@SP\n"
    code += "AM=M-1\n"
    #D=RAM[SP]
    code += "D=M\n"
    #RAM[register]=D
    code += "@R13\n"
    code += "A=M\n"
    code += "M=D\n"
    return code

#parser
class Parser:
    def __init__(self, file_name):
        self.index = 0
        self.file = open("%s.vm" %file_name, "r")
        self.lines = []
        for line in self.file:
            line = line.strip()
            if line != "" and line[0] + line[1] != "//":
                self.lines.append(line)
        self.current_instruction = self.lines[0]

    def has_more_commands(self):
        if self.index == len(self.lines) - 1:
            return False
        return True

    def advance(self):
        self.index += 1
        self.current_instruction = self.lines[self.index]
        if self.current_instruction.find("//") != -1:
            self.current_instruction = self.current_instruction[:self.current_instruction.find("//")].strip()

    #C_ARITHMETIC = 0, C_PUSH = 1, C_POP = 2, C_LABEL = 3, C_GOTO = 4
    #C_IF = 5, C_FUNCTION = 6, C_RETURN = 7, C_CALL = 8
    def command_type(self):
        if self.current_instruction.find(" ") != -1:
            command = self.current_instruction[:self.current_instruction.find(" ")]
        else:
            command = self.current_instruction
        arithmetic_commands = ["add", "sub", "neg", "eq",
                               "gt", "lt", "and", "or", "not"]
        for comm in arithmetic_commands:
            if command == comm:
                return 0
        if command == "push":
            return 1
        elif command == "pop":
            return 2
        elif command == "label":
            return 3
        elif command == "goto":
            return 4
        elif command == "if-goto":
            return 5
        elif command == "function":
            return 6
        elif command == "return":
            return 7
        elif command == "call":
            return 8
    
    def arithmetic_command(self):
        return self.current_instruction
    
    def arg1(self):
        argument = self.current_instruction[self.current_instruction.find(" ") + 1:]
        argument = argument[:argument.find(" ")]
        return argument

    def arg2(self):
        argument = self.current_instruction[self.current_instruction.find(" ") + 1:]
        argument = argument[argument.find(" ") + 1:]
        return argument

#code writer
class CodeWriter:
    def __init__(self, file_name):
        self.f = open("%s.asm" %file_name, "w")
        self.count = 0

    def write_arithmetic(self, command):
        code = ""
        code += "//%s\n" %command
        if command != "neg" and command != "not":
            #pop top 2 elements to RAM[14] and RAM[15]
            code += pop_register(15)
            code += pop_register(14)
        else:
            code += pop_register(14)

        #store the result of the desired operation in D
        if command == "add":
            code += "@15\n"
            code += "D=M\n"
            code += "@14\n"
            code += "D=D+M\n"
        elif command == "sub":
            code += "@15\n"
            code += "D=M\n"
            code += "@14\n"
            code += "D=M-D\n"
        elif command == "neg":
            code += "@14\n"
            code += "D=-M\n"
        elif command == "and":
            code += "@15\n"
            code += "D=M\n"
            code += "@14\n"
            code += "D=M&D\n"
        elif command == "or":
            code += "@15\n"
            code += "D=M\n"
            code += "@14\n"
            code += "D=M|D\n"
        elif command == "not":
            code += "@14\n"
            code += "D=!M\n"
        else:
            code += "@ARITHMETIC_%d\n"%self.count
            code += "0;JMP\n"
            code += "(ARITHMETIC_TRUE_%d)\n"%self.count
            code += "D=-1\n"
            code += "@ARITHMETIC_RETURN_%d\n"%self.count
            code += "0;JMP\n"
            code += "(ARITHMETIC_FALSE_%d)\n"%self.count
            code += "D=0\n"
            code += "@ARITHMETIC_RETURN_%d\n"%self.count
            code += "0;JMP\n"
            #execute jump based on RAM[14]-RAM[15]
            code += "(ARITHMETIC_%d)\n"%self.count
            code += "@15\n"
            code += "D=M\n"
            code += "@14\n"
            code += "D=M-D\n"
            code += "@ARITHMETIC_TRUE_%d\n"%self.count
            if command == "eq":
                code += "D;JEQ\n"
            elif command == "gt":
                code += "D;JGT\n"
            else:
                code += "D;JLT\n"
            code += "@ARITHMETIC_FALSE_%d\n"%self.count
            code += "0;JMP\n"
            code += "(ARITHMETIC_RETURN_%d)\n"%self.count
            self.count += 1

        #push the value stored in D onto the stack
        #SP++
        code += "@SP\n"
        code += "AM=M+1\n"
        #RAM[--SP]=D
        code += "A=A-1\n"
        code += "M=D\n"
        
        self.f.write(code)

    def write_push_pop(self, command, segment, index):
        code = ""
        addr = ""
        if segment == "local":
            addr = "LCL"
        elif segment == "argument":
            addr = "ARG"
        elif segment == "this":
            addr = "THIS"
        elif segment == "that":
            addr = "THAT"
        elif segment == "temp":
            addr = "5"
        elif segment == "pointer":
            addr = "3"
        elif segment == "static":
            addr = "16"
        
        if segment == "constant":
            code += "//push {} {}\n".format(segment, index)
            code += push_const(index)
        elif segment == "temp" or segment == "pointer" or segment == "static":
            if command == 1:
                code += "//push {} {}\n".format(segment, index)
                code += push_fixed_segment(addr, index)
            else:
                code += "//pop {} {}\n".format(segment, index)
                code += pop_fixed_segment(addr, index)
        elif command == 1:
            code += "//push {} {}\n".format(segment, index)
            code += push_segment(addr, index)
        else:
            code += "//pop {} {}\n".format(segment, index)
            code += pop_segment(addr, index)
        self.f.write(code)
    
    def close(self):
        self.f.close()

#main driver
file_name = sys.argv[1]
parser = Parser(file_name)
writer = CodeWriter(file_name)

while True:
    if parser.command_type() == 0:
        writer.write_arithmetic(parser.arithmetic_command())
    elif parser.command_type() == 1 or parser.command_type() == 2:
        writer.write_push_pop(parser.command_type(), parser.arg1(), parser.arg2())

    if parser.has_more_commands():
        parser.advance()
    else:
        break
    
writer.close()
