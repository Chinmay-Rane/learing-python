#prevent print() fromm printing new line at end

print("Chinmay")
print("HELLO")
#prints
'''Chinmay
HELLO'''

print("Chinmay", end="")
print("HELLO", end="")

# prints
'''ChinmayHELLO''' 
#doesnt add new line at end