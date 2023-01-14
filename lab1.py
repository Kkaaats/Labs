from textwrap import wrap

class BigInteg:
    length = 2048
    hex = '0123456789abcdef'
    def __init__(self, n): 
        n = n[-self.length:]
        for char in n:
            if char not in self.hex:
                 break
        self.n = n.zfill(self.length)
    def tobin(self):
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

    def elder_bit(self): 
        binary = self.tobin().lstrip('0')
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
            if res > 15:
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

    def LongMulOneDigit(self, b):
        carry=0
        c=""
        a = self.n.lstrip("0")
        b = int(self.todem(b))
        for i in range(len(self.n)-1, 0, -1):
            a = int(self.todem(self.n[i])) 
            res=a*b+carry
            if res > 15:
                carry = res//16
                res =res%16
            else: 
                carry = 0
            res = self.tohex(res)
            c += res
        return c[::-1].lstrip('0')

    def __mul__(self,other):
        mull = other.n.lstrip('0')[::-1]
        lst = []
        for i in range(0, len(mull)):
            temp=self.LongMulOneDigit(mull[i])
            temp+= "0"*i
            temp = BigInteg(temp)
            lst.append(temp)
        last = lst[0]
        if len(lst) == 1:
            return last.n.lstrip("0")
        for i in range(1, len(lst)):
            a = lst[i]
            res = BigInteg(last + a)
            last = res
        return res.n.lstrip("0")
    def LongCmp(self, other):
        i = len(self.n)-1
        while self.n[-i] == other.n[-i] and i != -1:
            i = i-1
        if i == -1: 
            return 0
        else:
            if self.n[-i]>other.n[-i]: 
                return 1
            else: return -1
    def LongDivMod(self, other):
        A = self.n.lstrip('0')
        B = other.n.lstrip('0')
        o_len = len(B)
        to_add = A[o_len:]
        A = BigInteg(A[:o_len])
        res = ""
        while A.LongCmp(other) != 0:
            if A.LongCmp(other) == -1:
                #res=BigInteg("0")
                return "0"
            test = 0
            while A.LongCmp(other) ==1:
                a = A.n.lstrip('0')
                b = other.n.lstrip('0')
                A = A - other
                A = BigInteg(A)
                test += 1
            if A.LongCmp(other) == 0:
                test += 1
            test = self.tohex(test)
            res += test
            if len(to_add) != 0:
                A = A.n.lstrip("0") + to_add[0]
                to_add = to_add[1:]
                A = BigInteg(A)
        return res
    def __pow__(self, other):
        c=""
        d = other.n.lstrip('0')[::-1]
        res=0
        for i in range (len(d)):
            res+=other.todem(d[i])*16**i
        temp=BigInteg('1')
        for i in range(res):
            temp = self * temp
            temp=BigInteg(temp)
        return temp.n              
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
   #Редукція Барретта
    def right_shift(self, n):
        bit = self.tobin()
        res= self.fromBin(n*'0'+bit[:-n])
        res1=BigInteg(res)
        return res1.n

    def left_shift(self, n):
        bit = self.tobin()
        res=bit[n:] + '0' *n
        res= self.fromBin(res)
        res1=BigInteg(res)
        return res1

    def BarrettReduction(self, n):
        c=BigInteg("1")
        k= n.elder_bit()+1
        #m=c.left_shift(2*k).LongDivMod(n)
        m=BigInteg("733")
        q= self.right_shift(k-1)
        q=BigInteg(q)
        q = q*m
        q=BigInteg(q)
        q= q.right_shift(k+1)
        q=BigInteg(q)
        a=q*n
        a=BigInteg(a)
        r=self-a
        r=BigInteg(r)
        while(r.LongCmp(n)!=-1):
            r-=n
            r=BigInteg(r)
        return r.n

a=BigInteg("45a5c")
b=BigInteg("21f")
print(a.BarrettReduction(b).lstrip('0'))
n=BigInteg("a15d3")
n1=BigInteg("2")
n4=BigInteg("bd45a8d3")
nn1=(n4+n).lstrip('0')
nn2=(n4-n).lstrip('0')
nn3=(n*n4).lstrip('f')
nn4=(n**n1).lstrip('0')
nn5=n4.LongDivMod(n)
nn6=n4.tobin().lstrip('0')
nn7=n4.fromBin(nn6).lstrip('0')
enter=f'''Сума = {nn1}
Віднімання = {nn2}
Множення = {nn3}
Степінь числа = {nn4}
Ділення = {nn5}
Бінарний вигляд = {nn6}
З бінарного = {nn7}
'''
print(enter)