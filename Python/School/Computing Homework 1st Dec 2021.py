def CheckForPrime(P):
    if P == 1 or P == 0 or (P % 2 == 0 and P > 2):
        return "Not a Prime number"
    else:
        for i in range (3, int(p**(1/2))+1, 2):
            if P%i == 0:
                return "Not a Prime number"
        return "This is a prime number"

S = 12
P = int(input("Value for P: "))

S_equals_0 = False

while S_equals_0 == False:
    if P%2 == 0:
        P+=1
        if CheckForPrime(P) == "Prime":
            if P<5:
                S = S - P
                P = P + 2
            else:
                S = S - 1
                if S == 0:
                    print(P)
                    S_equals_0 = True
                else:
                    P = P + 2
    else:
        P = P + 2
