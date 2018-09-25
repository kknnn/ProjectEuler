def esPrimo(numero):
    divisores=[]
    for i in range(1,numero+1):
        if(numero%i==0):
            divisores.append(i)
    if(len(divisores)==2):
        return True
    else:
        return False

def sum_primes(limit):
    primes = []
    for n in range(2, limit+1):
        # try dividing n with all primes less than sqrt(n):
        for p in primes:
            if n % p == 0: break     # if p divides n, stop the search
            if n < p*p:
               primes.append(n)      # if p > sqrt(n), mark n as prime and stop search
               break
        else: primes.append(n)       # fallback: we actually only get here for n == 2
    return sum(primes)

if(esPrimo(2000000)):
    print("Es primo")
else:
    print("NO")