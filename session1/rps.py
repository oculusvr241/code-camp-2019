p1=input('r,p,or s?')
p2=input('r,p,or s?')
if p1 == p2:
    print('tie')
if p1=='r':
    #p1 wins
    if p2 == 's':
        print('p1 wins with rock')
    #p1 loses
    if p2 == 'p':
        print('p2 wins with paper')
if p1=='p':
    #p1 wins
    if p2=='r':
        print('p1 wins with paper')
    #p1 loses
    if p2=='s':
        print('p2 wins with scissors')    
    