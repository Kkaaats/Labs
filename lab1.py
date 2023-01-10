from textwrap import wrap

class BigInteg:
    length = 2048
    hex = '0123456789abcdef'
    def __init__(self, n): #конструктор
        n = n[-self.length:]
        for char in n:
            if char not in self.hex:
                 break
        self.n = n.zfill(self.length)
    def __bin__(self):
        bin_num=""
        num = self.n.lstrip('0')
        i=0
        while i<len(num):
            if num[i] == '0':
               bin_num = bin_num + "0000"
            elif num[i] == '1':
               bin_num = bin_num + "0001"
            elif num[i] == '2':
               bin_num = bin_num + "0010"
            elif num[i] == '3':
               bin_num = bin_num + "0011"
            elif num[i] == '4':
               bin_num = bin_num + "0100"
            elif num[i] == '5':
               bin_num = bin_num + "0101"
            elif num[i] == '6':
               bin_num = bin_num + "0110"
            elif num[i] == '7':
               bin_num = bin_num + "0111"
            elif num[i] == '8':
               bin_num = bin_num + "1000"
            elif num[i] == '9':
               bin_num = bin_num + "1001"
            elif num[i] == 'a' or num[i] == 'A':
               bin_num = bin_num + "1010"
            elif num[i] == 'b' or num[i] == 'B':
              bin_num = bin_num + "1011"
            elif num[i] == 'c' or num[i] == 'C':
               bin_num = bin_num + "1100"
            elif num[i] == 'd' or num[i] == 'D':
                bin_num = bin_num + "1101"
            elif num[i] == 'e' or num[i] == 'E':
                bin_num = bin_num + "1110"
            elif num[i] == 'f' or num[i] == 'F':
                bin_num = bin_num + "1111"
            i = i+1
        return bin_num.zfill(self.length*4)

    def elder_bit(self): #номер старшого біта числа
        binary = self.toBin().lstrip('0')
        return len(binary) - 1

    def todem(self, t):
        if str(t) == 'a':
            res = 10
        elif str(t) == 'b':
            res = 11 
        elif str(t) == 'c':
            res = 12
        elif str(t) == 'd':
            res = 13
        elif str(t) == 'e':
            res = 14
        elif str(t) == 'f':
            res = 15
        else: res = int(t)
        return res

    def tohex(self, t):
        if int(t) == 10:
            res = 'a'
        elif int(t) == 11:
            res = 'b' 
        elif int(t) == 12:
            res = 'c'
        elif int(t) == 13:
            res = 'd'
        elif int(t) == 14:
            res = 'e'
        elif int(t) == 15:
            res = 'f'
        else: res = str(t)
        return res    

    def __add__(self, other):
        c = ""
        carry = 0
        for i in range(len(self.n)-1, 0, -1):
            a = self.todem(self.n[i])    
            b = other.todem(other.n[i])
            res = a + b + carry
            if res > 16:
                carry = 1
                res -= 16
            else: 
                carry = 0
            res = self.tohex(res)
            c += res
        return c[::-1]    
    def __sub__(self, other):
        c = ""
        borrow = 0
        for i in range(len(self.n)-1, 0, -1):
            a = self.todem(self.n[i])    
            b = other.todem(other.n[i])
            res = a - borrow - b
            if res < 0:
                borrow = 1
                res += 16
            else: 
                borrow = 0
            res = self.tohex(res)
            c += res
        return c[::-1]   
                  
    

    def fromBin(self, binary):
        result = ''
        result_arr = tuple(wrap(binary, 4))
        for binary in result_arr:
            if binary == '0000':
                result = result + '0'
            elif binary == '0001':
                result = result + '1'
            elif binary == '0010':
                result = result + '2'
            elif binary == '0011':
                result = result + '3'
            elif binary == '0100':
                result = result + '4'
            elif binary == '0101':
                result = result + '5'
            elif binary == '0110':
                result = result + '6'
            elif binary == '0111':
                result = result + '7'
            elif binary == '1000':
                result = result + '8'
            elif binary == '1001':
                result = result + '9'
            elif binary == '1010':
                result = result + 'a'
            elif binary == '1011':
                result = result + 'b'
            elif binary == '1100':
                result = result + 'c'
            elif binary == '1101':
                result = result + 'd'
            elif binary == '1110':
                result = result + 'e'
            elif binary == '1111':
                result = result + 'f'
        return result.lstrip("0")


n=BigInteg("a15")
n1=BigInteg("bc")
n2=n1+n
print(n2.lstrip('0'))
