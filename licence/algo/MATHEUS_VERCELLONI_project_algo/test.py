from algo import*


def test():
    s=100
    k=10
    d=3
    genere_cap_rand('cap_rand.txt',s,k)
    print(algo1('cap_rand.txt'))
    print(algo2('cap_rand.txt'))
    print(glouton('cap_rand.txt'))
    
    
test()