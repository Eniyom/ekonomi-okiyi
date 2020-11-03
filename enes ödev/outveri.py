data = ""
with open('veri.txt') as f:
    data = f.read()
 
chars = [char for char in data]
out = []
for a in chars:
    if (a.isdigit() == False) and (a != "\n"):
        if a == "\t":
            out.append("\n")
        else:    
            out.append(a)
with open('list.txt','w') as f:
    f.write("".join(out))    
