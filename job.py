class Job:
    def __init__(self, real_start, real_stop, real_parts,
                 imag_start, imag_stop, imag_parts):
        self.real_start = real_start
        self.real_stop = real_stop
        self.real_parts = real_parts

        self.imag_start = imag_start
        self.imag_stop = imag_stop
        self.imag_parts = imag_parts

    def exec(self):
        for i in range(20):
            print(i, end=" ")
        print()

    def __str__(self):
        s = ""
        s += f"real: {self.real_start}, {self.real_stop}, {self.real_parts}\n"
        s += f"imag: {self.imag_start}, {self.imag_stop}, {self.imag_parts}"
        return s
