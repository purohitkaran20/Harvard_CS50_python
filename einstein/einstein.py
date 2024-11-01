# print("Welcome to the calculator where you can find out the equivalent amount of energy in Joules for given mass, using famous equation E=MC^2")
# M = int(input("Enter the Mass value in kg for which you need to compute equivalent energy in Joules\n"))
# E = M*pow(300000000,2)
# print(int(E))

def formula(m):
    E = m * ((3*(10**8))**2)
    return E

m = int(input("Enter Mass (Kg): "))

print(f"Energy (J)= {formula(m)}")
