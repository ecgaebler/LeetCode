class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        split_a = a.split("+")
        a_real, a_imag = int(split_a[0]), int(split_a[1][:-1])
        split_b = b.split("+")
        b_real, b_imag = int(split_b[0]), int(split_b[1][:-1])
        final_real = a_real * b_real - a_imag * b_imag
        final_imag = a_real * b_imag + a_imag * b_real
        return str(final_real) + "+" + str(final_imag) + "i"