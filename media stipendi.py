x = 0
count = 0
while True:
    y = int(input("guadagno dipendente:"))
    if y == -1:
        break
    else:
        x += y
        count += 1
    
print("media degli stipendi:", x/ count,"€")
