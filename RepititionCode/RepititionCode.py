"""

RepititionCode
@description this is repitition code used in error correcting
            usually its a 3/2 error correcting
            meaning for every 3 bits if two bits are equal to 1 then the bit value is 1
            it sends 3 bits for every single bit to make sure the correct bit is received


"""

class RepititionCode:

    reps = 3 # number of bits used in error correcting

    def to_normal(self,string):
        res = ""

        for i in range(0,len(string),self.reps):
            one = 0
            zero = 0
            bit3 = string[i:i+self.reps]
            for z in range(0,len(bit3)):
                if bit3[z] == "1":
                    one += 1
                else:
                    zero += 1

            res += "1" if one > zero else "0"

        return res

    def to_repitition(self, string):
        res = ""

        for i in range(0, len(string)):
            res += ''.join([string[i] for z in range(0, self.reps)])

        return res



"""
print("input binary rep to binary:")

z = input()

rep = RepititionCode32()

res = rep.to_normal(z)

print(res)

"""

"""
print("input binary to convert to rep:")

z = input()

rep = RepititionCode32()

res = rep.to_repitition(z)

print(res)
"""
