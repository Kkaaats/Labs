def matrix():
    matrix = []
    m = 641
    p = 2*m+1
    for i in range(m):
        row = []
        for j in range(m):
            if (2**i + 2**j) % p == 1 or (2**i - 2**j) % p == 1 or (-2**i + 2**j) % p == 1 or (-2**i - 2**j) % p == 1:
                row.append('1')
            else:
                row.append('0')
        matrix.append(row)  
    return matrix

class ONB:
    m=641
    def __init__(self, n):
        lenn=self.m-len(n)
        n="0"*lenn + n
        self.n=n

    def __add__(self, other): 
        res = ""
        for i in range(len(self.n)):
            if self.n[i] == other.n[i]: res=res+ "0"
            else: res =res+ "1"
        res=ONB(res)
        return res

    def __rshift__(self,k):
        res = self.n[-k:] + self.n[:-k]
        return ONB(res)
    def __lshift__(self, k):
        res = self.n[k:] + self.n[:k]
        return ONB(res)

    def mul(self, other, matrix):
        result = ''
        for i in range(self.m):
            ao = self << i
            bo = other << i
            string = ''
            for i in range(self.m):
                res = 0
                for j in range(self.m):
                #     if self.n[j] == "0" or matrix[i][j] == "0":
                #         res += 0
                #     else: res += 1
                # string += str(res % 2)
                    a = int(ao.n[j])
                    b = int(matrix[i][j])
                    res += a*b
                string += str(res % 2)
            res = 0
            for i in range(self.m):
                a = int(string[i])
                b = int(bo.n[i]) 
                res += a * b        
            result =result+ str(res % 2) 
        return ONB(result)
    
    def trace(self):
        res=0
        for i in range(len(self.n)):
            if self.n[i]=="1": res=res+1
        if res%2==0: return 0
        else: return 1

    def powsq(self):
        return (self<<1).n

    def pows(self, pow, matrix):
        exp=pow.n
        res=ONB("1")
        for i in range(len(exp)):
            if exp[i]=="1": res=(res.mul(self, matrix))
            else: res=(res.mul(res,matrix))
        print (res.n)
        return res.n


a=ONB("11101100101111100000100100110001010110111001010100000111000011101101011100010010101001001010101000111110001001111000101001010001011011001001001000101001101100001111000101011100000000000111000010110000011111000111011100110010110001110") 
b=ONB("00001100000001001001001011010110101101110101001000101110101010010111100110100111101000110000001000001100100100010110100100110010010001011101100000110110111011011100100011100100000110010011010011001101001101010011110111011101110011001") 
c=ONB("11101100101111100000100100110001010110111001")
d=ONB("00001100000001001001001011010110101101110101")
m=ONB("1010100010111")
print("Сума: ", (a+b).n.lstrip('0'))
print("Слід: ", b.trace())
print("Множення: ",a.mul(b, matrix()).n)
print("Квадрат числа: ",a.powsq())
k=ONB('0010')
print(m.pows(k, matrix()))



    