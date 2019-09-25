class fraction: 
   def __init__(self,_numerator=1,_denominator=1):   
          self._numerator   = _numerator
          self._denominator = _denominator

   def get_n(self):
      return self._numerator
   def set_n(self, n):
      self._numerator = n
      
   def get_d(self):
      return self._denominator
   def set_d(self, n):
      self._denominator = n