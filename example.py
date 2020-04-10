from cgen_nasm.nasm import NASM
from cgen_nasm.regs import Regs as R

nasm = NASM(org = 0x07C00)

nasm.inj('; custom')

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
nasm.int(0x10)
nasm.into(0x10)
nasm.iret()
nasm.jcxz('l2')
nasm.jmp(0x200)
nasm.lahf()
nasm.lds(R.AX, '[1]')
nasm.lea(R.EAX, '[ebx+8]')
nasm.les(R.EAX, '[ebx+16]')
nasm.lock()
nasm.lodsb()
nasm.lodsw()

# nasm.or_(R.AX, R.DI)
# nasm.xor(R.AX, R.DI)
# nasm.test(R.AX, R.DI)
# nasm.not_(R.AX)

with nasm.label('end') as label: # Label пример
    nasm.comment('comment')
    nasm.loop('end')

nasm.mov(R.AX, R.DI)

print(nasm) # Получить код
