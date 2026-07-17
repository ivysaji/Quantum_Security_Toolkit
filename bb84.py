import random
def generate_bits(n):
     return [random.randint(0,1) for i in range(n)] 
def generate_bases(n):
     return [random.choice(['+','x']) for i in range(n)]
bob_bases = generate_bases(8) 
n = 8 
alice_bits = generate_bits(n)
alice_bases = generate_bases(n) 
bob_bases = generate_bases(n) 
print("Alice Bits :", alice_bits) 
print("Alice Bases:", alice_bases) 
print("Bob Bases :", bob_bases)  
shared_key=[] 
for i in range(n):
     if alice_bases[i]==bob_bases[i]:
         shared_key.append(alice_bits[i]) 
print("Shared Secret Key") 
print(shared_key) 