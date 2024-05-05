section .data
    num dd 0

global asm_operation
section .text

asm_operation:
    push ebp
    mov ebp, esp
    fld dword [esp + 8]
    fistp dword[num]
    mov eax, [num]
    add eax, 1
    mov [num], eax
    mov esp, ebp
    pop ebp
    ret