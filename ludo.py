from selectors import SelectSelector
import ludo_f
from ludo_f import choose_token

board_view = [['▔','▔','▔','▔'] for _ in range(92)]
game = {
    'p_tokens':{'red':[1,2,3,4],'green':[1,2,3,4],'yellow':[1,2,3,4],'blue':[1,2,3,4]},
    'p_tokens_win':{'red':{'1':False,'2':False,'3':False,'4':False},'yellow':{'1':False,'2':False,'3':False,'4':False}},
    'p_tokens_pos':{'red':{'1':-1,'2':-1,'3':-1,'4':-1},
                    'yellow':{'1':-1,'2':-1,'3':-1,'4':-1}
                    },
    'tokens_kill':{'yellow':False,'red':False},
    'main_path':{'yellow':[26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,
                   50,57,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,64,65,66,67,68,69],
                 'red':[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,
                        27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56]},
    'yard_path':{'red':[76,77,78,79],'yellow':[84,85,86,87]}
}
print(f'                               Welcome to ludo')
while True:
    print('Press 1 for one vs one')
    print('Press 2 for exit')
    choice=input('')
    if choice in ['1','2']:
        break
    else:
        print("Invalid choice!")
choice=int(choice)
if choice == 1:
    player_1 = input('Enter Player 1 Name:')
    player_2 = input('Enter Player 2 Name:')
    player_1 =f'\033[91m{player_1}\033[0m'
    player_2 = f'\033[93m{player_2}\033[0m'
    print(f'{player_1} gets the red block, and {player_2} gets the yellow block.”')
    print('Players have four tokens(1,2,3,4)')
    ludo_f.print_dashboard(board_view)
    while True:
        found =False
        while True:
            value = ludo_f.player_move(board_view, game, ludo_f.player_turn(player_1), 'red')
            count = 0
            lst = ['1', '2', '3', '4']
            for i in lst:
                if game['p_tokens_win']['red'][i]:
                    count += 1
            if count == 4:
                print(f'Congratulation {player_1} you win.')
                found=True
                break
            if not value:
                break
        if found:
            break
        print('_____________________________________________________________')
        print('_____________________________________________________________')
        while True:
            found=False
            ludo_f.player_move(board_view, game, ludo_f.player_turn(player_2), 'yellow')
            count = 0
            lst = ['1', '2', '3', '4']
            for i in lst:
                if game['p_tokens_win']['yellow'][i]:
                    count += 1
            if count == 4:
                found=True
                print(f'Congratulation {player_2} you win.')
                break
            if not value:
                break
        if found:
            break
        print('_____________________________________________________________')
        print('_____________________________________________________________')

