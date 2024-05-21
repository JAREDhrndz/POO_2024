n1=0
u=0
for u in range (1,10):
    print(f"Tabla del {u}")
    for i in range (1,11):
        n1=i*u
        print(f"{u} x {i} = {n1}")
    u+=1
    print("")
