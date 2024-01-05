import os
import sys
import pathlib


def init_dirs():
    path_to_script = pathlib.Path(__file__).parent.resolve()
    dirs = ["src", "build"]

    try:
        for dir in dirs:
            os.mkdir(os.path.join(path_to_script, dir))
    except:
        print("Error:", sys.exc_info()[0])


def init_makefile(linker, debugging):
    file_name = "makefile"
    file_contents = "build/main: src/main.o\n"
    if linker == 1:
        if debugging:
            file_contents += "\tgcc -g -z noexecstack -no-pie -Wall -Werror -o build/main src/main.o\n"
        else:
            file_contents += (
                "\tgcc -z noexecstack -no-pie -Wall -Werror -o build/main src/main.o\n"
            )
    else:
        file_contents += "\tld -o build/main src/main.o\n"
    file_contents += "\nsrc/main.o: src/main.asm\n"
    file_contents += "\tnasm -f elf64 src/main.asm\n"

    init_file(file_name, "w", file_contents)


def init_src_file(linker, debugging):
    file_name = "src/main.asm"
    file_contents = "SECTION .data\n"
    file_contents += "\nSECTION .bss\n"
    file_contents += "\nSECTION .text\n"
    if linker == 1:
        file_contents += "\nglobal main\n"
        file_contents += "\nmain:\n"
    else:
        file_contents += "\nglobal _start\n"
        file_contents += "_start:\n"
    if debugging:
        file_contents += "\t\tmov rbp,rsp"
        file_contents += (" " * 10) + "; Store stack pointer for debugging\n"
        file_contents += "\t\tnop"
        file_contents += (" " * 18) + "; Debugging breakpoint\n"
        file_contents += "\n"
    file_contents += "\t\t; Insert commands here\n"
    file_contents += "\n"
    if debugging:
        file_contents += "\t\tnop"
        file_contents += (" " * 18) + "; Debugging endpoint\n"
    file_contents += "\t\tmov rax,60"
    file_contents += (" " * 11) + "; Exit the program\n"
    file_contents += "\t\tmov rdi,0"
    file_contents += (" " * 12) + "; Nothing to return\n"
    file_contents += "\t\tsyscall"
    file_contents += (" " * 14) + "; Call system to exit\n"

    init_file(file_name, "w", file_contents)


def init_file(file_name, mode, file_contents):
    try:
        with open(file_name, mode) as file:
            file.write(file_contents)
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
    except:
        print("Error:", sys.exc_info()[0])


def get_linker():
    print("Do you want to use gcc or ld for linking?")
    try:
        while True:
            linker = input("[gcc/ld]: ").lower()
            if linker != "gcc" and linker != "ld":
                print(linker, "is invalid, please enter gcc or ld")
            else:
                break
    except:
        print("Error: ", sys.exc_info()[0])

    return 1 if linker == "gcc" else 2


def get_debug_bool():
    print("Do you want to include debug symbols?")
    affirm = ["y", "yes"]
    deny = ["n", "no"]
    try:
        while True:
            debugging = input("[y/n]: ").lower()
            if debugging not in affirm and debugging not in deny:
                print(debugging, "is invalid, please enter y or n")
            else:
                break
    except:
        print("Error: ", sys.exc_info()[0])

    return True if debugging in affirm else False


if __name__ == "__main__":
    linker = get_linker()
    debugging = False
    if linker == 1:
        debugging = get_debug_bool()

    init_dirs()
    init_makefile(linker, debugging)
    init_src_file(linker, debugging)
