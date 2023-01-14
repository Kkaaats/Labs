class PB:
    m=571
    def __init__(self, n):
        p = "10000100101"
        if len(n)==self.m: self.n=n
        elif len(n)<self.m: self.n=n.zfill(self.m)
        elif len(n)>self.m:
            res = PB(n[-571:])
            for i in range(self.m, len(n)):
                if n[::-1][i] == "1":
                    res += PB(p) << (i - self.m)
            try: self.n = res.n
            except: self.n = res
        
    def __add__(self, other): 
        res = ""
        for i in range(len(self.n)):
            if self.n[i] == other.n[i]: res=res+ "0"
            else: res =res+ "1"
        res=PB(res)
        return res

    def __lshift__(self, n):
        res=self.n + "0" * n
        res=PB(res)
        return res

    def __mul__(self, other):
        res = PB("0")
        for i in range(len(other.n)):
            if other.n[i] == "1":
                res1=self << (len(other.n) - i - 1)
                res =res1+ res
        return res
    def powsq(self):
        return self*self

    def __pow__(self, pow):
        res=PB("1")
        while(pow>0):
            if(pow%2==1): res=res*self
            self=self*self
            pow=pow//2
        return res

    def trace(self):
        matrix=[]
        a=self.n.lstrip('0')
        for i in range(len(a)):
            matrix.append(a[i])
        return matrix[-1]
   

n1=PB('11110001011000101110100000011000100000010111010011010011110100001011001110101111111100101011010110000011000110010101001011111100101001011010110000001110011011010011000100001')
n2=PB('10111100011110010110000111000111001010000110111011111100000110011111101110000101101110110101000111000011000010010001111001010110100011011111100001100010000010000001111101010')
n3=3

print("Сумa n1 + n2: ", (n1+n2).n.lstrip('0'))
print("Множення n1 * n2: ",(n1*n2).n.lstrip('0'))
print("n1 в степені n3: ",(n1**n3).n.lstrip('0'))
print("Слід n1: ",n1.trace())
print("Слід n2: ",n2.trace())
print(" n1 в квадраті: ",(n1.powsq()).n.lstrip('0'))



