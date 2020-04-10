## cgen-nasm

> ### RU
> Генератор NASM кода написаный на Python.<br>
> <br>
> > ### Пример
```
> > from cgen_nasm.nasm import NASM
> > from cgen_nasm.regs import Regs as R
> >
> > nasm = NASM(org = 0x07C00)
> > nasm.add(R.AX, R.DI)
> > nasm.hlt()
> >
> > print(nasm.gen()) # или print(nasm)
```

> ### EN
> Generator NASM code, writen in Python.<br>
> <br>
> > ### Example
```
> > from cgen_nasm.nasm import NASM
> > from cgen_nasm.regs import Regs as R
> >
> > nasm = NASM(org = 0x07C00)
> > nasm.add(R.AX, R.DI)
> > nasm.hlt()
> >
> > print(nasm.gen()) # Or print(nasm)
```

