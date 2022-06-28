# 3.1 put names of friends ina  list and then access them 
# each at a time

friends = ['Bruce',
        'James',
        'Thomas',
        'Jimmy',
        'Oliver',
        'Michael',
        'Matthew']

# pythonic
'''for i in friends:
        print(i)'''
# same thing
'''for i in range(len(friends)):
        print(friends[i])'''

# 3.2 greetings, presenting to each person the same mesage with apresentar a cada pessoa a mesma mensagem com
# the custom name of each person
def ms_friends(name):
        message = 'Hi, ' + name + ' how are you? \
                        \nLog time no see, I only want to say that for me you are my best friend.\
                        \n I will never forgt you'  + name + '.'
        return print(message)

for i in friends:       
        ms_friends(i)

