import numpy as np
import sys, tty


source_code = ""

# The instruction pointer is how we keep track
# of which opcode we are executing in the 
# source code
instruction_pointer = 0 

# The head pointer tells us at which cell on
# tape we are operating
head_pointer = 0

cells = np.zeros(30000, dtype=np.uint8)

def move_head_pointer_right():
    global head_pointer
    head_pointer += 1
    
def move_head_pointer_left():
    global head_pointer
    head_pointer -= 1

def increment_current_cell():
    cells[head_pointer] += 1
    
def decrement_current_cell():
    cells[head_pointer] -= 1
    
def output_current_cell():
    print(chr(cells[head_pointer]), end='')
    
def replace_with_input():
    character = sys.stdin.read(1)
    cells[head_pointer] = ord(character)
 
def jump_if_zero():
    global instruction_pointer
    if cells[head_pointer] != 0:
        return
    
    braces = 1
    while braces > 0:
        instruction_pointer += 1
        if source_code[instruction_pointer] == ']':
            braces -= 1
        if source_code[instruction_pointer] == '[':
            braces += 1
    instruction_pointer += 1
    
    
def jump_not_zero():
    global instruction_pointer
    if cells[head_pointer] == 0:
        return
    
    braces = 1
    while braces > 0:
        instruction_pointer -= 1
        if source_code[instruction_pointer] == ']':
            braces += 1
        if source_code[instruction_pointer] == '[':
            braces -= 1
    instruction_pointer -= 1
            
instructions = {
    '>': move_head_pointer_right,
    '<': move_head_pointer_left,
    '+': increment_current_cell,
    '-': decrement_current_cell,
    '.': output_current_cell,
    ',': replace_with_input,
    '[': jump_if_zero,
    ']': jump_not_zero
}


def get_source_code(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read().replace('\n', '')


def run(source: str):
    global instruction_pointer
    global source_code
    source_code = source

    while instruction_pointer < len(source_code):
        if source_code[instruction_pointer] in instructions:
            instructions[source_code[instruction_pointer]]()
        instruction_pointer += 1


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Please supply program")
        sys.exit()
        
    source_code = get_source_code(sys.argv[1])
    run(source_code)