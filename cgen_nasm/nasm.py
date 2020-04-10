from cgen_nasm.label import Label

class NASM:
    tab = 0
    lines = []
    def __init__(self, org = 0x07C00, tabs = False):
        self.org = org
        self.tabs = tabs

    def __str__(self):
        return self.gen()

    def next(self): # На след. уровень табирования
        self.tab += 1

    def prev(self): # На пред. уровень табирования
        self.tab -= 1

    def gen(self):
        code = ''
        code += 'org ' + hex(self.org) + '\n\n'
        for line in self.lines:
            code += ('  ' * line[0]) # Tabs
            i = 0
            for s in line[1]:
                code += s if not self.isInt(s) else hex(s)
                code += ' ' if not (i == 1 and len(line[1]) - 1 != i) else ', '
                i += 1
            code += '\n'

        return code

    def isInt(self, i):
        try:
            int(i)
            return True
        except:
            return False

    def add_line(self, line):
        self.lines.append([self.tab, line])

    def inj(self, c):
        self.add_line([c])

    # ...

    def aaa(self):
        self.add_line(['aaa'])

    def aad(self):
        self.add_line(['aad'])

    def aam(self):
        self.add_line(['aam'])

    def aas(self):
        self.add_line(['aas'])

    def adc(self, a, b):
        self.add_line(['adc', a, b if not self.isInt(b) else hex(b)])

    def add(self, a, b):
        self.add_line(['add', a, b if not self.isInt(b) else hex(b)])

    def and_(self, a, b):
        self.add_line(['and', a, b if not self.isInt(b) else hex(b)])

    def call(self, b):
        self.add_line(['call', b if not self.isInt(b) else hex(b)])

    def cbw(self, b):
        self.add_line(['cbw', b if not self.isInt(b) else hex(b)])

    def clc(self):
        self.add_line(['clc'])

    def cld(self):
        self.add_line(['cld'])

    def cli(self):
        self.add_line(['cli'])

    def cmc(self):
        self.add_line(['cmc'])

    def cmp(self, a, b):
        self.add_line(['cmp', a, b if not self.isInt(b) else hex(b)])

    def cmpsb(self):
        self.add_line(['cmpsb'])

    def cmpsw(self):
        self.add_line(['cmpsw'])

    def cwd(self):
        self.add_line(['cwd'])

    def daa(self):
        self.add_line(['daa'])

    def dac(self):
        self.add_line(['dac'])

    def dec(self, b):
        self.add_line(['dec', b if not self.isInt(b) else hex(b)])

    def div(self, b):
        self.add_line(['div', b if not self.isInt(b) else hex(b)])

    def esc(self, a, b):
        self.add_line(['esc', a, b if not self.isInt(b) else hex(b)])

    def hlt(self):
        self.add_line(['hlt'])

    def idiv(self, b):
        self.add_line(['idiv', b if not self.isInt(b) else hex(b)])

    def imul(self, b):
        self.add_line(['imul', b if not self.isInt(b) else hex(b)])

    def in_(self, a, b):
        self.add_line(['in', a, b if not self.isInt(b) else hex(b)])

    def inc(self, b):
        self.add_line(['inc', b if not self.isInt(b) else hex(b)])

    def int(self, b):
        self.add_line(['int', b if not self.isInt(b) else hex(b)])

    def into(self, b):
        self.add_line(['into', b if not self.isInt(b) else hex(b)])

    def iret(self):
        self.add_line(['iret'])

    def jcxz(self, b):
        self.add_line(['jcxz', b if not self.isInt(b) else hex(b)])

    def jmp(self, b):
        self.add_line(['jmp', b if not self.isInt(b) else hex(b)])

    def lahf(self):
        self.add_line(['lahf'])

    def lds(self, a, b):
        self.add_line(['lds', a, b if not self.isInt(b) else hex(b)])

    def lea(self, a, b):
        self.add_line(['lea', a, b if not self.isInt(b) else hex(b)])

    def les(self, a, b):
        self.add_line(['les', a, b if not self.isInt(b) else hex(b)])

    def lock(self):
        self.add_line(['lock'])

    def lodsb(self):
        self.add_line(['lodsb'])

    def lodsw(self):
        self.add_line(['lodsw'])

    def loop(self, b):
        self.add_line(['loop', b if not self.isInt(b) else hex(b)])

    def mov(self, a, b):
        self.add_line(['mov', a, b if not self.isInt(b) else hex(b)])


    def or_(self, a, b):
        self.add_line(['or', a, b if not self.isInt(b) else hex(b)])

    def xor(self, a, b):
        self.add_line(['xor', a, b if not self.isInt(b) else hex(b)])

    def test(self, a, b):
        self.add_line(['test', a, b if not self.isInt(b) else hex(b)])

    def not_(self, b):
        self.add_line(['not', b if not self.isInt(b) else hex(b)])

    def label(self, name):
        self.add_line([name + ':'])

        return Label(name, self)

    def comment(self, text):
        self.add_line([';', text])

    def int(self, i):
        self.add_line(['int', hex(i)])

    def db(self, arg):
        self.add_line([])
