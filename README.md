## cgen-nasm
 Генератор NASM кода написаный на Python.<br>
 Готово 32 инструкций!<br>
 <br>

> ### Установка
> ```python
> apt install git
> pip install git+https://github.com/qbaddev/cgen-nasm.git
> ```
<br>

> ### Пример
> ```
> from cgen_nasm.nasm import NASM
> from cgen_nasm.regs import Regs as R
>
> nasm = NASM(org = 0x07C00)
> nasm.add(R.AX, R.DI)
> nasm.hlt()
>
> print(nasm.gen()) # или print(nasm)
> ```
