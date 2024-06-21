#include <iostream>
#include <fstream>
#include <vector>
#include <string>

std::string get_source_code(const std::string& filename) {
    std::ifstream file(filename);
    std::string content((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
    return content;
}

void run(const std::string& source) {
    std::vector<int> cells(3000, 0);
    int head_pointer = 0;
    int instruction_pointer = 0;
    while (instruction_pointer < source.length()) {
        switch (source[instruction_pointer]) {
        case '>':
            head_pointer++;
            break;
        case '<':
            head_pointer--;
            break;
        case '+':
            cells[head_pointer]++;
            break;
        case '-':
            cells[head_pointer]--;
            break;
        case '.':
            std::cout << static_cast<char>(cells[head_pointer]);
            break;
        case ',':
            char c;
            std::cin >> c;
            cells[head_pointer] = static_cast<int>(c);
            break;
        case '[':
            if (cells[head_pointer] == 0) {
                int braces = 1;
                while (braces > 0) {
                    instruction_pointer++;
                    if (source[instruction_pointer] == ']') {
                        braces--;
                    } else if (source[instruction_pointer] == '[') {
                        braces++;
                    }
                }
            }
            break;
        case ']':
            if (cells[head_pointer] != 0) {
                int braces = 1;
                while (braces > 0) {
                    instruction_pointer--;
                    if (source[instruction_pointer] == ']') {
                        braces++;
                    } else if (source[instruction_pointer] == '[') {
                        braces--;
                    }
                }
                instruction_pointer--;
            }
            break;
        }
        instruction_pointer++;
    }
}

void compile(const std::string& source) {
    std::ofstream file("destination.cpp");
    file << "#include <iostream>\n"
         << "int main() {\n"
         << "    // Your compiled C++ code goes here\n"
         << "    return 0;\n"
         << "}\n";
}

int main(int argc, char* argv[]) {
    if (argc < 3) {
        std::cout << "Please supply program" << std::endl;
        return 1;
    }

    std::string source_code = get_source_code(argv[2]);
    if (argv[1] == std::string("run")) {
        run(source_code);
    } else if (argv[1] == std::string("compile")) {
        compile(source_code);
    } else {
        std::cout << "Unrecognised command '" << argv[1] << "'. Supported commands: compile, run" << std::endl;
    }

    return 0;
}

