# break      continue

for i in range(1,10):
    if i==5:
        break
    print(i)


print("-----------------------------------")

for i in range(1,10):
    if i==5 or i==7 or i==8:
        continue
    print(i)