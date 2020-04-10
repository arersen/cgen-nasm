class Label:
    def __init__(self, name, nasm):
        self.name = name
        self.nasm = nasm

    def __enter__(self):
        # self.nasm.label(self.name)
        self.nasm.next()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.nasm.prev()

        if exc_val:
            raise
