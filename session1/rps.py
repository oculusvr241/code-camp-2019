p1=input('r,p,or s?')
p2=input('r,p,or s?')
if p1 and p2=='r'or'p'or's':
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
if p1=='s':
    #p1 wins
    if p2=='p':
        print('p1 wins with scissors')
    #p1 loses
    if p2=='r':
        print('p2 wins with rock')
if p1=='i win':
    #p1 wins
        print('p1 wins automaticly. its super effective. p2 gets knocked out')
if p2=='i win':
    #p2 wins
        print('p1 dies in a hole. p2 wins by default')
if p1 and p2=='i win':
    print('ladies, ladies. your both pretty. actually your both ugly corpses. play again')
if p1 and p2=='':
    print('SAY SOMETHING!!!!!!!!!!!')
if p1=='uno reverse card':
    #p1 loses
    if p2=='r'or'p'or's':
        print('uno reverse failed')
    if p2=='i win':
        print('UNO REVERSE CARD! p1 wins') 
if p2=='uno reverse card':
    #p2 loses
    if p1=='r'or'p'or's':
        print('uno reverse failed')
    if p1=='i win':
        print('UNO REVERSE CARD! p2 wins') 
if p1=='NOPE!!!':
    if p2=='UNO REVERSE CARD!':
        print('UNO and NOPE collide and create a world destroying reverse tornado')
    if p2=='r'or'p'or's':
        print('whoever thought p1 was genuis for choosing nope is an idiot along with p1. p2 wins obviously.')
if p2=='NOPE!!!':
    if p1=='UNO REVERSE CARD!':
        print('UNO and NOPE collide and create a world destroying reverse tornado')
    if p1=='r'or'p'or's':
        print('whoever thought p2 was genuis for choosing nope card, is and idiot along with p2. p1 wins obviously.')