from cgen_nasm.nasm import NASM
from cgen_nasm.regs import Regs as R

nasm = NASM(org = 0x07C00)

nasm.aaa()
nasm.aad()
nasm.aam()
nasm.aas()
nasm.adc(R.AX, 0x00)
nasm.add(R.AX, R.DI)
nasm.and_(R.AX, R.DI)
nasm.call(0x200)
nasm.cbw(R.AX)
nasm.clc()
nasm.cld()
nasm.cli()
nasm.cmc()
nasm.cmp(R.AX, R.DI)
nasm.cmpsb()
nasm.cmpsw()
nasm.cwd()
nasm.daa()
nasm.dac()
nasm.dec(R.AX)
nasm.div(R.AX)
nasm.esc(R.AX, R.DI)
nasm.hlt()
nasm.idiv(R.AX)
nasm.imul(R.AX)
nasm.in_(R.AX, 0xff20)

# nasm.or_(R.AX, R.DI)
# nasm.xor(R.AX, R.DI)
# nasm.test(R.AX, R.DI)
# nasm.not_(R.AX)

with nasm.label('end') as label: # Label пример
    nasm.comment('comment')

print(nasm) # Получить код
