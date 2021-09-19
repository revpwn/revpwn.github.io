#!/usr/bin/env python3
instructions = {
    "INC A":      1,
    "INC A_HI":   2,
    "BUF [M]":    3,
    "PRINT":      4,
    "MOV A, [M]": 5,
    "MOV [M], A": 6,
    "MOV M, A":   7,
    "EXIT":       8,
}

class Opcode:
    def __init__(self, ins, val=0):
        self.op = (instructions[ins] << 5) | (val & 0x1f)
        assert(self.op == self.op & 0xff)

opcodes = []

# Get to A=0xe080
for i in range(0x80//16):
    opcodes.append(Opcode("INC A", 16))
for i in range(0xe0//16):
    opcodes.append(Opcode("INC A_HI", 16))

for i in range(40):
    opcodes.append(Opcode("MOV M, A"))
    opcodes.append(Opcode("BUF [M]"))
    opcodes.append(Opcode("INC A", 1))

opcodes.append(Opcode("PRINT"))

with open("out.txt", "wb") as f:
    f.write(bytes([o.op for o in opcodes]))

# nc chal.2021.sunshinectf.org 21101 < out.txt
# sun{We_hire_RIIverse_engineers}
