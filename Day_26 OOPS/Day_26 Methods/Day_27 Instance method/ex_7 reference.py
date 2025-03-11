# Setters and Getters

class saif:
    def setfname(self,name):
       self.fn=name
    def getfname(self):
        return self.fn
    def setlname(self,lname):
        self.ln=lname
    def getlname(self):
        return self.ln
u=saif()
u.setlname("muthyala")
u.setfname("harinath")

print(u.getfname())
print(u.getlname())

#
# '''333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333'''
# '''333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333'''
#
# class rbm:
#     def setnames(self,name):
#         self.n=name
#     def getnames(self):
#         return self.n
# ij=rbm()
# ij.setnames("hai")
#
# print(ij.getnames())
#
# '''333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333'''
#
# class ij:
#     def io(self,name):
#         self.name=name
#
#     def getio(self):
#         return self.name
# ok=ij()
# ok.io("hello")
# print(ok.getio())
#
