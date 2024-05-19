#!/bin/bash

if [ -d "build" ]; then
    rm -rf ./build
    mkdir ./build
else
    mkdir ./build
fi

nasm -f elf32 $(src/operation).asm -o $(build/operation).o -g
#elf32
gcc -o build/result build/operation.o src/main.c -m32 -g
#-m32

