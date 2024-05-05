#!/bin/bash

if [ -d "./lib" ]; then
    rm -rf ./lib
    mkdir ./lib
else
    mkdir ./lib
fi

if [ -d "./build" ]; then
    rm -rf ./build
    mkdir ./build
else
    mkdir ./build
fi

echo "Compilando la librería dinámica en C..."
#-elf32
nasm -f elf64 src/operation.asm -o build/operation.o
gcc -shared -W -o lib/libaddToGINI.so src/sum_GINI.c build/operation.o -m64
#-m32

echo "Compilacion exitosa, librería compilada y guardada en ./lib..."
