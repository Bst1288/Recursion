def towerOfHanoi(rings, fromPole, toPole, auxPole):
    if rings == 1:
        print('Move ring 1 from',fromPole,'to',toPole)
        return
    towerOfHanoi(rings-1,fromPole,auxPole,toPole)
    print('Move ring',rings,'from',fromPole,'to',toPole)
    towerOfHanoi(rings-1,auxPole,toPole,fromPole)

rings = int(input('Tower of hanoi: '))
towerOfHanoi(rings,'L','R','M')