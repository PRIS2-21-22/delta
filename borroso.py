
class borroso:
    def __init__(self,m,alpha,beta):
        """Constructor del borroso"""
        self.m=m
        self.alpha = alpha
        self.beta = beta
        #self.p = p

    def suma(self,num):
        m = self.m+num.m
        alpha = self.alpha + num.alpha
        beta = self.beta + num.beta
        return borroso(m,alpha,beta)

    def resta(self,num):
        m = self.m-num.m
        alpha = self.alpha + num.beta
        beta = self.beta + num.alpha
        return borroso(m,alpha,beta)

    def opuesto(self):
        m = -self.m
        alpha = self.beta
        beta = self.alpha
        return borroso(m,alpha,beta)

    def multiplicacion(self, num):
        if self.m > 0:
            if num.m > 0:
                m = self.m * num.m
                alpha = self.m * num.alpha + self.alpha * num.n
                beta = self.m * num.beta + self.beta * num.m
                return borroso(m, alpha, beta)
            elif num.m < 0:
                m = self.m * num.m
                alpha = self.m * self.alpha - num.beta * num.n
                beta = self.m * self.beta - num.alpha * num.m
                return borroso(m, alpha, beta)
        elif self.m < 0:
            if num.m > 0:
                m = self.m * num.m
                alpha = num.m * self.alpha - self.m * num.beta
                beta = num.m * self.beta - self.m * num.alpha
                return borroso(m, alpha, beta)
            elif num.m < 0:
                m = self.m * num.m
                alpha = -num.m * self.beta - self.m * num.beta
                beta = -num.m * self.alpha - self.m * num.alpha
                return borroso(m, alpha, beta)

    def division(self, num):
        m = self.m / num.m
        alpha = (self.m*num.beta+self.alpha*num.m)//(num.m**2)
        beta = (self.m*num.alpha+self.beta*num.m)//(num.m**2)
        return borroso(m, alpha, beta)

    def __str__(self):
        """To String del borroso"""
        return "M: {},Alpha: {}, Beta: {}".format(self.m, self.alpha, self.beta)

borr1 = borroso(m=0,alpha=1,beta=2)
borr2 = borroso(m=1,alpha=2,beta=3)
borrSuma = borr1.suma(borr2)
borrResta = borr1.resta(borr2)
borrMul = borr1.multiplicacion(borr2)
borrDiv = borr1.division(borr2)
borrOpu1 = borr1.opuesto()
borrOpu2 = borr2.opuesto()
print("Suma de",borr1," y ",borr2,"->",borrSuma)
print("Resta de",borr1," y ",borr2,"->",borrResta)
print("Multiplicación de",borr1," y ",borr2,"->",borrMul)
print("División de",borr1," y ",borr2,"->",borrDiv)
print("Opuesto de",borr1,"->",borrOpu1)
print("Opuesto de",borr2,"->",borrOpu2)
