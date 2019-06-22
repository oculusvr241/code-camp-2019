# data setup
rooms = {
    'empty': {
        'name': 'an empty room', 
        'east': 'bedroom', 
        'north': 'temple',
        'text': 'The stone floors and walls and cold and damp.'},
    'temple': {
        'name': 'a small temple', 
        'east': 'torture', 
        'south': 'empty',
        'text': 'There are three rows of benches facing a small statue.'},
    'torture': {
        'name': 'a torture chamber', 
        'west': 'temple', 
        'south': 'bedroom',
        'text': 'There is a rack and an iron maiden against the wall\nand some chains and thumbscrews on the floor.'},
    'bedroom': {
        'name': 'a bedroom', 
        'north': 'torture', 
        'west': 'empty',
        'text': 'There is a large bed with black, silk sheets on it.'}
    }
commands = ['north','south','west','east']
room = rooms['empty']

#game loop
while True:
    print(f'you are in {room['name']}')