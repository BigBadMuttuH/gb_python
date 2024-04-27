data = [2, 4, 6, 8, 9, 10, 23, 3443]
print(*data, sep='\t')

a, b, c, *d = data
print(a, b, c, d, sep='\t')

*a, b, c,  = data
print(a, b, c, sep='\t')

# можно забрать первый и последний элемент
a, *_, b, = data
print(a, b, sep='\t')

link = 'https://gateway.pinata.cloud/ipfs/bafybeia4nrbuvpfd6k7lkorzgjw3t6totaoko7gmvq5pyuhl2eloxnfiri'
prefix, *_, suffix = link.split('/')
print(prefix, suffix, sep='\t')

# Множество
data = {10, 9, 5, 8, 1, 2}
a, b, c, *d, e = data
print(a, b, c, d, e, sep='\t')
