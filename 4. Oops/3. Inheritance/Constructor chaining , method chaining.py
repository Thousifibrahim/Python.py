class bank:
    bname = 'vijaya'
    loc= 'rajaji'
    ifc = 'VIJ0015'
    
    def __init__ (self,name , phone, bal):
        self.name=name
        self.phone=phone
        self.bal=bal
        
    def display(self):
        print(self.name, self.phone, self.bal , end = ' ' )

class bank_merge(bank):
    bname = 'BOB'
    ifc = 'BOB10015'
    
    def __init__(self, name,phone,bal,pan,aadhar):
        super().__init__(name,phone,bal)
        self.pan=pan
        self.aadhar=aadhar
        
    def display_all(self):
        super().display()
        print(self.pan, self.aadhar)

vijayalakshmi=bank_merge('vijayalakshmi',7896541236,50000,'VIJ456','75396385')

print(vijayalakshmi.display_all())
