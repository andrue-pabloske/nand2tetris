import os
import sys

class Parser:
    def __init__(self, file_name):
        self.index = 0
        self.line_number = 0
        self.file = open('%s.asm' % file_name, 'r')
        self.lines = []
        for line in self.file:
            line = line.strip()
            if line != '' and line[0] + line[1] != '//':
                self.lines.append(line)
        self.current_instruction = self.lines[0]

    def has_more_lines(self):
        if self.index == len(self.lines) - 1:
            return False
        return True

    def advance(self):
        self.index += 1
        self.current_instruction = self.lines[self.index]
        if self.current_instruction.find('//') != -1:
            self.current_instruction = self.current_instruction[:self.current_instruction.find('//')].strip()
        if self.instruction_type() == 0 or self.instruction_type() == 1:
          self.line_number += 1

    def instruction_type(self):
        if self.current_instruction[0] == '@':
            return 0
        elif self.current_instruction[0] == '(':
            return 2
        else:
            return 1

    def symbol(self):
        if self.instruction_type() == 0:
            return self.current_instruction[1:]
        else:
            return self.current_instruction[1:len(self.current_instruction) - 1]

    def dest(self):
        if self.current_instruction.find('=') != -1:
            return self.current_instruction[:self.current_instruction.find('=')]
        else:
            return ''

    def comp(self):
        start = 0
        end = len(self.current_instruction)
        if self.current_instruction.find('=') != -1:
            start = self.current_instruction.find('=') + 1
        if self.current_instruction.find(';') != -1:
            end = self.current_instruction.find(';')
        return self.current_instruction[start:end]

    def jump(self):
        if self.current_instruction.find(';') != -1:
            return self.current_instruction[self.current_instruction.find(';') + 1:]
        else:
            return ''


class Translator:
    def dest(self, input):
        code = list('000')
        if 'A' in input:
            code[0] = '1'
        if 'D' in input:
            code [1] = '1'
        if 'M' in input:
            code[2] = '1'
        return ''.join(code)

    def comp(self, input):
        if input == '0':
            return '0101010'
        elif input == '1':
            return '0111111'
        elif input == '-1':
            return '0111010'
        elif input == 'D':
            return '0001100'
        elif input == 'A':
            return '0110000'
        elif input == 'M':
            return '1110000'
        elif input == '!D':
            return '0001101'
        elif input == '!A':
            return '0110001'
        elif input == '!M':
            return '1110001'
        elif input == '-D':
            return '0001111'
        elif input == '-A':
            return '0110011'
        elif input == '-M':
            return '1110011'
        elif input == 'D+1':
            return '0011111'
        elif input == 'A+1':
            return '0110111'
        elif input == 'M+1':
            return '1110111'
        elif input == 'D-1':
            return '0001110'
        elif input == 'A-1':
            return '0110010'
        elif input == 'M-1':
            return '1110010'
        elif input == 'D+A':
            return '0000010'
        elif input == 'D+M':
            return '1000010'
        elif input == 'D-A':
            return '0010011'
        elif input == 'D-M':
            return '1010011'
        elif input == 'A-D':
            return '0000111'
        elif input == 'M-D':
            return '1000111'
        elif input == 'D&A':
            return '0000000'
        elif input == 'D&M':
            return '1000000'
        elif input == 'D|A':
            return '0010101'
        else:
            return '1010101'

    def jump(self, input):
        if input == '':
            return '000'
        elif input == 'JGT':
            return '001'
        elif input == 'JEQ':
            return '010'
        elif input == 'JGE':
            return '011'
        elif input == 'JLT':
            return '100'
        elif input == 'JNE':
            return '101'
        elif input == 'JLE':
            return '110'
        else:
            return '111'


class SymbolTable:
    def __init__(self):
        self.table = {}

    def add_entry(self, symbol, address):
        self.table.update({symbol: address})

    def contains(self, symbol):
        return symbol in self.table

    def get_address(self, symbol):
        return self.table[symbol]

#convert symbol to A-instruction
number_of_vars = 0
def symbol_to_instruction(symbol):
  global number_of_vars
  if symbol.isdigit():
    value = symbol
  elif my_symbol_table.contains(symbol):
    value = my_symbol_table.get_address(symbol)
  else:
    my_symbol_table.add_entry(symbol, 16 + number_of_vars)
    number_of_vars += 1
    value = my_symbol_table.get_address(symbol)
  
  binary = decimal_to_binary(value)
  padding = ''
  for i in range(16 - len(binary)):
      padding += '0'
  return padding + binary

def decimal_to_binary(n):
    return '{0:b}'.format(int(n))

#main driver
file_name = sys.argv[1]
first_parser = Parser(file_name)
my_translator = Translator()
my_symbol_table = SymbolTable()

#initialize the symbol table
for i in range(16):
    my_symbol_table.add_entry('R{}'.format(i), i)
my_symbol_table.add_entry('SP', 0)
my_symbol_table.add_entry('LCL', 1)
my_symbol_table.add_entry('ARG', 2)
my_symbol_table.add_entry('THIS', 3)
my_symbol_table.add_entry('THAT', 4)
my_symbol_table.add_entry('SCREEN', 16384)
my_symbol_table.add_entry('KBD', 24576)

#first pass - add labels to table
while first_parser.has_more_lines():
  if first_parser.instruction_type() == 2:
    my_symbol_table.add_entry(first_parser.symbol(), first_parser.line_number + 1)
  first_parser.advance()

#second pass
second_parser = Parser(file_name)
code = ''
while second_parser.has_more_lines():
    if second_parser.instruction_type() == 1:
        code += '111' + my_translator.comp(second_parser.comp()) + my_translator.dest(second_parser.dest()) + my_translator.jump(second_parser.jump()) + '\n'
    elif second_parser.instruction_type() == 0:
        code += symbol_to_instruction(second_parser.symbol()) + '\n'
    if second_parser.has_more_lines():
        second_parser.advance()
    else:
        break

f = open('%s.hack' % file_name, 'w')
f.write(code)
f.close()
