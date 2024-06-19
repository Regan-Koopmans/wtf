package main

import (
	"fmt"
	"os"
)

func get_source_code(filename string) string {
	dat, _ := os.ReadFile(filename)
	return string(dat)
}

func run(source string) {
	var cells []int = make([]int, 3000)
	head_pointer := 0
	instruction_pointer := 0
	for instruction_pointer < len(source) {
		switch instruction := source[instruction_pointer]; instruction {
		case '>':
			head_pointer += 1
		case '<':
			head_pointer -= 1
		case '+':
			cells[head_pointer] += 1
		case '-':
			cells[head_pointer] -= 1
		case '.':
			fmt.Print(string(cells[head_pointer]))
		case ',':
			var b []byte = make([]byte, 1)
			os.Stdin.Read(b)
			cells[head_pointer] = int(b[0])
		case '[':
			if cells[head_pointer] == 0 {
				braces := 1
				for braces > 0 {
					instruction_pointer += 1
					if source[instruction_pointer] == ']' {
						braces -= 1
					}
					if source[instruction_pointer] == '[' {
						braces += 1
					}
				}
				instruction_pointer += 1
			}
		case ']':
			if cells[head_pointer] != 0 {
				braces := 1
				for braces > 0 {
					instruction_pointer -= 1
					if source[instruction_pointer] == ']' {
						braces += 1
					}
					if source[instruction_pointer] == '[' {
						braces -= 1
					}
				}
				instruction_pointer -= 1
			}

		}
		instruction_pointer += 1
	}
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Please supply program")
		return
	}

	source_code := get_source_code(os.Args[1])
	run(source_code)
}
