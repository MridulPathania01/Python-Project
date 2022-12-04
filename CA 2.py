def student(n,a=1):
    p = []
    c = 0
    while True:
        
        r = 0
        a = a + 1
        b = str(a)
        #test if candidate is prime
        for i in p:
            if a%i == 0:
                r += 1
        #test if candidate is palindromic
        d = b[len(b)::-1]
        if r == 0:
            p.append(a)
            if b == d:
                c += 1
        if c == n:
            return a
n=int(input("Enter the nth number : "))
print(n,"th prime palindrome number is ",student(n))
