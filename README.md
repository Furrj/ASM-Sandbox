# x64 Assembly Project Setup
Script for initializing a nasm assembly project. Creates a src folder with a 
boilerplate .asm file, a build file for the compiled executable, and a basic makefile for compiling the single .asm file. Uses nasm for compilation and gcc
or ld for linking. If using gcc, has option to include gdb debug symbols and extra boilerplate for easier debugging.  Works on GNU/Linux systems only.

## Dependencies
- python3
- make
- nasm
- gcc/ld

## Instructions
1. Create and move into folder
```
mkdir asm-project
cd asm-project
```
2. Move script into folder root
```
git clone https://github.com/Furrj/ASM-Sandbox.git .
(or copy and paste init.py)
```
3. Run script
```
python3 init.py
```
4. Choose which linker you would like to use
```
Do you want to use gcc or ld for linking?
[gcc/ld]:
```
5. [*Conditional*] If using gcc, choose if you want to include debug symbols
```
Do you want to include debug symbols?
[y/n]:
```
6. Remove script
```
rm init.py
```
7. Run make to compile
```
make
```
8. Run executable
```
./build/main
```
  
## Intialized Project
- asm-project/
    - makefile
    - src/
        - main.asm
    - build/

## Post-Build Project
- asm-project/
    - makefile
    - src/
        - main.asm
        - main.o
    - build/
        - main
