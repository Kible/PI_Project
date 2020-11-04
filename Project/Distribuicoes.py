from numpy import random, sqrt, log

#Normal/Gauss Continua
def normal(mu, sigma):
        #Unif intervalo [0, 1]
        #To sample Unif[a, b], b > a multiply the output of random_sample by (b-a) and add a:
        #[-1,1] => a=-1 && b = 1
        a=-1
        b=1
        while True:
            u1 = random.random()*(b-a)+a
            u2 = random.random()*(b-a)+a
            u = u1**2 + u2**2
            if u<1:
                break
        return mu + sigma * u1 * sqrt(-2.0 * log(u)/u)

#Exponencial Continua
def expo(a, med):
    u = random.random()
    return a-med*log(u)

#Bernoulli Discreta (um caso especifico da discreta em que n = 1)
def bernoulli(p):
    u = random.random()
    if u<p:
        return 1
    else:
        return 0

#Binomial Discreta
def binomial(n, p):
    cases = 0
    for i in range(n):
        cases = cases + bernoulli(p)

    return cases
    
#Uniforme Discreta (com [0,1], e o mesmo que Bernoulli com p = 0.5)
def uniformeDisc(a, b):
        u = random.random()
        return a+int((b-a+1)*u)
        

#Uniforme Continua
def uniformeCont(a, b):
        u = random.random()
        return a+((b-a)*u)
