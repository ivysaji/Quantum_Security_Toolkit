import random 
original_key = [random.randint(0,1) for i in range(8)] 
print("Original Key") 
print(original_key)
modified_key = [] 
for bit in original_key:
    if random.random() < 0.30:
        modified_key.append(1-bit)
    else:
        modified_key.append(bit)
print()
print("Modified key")
print(modified_key)
errors = 0
for i in range(len(original_key)):
    if original_key[i] != modified_key[i]:
        errors += 1 
    print()
    print("Errors :", errors) 
if (errors > 0):
  print("ATTACK DETECTED")
else:
  PRINT("COMMUNICATION SECURE")