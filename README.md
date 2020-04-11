## cgen-nasm
 Генератор NASM кода написаный на Python.<br>
 Готово 48 инструкции!<br>
 <br>

> ### Установка
> ```bash
> apt install git
> pip install git+https://github.com/qbaddev/cgen-nasm.git
> ```
<br>

> ### Пример
> ```python
> from cgen_nasm.nasm import NASM
> from cgen_nasm.regs import Regs as R
>
> nasm = NASM(org = 0x07C00)
> nasm.add(R.AX, R.DI)
> nasm.hlt()
>
> print(nasm.gen()) # или print(nasm)
> ```
