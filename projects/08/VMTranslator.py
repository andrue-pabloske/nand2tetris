import os
import sys

#parser
class Parser:
    def __init__(self, file_name):
        self.index = 0
        self.file = open('%s'%file_name, 'r')
        self.lines = []
        for line in self.file:
            line = line.strip()
            if line != '' and line[0] + line[1] != '//':
                self.lines.append(line)
        self.current_instruction = self.lines[0]

    def has_more_commands(self):
        if self.index == len(self.lines) - 1:
            return False
        return True

    def advance(self):
        self.index += 1
        self.current_instruction = self.lines[self.index]
        if self.current_instruction.find('//') != -1:
            self.current_instruction = self.current_instruction[:self.current_instruction.find('//')].strip()

    #C_arithmetic = 0, C_PUSH = 1, C_POP = 2, C_LABEL = 3, C_GOTO = 4
    #C_IF = 5, C_FUNCTION = 6, C_CALL = 7, C_RETURN = 8
    def command_type(self):
        if self.current_instruction.find(' ') != -1:
            command = self.current_instruction[:self.current_instruction.find(' ')]
        else:
            command = self.current_instruction
            
        if command in ['add', 'sub', 'neg', 'eq',
                               'gt', 'lt', 'and', 'or', 'not']:
            return 0
        elif command == 'push':
            return 1
        elif command == 'pop':
            return 2
        elif command == 'label':
            return 3
        elif command == 'goto':
            return 4
        elif command == 'if-goto':
            return 5
        elif command == 'function':
            return 6
        elif command == 'call':
            return 7
        elif command == 'return':
            return 8
    
    def arithmetic_command(self):
        return self.current_instruction
    
    def arg1(self):
        argument = self.current_instruction[self.current_instruction.find(' ') + 1:]
        argument = argument[:argument.find(' ')]
        return argument

    def arg2(self):
        argument = self.current_instruction[self.current_instruction.find(' ') + 1:]
        argument = argument[argument.find(' ') + 1:]
        return argument

