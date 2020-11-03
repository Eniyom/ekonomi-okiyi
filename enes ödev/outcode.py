l = []
with open('list.txt') as f:
    l = f.readlines()

data = ""
i = 1
for a in [num[:-1].encode('utf8').decode('utf8') for num in l]:
    out = f'''\t\t\tcase {i}:
            \treturn "{a}";
            \tbreak;\n'''
    data += out
    i += 1
with open('out.txt','w') as f:
    f.write(data)
