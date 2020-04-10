## cgen-nasm

> ### RU
> Генератор NASM кода написаный на Python.<br>
> <br>
> > ### Пример использования
> > ```
> > from cgen_nasm.nasm import NASM<br>
> > from cgen_nasm.regs import Regs as R<br>
> > <br>
> > nasm = NASM(org = 0x07C00) <br>
> > nasm.add(R.AX, R.DI) <br>
> > nasm.hlt() <br>
> > <br>
> > print(nasm.gen()) # Можно использовать как print(nasm) <br>
> > ``` <br>

