n = int(input("몇 단까지 출력할까요?"))
for a in range(1, n+1):
    print("------", "[", a, "단", "]", "------")
    for b in range(1, 20):
        print(a, "X", b, "=", a*b)
