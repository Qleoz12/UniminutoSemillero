from fraction import fraction 

class mathFractions:
     def __init__(self,operation,fraction1,fraction2,num=1,denom=1): 
          self.operation=operation
          self.fraction1=fraction1
          self.fraction2=fraction2
          self.num=num
          self.denom=denom
          'print("se creo el profe")'


     def sumar_fracciones(self,fraction1 ,fraction2):
           self.num=fraction1.get_n()*fraction2.get_d()+fraction2.get_n()*fraction1.get_d()
           self.denom=fraction1.get_d()*fraction2.get_d()
     
     def restar_fracciones(self,fraction1 ,fraction2 ):
           self.num=fraction1.get_n()*fraction2.get_d()-fraction2.get_n()*fraction1.get_d()
           self.denom=fraction1.get_d()*fraction2.get_d()
     
     def multiplicar_fracciones(self,fraction1 ,fraction2 ):
           self.num=fraction1.get_n()*fraction2.get_n()
           self.denom=fraction1.get_d()*fraction2.get_d()
     
     def dividir_fracciones(self,fraction1 ,fraction2 ):
          self.num=fraction1.get_n()*fraction2.get_d()
          self.denom=fraction2.get_n()*fraction1.get_d()


     def determinate_operation(self):
          if self.operation == '+':
               self.sumar_fracciones(self.fraction1,self.fraction2)
          elif self.operation=="-":
               self.restar_fracciones(self.fraction1,self.fraction2)
          elif self.operation=="*":
               self.multiplicar_fracciones(self.fraction1,self.fraction2)
          elif self.operation=="/":
               self.dividir_fracciones(self.fraction1,self.fraction2)
          else:
               print("operation no soportada")
     
     def simplifyFraction(self):
          gcd_value=self.determinate_GCD(self.num,self.denom)
          self.num_simplify=int(self.num/gcd_value)
          self.denom_simplify=int(self.denom/gcd_value)
          print("{}/{} = {}/{}".format(self.num,self.denom,self.num_simplify,self.denom_simplify))

     'return the valueof GCD'
     'uing the  euclidean algorithm, we can determinate de GCD for the fraction n/d'
     def determinate_GCD(self,numerator,denominator):
        numerator=abs(numerator)
        denominator=abs(denominator)
        if numerator<denominator:
             pivot=numerator
             numerator=denominator
             denominator=pivot
        if denominator==0:
             return numerator
        'first stem into GCD'
        res=numerator%denominator;
        while res>0: 
             numerator=denominator
             denominator=res
             res=numerator%denominator
        
        return denominator

     def result(self):
          self.determinate_operation()
          self.simplifyFraction()
