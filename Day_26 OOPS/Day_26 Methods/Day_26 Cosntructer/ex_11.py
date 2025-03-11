                  # Pameterised Constructor


class MWS:
    def __init__(self,fName,lName,contact,address):
        self.fn=fName
        self.ln=lName
        self.ct=contact
        self.ads=address
po=MWS("Harinath","M",9666615448,"MADANAPALLI - 517325")
print("first name: ",po.fn)
print("Last name: ",po.ln)
print("Conatct: ",po.ct)
print("Address",po.ads)

print("\n")

no=MWS("Jagadeesh","B",6305134256,"NIMMANPALLI")
print("first name: ",no.fn)
print("Last name: ",no.ln)
print("Conatct: ",no.ct)
print("Address",no.ads)

print("\n")

no=MWS("Satheesh","B",6305134256,"NIMMANPALLI")
print("first name: ",no.fn)
print("Last name: ",no.ln)
print("Conatct: ",no.ct)
print("Address",no.ads)

