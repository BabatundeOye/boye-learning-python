counter = 1
while counter <= 25:
    if counter % 4 == 0:
        print(counter)
    counter += 1
    
print("looping")

for _ in range(4):
    print('looping')
    
colours = ['blue', 'purple', 'green', 'red']
for colour in colours:
    print(colour)
    
point = (1, 2, 3)
for value in point:
    print(value)

ages ={'kevin': 59, 'bob': 23,  "sade": 26}
for key in ages:
    print(key, value)
    
for letter in 'my_string':
    print(letter)
    
colours = ['red', 'green', 'gold', 'yellow']
uppercase_colours = []
for colour in colours:
    uppercase_colours.append(colour.upper())
    print(uppercase_colours)