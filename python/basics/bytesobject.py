# Byte object common uses

#1. Streaming files
#2. Transmitting text with out knowing the encoding 
#3. often used "under the hood" in python libraries

print(bytes(4))

sample1 = bytes('!vjvujy', 'utf-8')
print(sample1)

print(sample1.decode('utf-8'))