#code writer
class CodeWriter:
    def __init__(self, file_name):
        self.asm = open('{}/{}.asm'.format(file_name, file_name), 'w')
        self.function_name = ''
        self.boolean_count = 0
        self.function_count = 0
        self.addresses = {
            'local': 'LCL', # Base R1
            'argument': 'ARG', # Base R2
            'this': 'THIS', # Base R3
            'that': 'THAT', # Base R4
            'pointer': 3, # Edit R3, R4
            'temp': 5, # Edit R5-12
            # R13-15 are free
            'static': 16, # Edit R16-255
        }

    def write_bootstrap(self):
        self.write('//bootstrap code')
        self.write('//SP = 256')
        self.write('@256')
        self.write('D=A')
        self.write('@SP')
        self.write('M=D')
        self.write('')
        self.write_call('Sys.init', 0)
        
    #######
    ### API
    def set_file_name(self, file_name):
        self.file_name = os.path.splitext(file_name)[0]
        self.file_name = self.file_name[self.file_name.find('/')+1:]

    def write_arithmetic(self, command):
        count = self.boolean_count
        
        self.write('//%s'%command)
        if command in ['neg', 'not']:
            self.pop_stack_to_D()
            self.write('@R14')
            self.write('M=D')
        else:
            self.pop_stack_to_D()
            self.write('@R15')
            self.write('M=D')
            self.pop_stack_to_D()
            self.write('@R14')
            self.write('M=D')

        #store the result of the desired operation in D
        if command in ['neg', 'not']:
            self.write('@14')
        elif command in ['add', 'sub', 'and', 'or']:
            self.write('@15')
            self.write('D=M')
            self.write('@14')

        if command == 'add':
            self.write('D=D+M')
        elif command == 'sub':
            self.write('D=M-D')
        elif command == 'neg':
            self.write('D=-M')
        elif command == 'and':
            self.write('D=M&D')
        elif command == 'or':
            self.write('D=M|D')
        elif command == 'not':
            self.write('D=!M')
        else:
            self.write('@logical.%d'%count)
            self.write('0;JMP')
            self.write('(logical$TRUE.%d)'%count)
            self.write('D=-1')
            self.write('@logical$ret.%d'%count)
            self.write('0;JMP')
            self.write('(logical$FALSE.%d)'%count)
            self.write('D=0')
            self.write('@logical$ret.%d'%count)
            self.write('0;JMP')
            #execute jump based on RAM[14]-RAM[15]
            self.write('(logical.%d)'%count)
            self.write('@15')
            self.write('D=M')
            self.write('@14')
            self.write('D=M-D')
            self.write('@logical$TRUE.%d'%count)
            if command == 'eq':
                self.write('D;JEQ')
            elif command == 'gt':
                self.write('D;JGT')
            else:
                self.write('D;JLT')
            self.write('@logical$FALSE.%d'%count)
            self.write('0;JMP')
            self.write('(logical$ret.%d)'%count)
            self.boolean_count += 1

        self.push_D_to_stack()
        self.write('')

    def write_push_pop(self, command, segment, index):
        if command == 1:
            self.write('//push {} {}'.format(segment, index))
            self.resolve_address(segment, index)
            if segment == 'constant':
                self.write('D=A')
            else:
                self.write('D=M')
            self.push_D_to_stack()
        else:
            self.write('//pop {} {}'.format(segment, index))
            self.resolve_address(segment, index)
            self.write('D=A')
            self.write('@R13')
            self.write('M=D')
            self.pop_stack_to_D()
            self.write('@R13')
            self.write('A=M')
            self.write('M=D')
            
        self.write('')

    def write_label(self, label):
        self.write('//label {}'.format(label))
        self.write('({}${})'.format(self.function_name, label))
        self.write('')

    def write_goto(self, label):
        self.write('//goto {}'.format(label))
        self.write('@{}${}'.format(self.function_name, label))
        self.write('0;JMP')
        self.write('')

    def write_ifgoto(self, label):
        self.write('//if-goto {}'.format(label))
        self.pop_stack_to_D()
        self.write('@{}${}'.format(self.function_name, label))
        self.write('D;JNE')
        self.write('')

    def write_function(self, function_name, nvars):
        self.write('//function {} {}'.format(function_name, nvars))
        #(f)
        self.write('({})'.format(function_name))
        #push constant 0 (nvars times)
        for i in range(int(nvars)):
            self.write('D=0')
            self.push_D_to_stack()
        self.write('')
        self.function_name = function_name
        
    def write_call(self, function_name, nargs):
        count = self.function_count
        self.function_count += 1
        
        self.write('//call {} {}'.format(function_name, nargs))
        #push retAddr
        self.write('@{}$ret.{}'.format(function_name, count))
        self.write('D=A')
        self.push_D_to_stack()
        
        #push LCL
        #push ARG
        #push THIS
        #push THAT
        for address in ['LCL', 'ARG', 'THIS', 'THAT']:
            self.write('@%s'%address)
            self.write('D=M')
            self.push_D_to_stack()
            
        #LCL = SP
        self.write('@SP')
        self.write('D=M')
        self.write('@LCL')
        self.write('M=D')
        
        #ARG = SP-nArgs-5
        self.write('@{}'.format(int(nargs)+5))
        self.write('D=D-A')
        self.write('@ARG')
        self.write('M=D')
        
        #goto function_name
        self.write('@{}'.format(function_name))
        self.write('0;JMP')
        
        #(returnAddress)
        self.write('({}$ret.{})'.format(function_name, count))
        self.write('')
        
    def write_return(self):
        FRAME = 'R14'
        RET = 'R15'
        
        self.write('//return')
        #frame = LCL
        self.write('@LCL')
        self.write('D=M')
        self.write('@' + FRAME)
        self.write('M=D')
        
        #retAddr = *(frame - 5)
        self.write('@5')
        self.write('A=D-A')
        self.write('D=M')
        self.write('@' + RET)
        self.write('M=D')
        
        #*ARG = pop()
        self.pop_stack_to_D()
        self.write('@ARG')
        self.write('A=M')
        self.write('M=D')
        
        #SP = ARG + 1
        self.write('@ARG')
        self.write('D=M+1')
        self.write('@SP')
        self.write('M=D')

        #THAT = *(frame - 1)
        #THIS = *(frame - 2)
        #ARG = *(frame - 3)
        #LCL = *(frame - 4)
        offset = 1
        for addr in ['THAT', 'THIS', 'ARG', 'LCL']:
            self.write('@' + FRAME)
            self.write('D=M')
            self.write('@' + str(offset))
            self.write('A=D-A')
            self.write('D=M')
            self.write('@' + addr)
            self.write('M=D')
            offset += 1
        
        #goto retAddr
        self.write('@' + RET)
        self.write('A=M')
        self.write('0;JMP')
        self.write('')
    
    def close(self):
        self.asm.close()
    ### END API
    #######

    ### helper methods
    def write(self, code):
        self.asm.write(code + '\n')

    def push_D_to_stack(self):
        self.write('@SP')
        self.write('AM=M+1')
        self.write('A=A-1')
        self.write('M=D')

    def pop_stack_to_D(self):
        self.write('@SP')
        self.write('AM=M-1')
        self.write('D=M')

    def resolve_address(self, segment, index):
        addr = self.addresses.get(segment)
        if segment == 'constant':
            self.write('@{}'.format(index))
        elif segment == 'static':
            self.write('@' + self.file_name + '.' + index + '')
        elif segment in ['pointer', 'temp']:
            self.write('@R' + str(addr + int(index)) + '')
        else:
            self.write('@' + addr)
            self.write('D=M')
            self.write('@{}'.format(index))
            self.write('A=D+A')

#helper methods
def translate(file_name, writer):
    parser = Parser(file_name)
    writer.set_file_name(file_name)
    
    while True:
        if parser.command_type() == 0:
            writer.write_arithmetic(parser.arithmetic_command())
        elif parser.command_type() == 1 or parser.command_type() == 2:
            writer.write_push_pop(parser.command_type(), parser.arg1(), parser.arg2())
        elif parser.command_type() == 3:
            writer.write_label(parser.arg1())
        elif parser.command_type() == 4:
            writer.write_goto(parser.arg1())
        elif parser.command_type() == 5:
            writer.write_ifgoto(parser.arg1())
        elif parser.command_type() == 6:
            writer.write_function(parser.arg1(), parser.arg2())
        elif parser.command_type() == 7:
            writer.write_call(parser.arg1(), parser.arg2())
        elif parser.command_type() == 8:
            writer.write_return()
            
        if parser.has_more_commands():
            parser.advance()
        else:
            break


#main driver
file_name = sys.argv[1]
writer = CodeWriter(file_name)
if os.path.isfile(file_name):
    translate(file_name, writer)
    writer.close()
elif os.path.isdir(file_name):
    writer.write_bootstrap()
    for file in os.listdir(file_name):
        if os.path.splitext(file)[1] == '.vm':
            file = '%s/'%file_name + file
            translate(file, writer)
    writer.close()
