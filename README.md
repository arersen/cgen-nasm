## cgen-nasm
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)

> ### RU
> Генератор NASM кода написаный на Python.<br>
> Готово 27 инструкций!<br>
> <br>
> > ### Пример
> > ```
> > from cgen_nasm.nasm import NASM
> > from cgen_nasm.regs import Regs as R
> >
> > nasm = NASM(org = 0x07C00)
> > nasm.add(R.AX, R.DI)
> > nasm.hlt()
> >
> > print(nasm.gen()) # или print(nasm)
> > ```

> ### EN
> NASM code generator, writen in Python.<br>
> Done 27 instructions!<br>
> <br>
> > ### Example
> > ```
> > from cgen_nasm.nasm import NASM
> > from cgen_nasm.regs import Regs as R
> >
> > nasm = NASM(org = 0x07C00)
> > nasm.add(R.AX, R.DI)
> > nasm.hlt()
> >
> > print(nasm.gen()) # Or print(nasm)
> > ```
