class Solution:
    def addBinary(self, a: str, b: str) -> str:
        summ = ''
        carrier = 0

        for i in range(min(len(a), len(b))):
            summ = str((int(a[-1-i]) + int(b[-1-i]) + carrier) % 2) + summ
            carrier = (int(a[-1-i]) + int(b[-1-i]) + carrier) // 2
        
        if len(a) < len(b):
            for i in range(len(b) - len(a)):
                summ = str((int(b[-1-len(a)-i]) + carrier) % 2) + summ
                carrier = (int(b[-1-len(a)-i]) + carrier) // 2
            if carrier == 1:
                summ = str(carrier) + summ
        if len(a) > len(b):
            for i in range(len(a) - len(b)):
                print(carrier)
                summ = str((int(a[-1-len(b)-i]) + carrier) % 2) + summ
                carrier = (int(a[-1-len(b)-i]) + carrier) // 2
                print(int(a[-1-len(b)-i]), carrier)
            if carrier == 1:
                summ = str(carrier) + summ
        if len(a) == len(b):
            if carrier == 1:
                summ = str(carrier) + summ
        return summ
