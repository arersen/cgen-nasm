## cgen-nasm
 Генератор NASM кода написаный на Python.<br>
 Готово 48 инструкции!<br>
 <br>

> ### Установка
> * Клонировать репозиторий
> * Распаковать папку cgen_nasm в папку с вашим проектом
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
