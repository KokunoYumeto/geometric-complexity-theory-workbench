"""Independent small checks (agent a17221e5) for statements A and B on GCT VI.
1. ordinary and symmetric Kronecker multiplicities g, sk at lambda=s(2m,2m), rectangles (4s)^m, against the box difference;
   the same at lambda=k(m-1,1), rectangles k^m, against partitions of k into parts 2..m.
2. numeric inequalities used to move the no-occurrence proof to an independent padding variable (n>=5).
3. the degree-one dimension drop that gives non-normality of the reduced class variety."""
from fractions import Fraction as F
from functools import lru_cache
from math import comb, factorial, prod
def parts(n,m=None):
    if n==0: yield (); return
    for k in range(min(n,m or n),0,-1):
        for r in parts(n-k,k): yield (k,)+r
@lru_cache(None)
def chi(beta,mu):
    if not mu: return 1
    r=mu[0];t=0
    for b in beta:
        if b>=r and b-r not in beta:
            t+=(-1)**sum(b-r<x<b for x in beta)*chi(tuple(sorted([x for x in beta if x!=b]+[b-r],reverse=True)),mu[1:])
    return t
B=lambda l:tuple(l[i]+len(l)-1-i for i in range(len(l)))
def square(mu): return tuple(sorted([x for a in mu for x in ([a/2,a/2] if a%2==0 else [a])],reverse=True))
def kron(lam,rect):
    g=sq=F(0); bl=B(lam); br=B(rect)
    for mu in parts(sum(lam)):
        a=chi(bl,mu)
        if not a: continue
        z=prod(k**mu.count(k)*factorial(mu.count(k)) for k in set(mu))
        g+=F(a*chi(br,mu)**2,z); sq+=F(a*chi(br,tuple(int(x) for x in square(mu))),z)
    return g,(g+sq)/2
@lru_cache(None)
def box(k,n,w):
    if k==0: return 1
    if k<0 or n==0 or w==0: return 0
    return box(k,n-1,w)+box(k-n,n,w-1)
for s,ms in ((1,range(3,9)),(2,(3,4))):
    for m in ms:
        g,sk=kron((2*s*m,2*s*m),(4*s,)*m); f=box(2*s*m,m,4*s)-box(2*s*m-1,m,4*s)
        print('lambda=%d(2m,2m) m=%d'%(s,m),g,sk,f,g==sk==f,flush=True)
for m in range(3,7):
    for k in range(1,7):
        if k*m>30: continue
        g,sk=kron((k*(m-1),k),(k,)*m); f=sum(1 for p in parts(k,m) if 1 not in p)
        print('lambda=%d(m-1,1) m=%d'%(k,m),g,sk,f,g==sk==f,flush=True)
ok=all(2*(M+1)**10<=M**12 and 2*(M+1)**20<=M**25 and 24*(M+1)**6<=M**25 and 4*(M+1)**6<M**12 for M in range(5,2001))
print('transfer inequalities n=5..2000',ok)
ok=all(comb(n*n+p,p)*comb(n*n+n,n)>comb(n*n+p+n,p+n) for n in range(2,9) for p in range(1,40))
print('degree-one map not surjective',ok)
