from turtledemo.clock import current_day

from urllib3.util.util import to_str


# =========================
# DASHBOARD DISPLAY
# =========================

def print_dashboard(o_board):
    red,green,yellow,blue,reset = (
        '\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[0m'
    )
    board=o_board.copy()
    for i in range(92):
        if not board[i][2]:
            continue
        board[i] = ''.join(board[i]).ljust(4)
    for index in range(92):

        if index in [0, 9, 13, 22, 26, 35, 39, 48] and board[index] == '▔▔▔▔':
            board[index] = '▓▓▓▓'

        if index in [56, 63, 69, 75] and board[index] == '▔▔▔▔':
            board[index] = '    '

        if index in [76, 77, 78, 79] and board[index] == '▔▔▔▔':
            board[index] = '1'

        if index in [80, 81, 82, 83] and board[index] == '▔▔▔▔':
            board[index] = '2'

        if index in [84, 85, 86, 87] and board[index] == '▔▔▔▔':
            board[index] = '3'

        if index in [88, 89, 90, 91] and board[index] == '▔▔▔▔':
            board[index] = '4'

    print(f'{red}╔══════════════R══════════════╦{reset}══════════════{green}╦═══════════════G═════════════╗{reset}')
    print(f'{red}║   ●      ●      ●     ●     ║{reset}{board[10]}|{board[11]}|{board[12]}{green}║   ●      ●      ●     ●     ║{reset}')
    print(f'{red}║   ●      ●      ●     ●     ║{reset}{board[9]}{green}|{board[58]}|{board[13]}║   ●      ●      ●     ●     ║{reset}')
    print(f'{red}║   ●      ●      ●     ●     ║{reset}{board[8]}{green}|{board[59]}|{reset}{board[14]}{green}║   ●      ●      ●     ●     ║{reset}')
    print(f'{red}║   ●      ●      ●     ●     ║{reset}{board[7]}{green}|{board[60]}|{reset}{board[15]}{green}║   ●      ●      ●     ●     ║{reset}')
    print(f'{red}║   ●      ●      ●     ●     ║{reset}{board[6]}{green}|{board[61]}|{reset}{board[16]}{green}║   ●      ●      ●     ●     ║{reset}')
    print(f'{red}║   {board[76][0]}      {board[77][0]}      {board[78][0]}     {board[79][0]}     ║{reset}{board[5]}{green}|{board[62]}|{reset}{board[17]}{green}║   {board[80]}      {board[81]}      {board[82]}     {board[83]}     ║{reset}')
    print(f'{red}║═════════════════════════════╬{reset}════{green}══════{reset}════{green}╬═════════════════════════════║{reset}')

    print(f'║{board[57]}{red}|{board[0]}|{reset}{board[1]}|{board[2]}|{board[3]}|{board[4]}║     {board[63]}     ║{board[18]}|{board[19]}|{board[20]}|{board[21]}|{board[22]}|{board[23]}║')
    print(f'║{board[50]}{red}|{board[51]}|{board[52]}|{board[53]}|{board[54]}|{board[55]}║{reset}{board[56]}      {board[69]}{yellow}║{board[68]}|{board[67]}|{board[66]}|{board[65]}|{board[64]}|{reset}{board[24]}║')
    print(f'║{board[49]}{red}|{board[48]}|{board[47]}{reset}|{red}{board[46]}{reset}|{red}{board[45]}{reset}|{red}{board[44]}{reset}║     {board[75]}     ║{yellow}{board[30]}{reset}|{yellow}{board[29]}{reset}|{yellow}{board[28]}{reset}|{yellow}{board[27]}{reset}{yellow}|{board[26]}|{reset}{board[25]}║')

    print(f'{blue}║═════════════════════════════╬{reset}════{yellow}══════{reset}════{yellow}╬═════════════════════════════║{reset}')
    print(f'{blue}║   ●      ●      ●     ●     ║{reset}{board[43]}{blue}|{board[74]}|{reset}{board[31]}{yellow}║   ●      ●      ●     ●     ║{reset}')
    print(f'{blue}║   ●      ●      ●     ●     ║{reset}{board[42]}{blue}|{board[73]}|{reset}{board[32]}{yellow}║   ●      ●      ●     ●     ║{reset}')
    print(f'{blue}║   ●      ●      ●     ●     ║{reset}{board[41]}{blue}|{board[72]}|{reset}{board[33]}{yellow}║   ●      ●      ●     ●     ║{reset}')
    print(f'{blue}║   ●      ●      ●     ●     ║{reset}{board[40]}{blue}|{board[71]}|{reset}{board[34]}{yellow}║   ●      ●      ●     ●     ║{reset}')
    print(f'{blue}║   ●      ●      ●     ●     ║{board[39]}|{board[70]}|{reset}{board[35]}{yellow}║   ●      ●      ●     ●     ║{reset}')
    print(f'{blue}║   {board[88]}      {board[89]}      {board[90]}     {board[91]}     ║{reset}{board[38]}|{board[37]}|{board[36]}{yellow}║   {board[84][0]}      {board[85][0]}      {board[86][0]}     {board[87][0]}     ║{reset}')

    print(f'{blue}╚═════════════B═══════════════╩{reset}══════════════{yellow}╩══════════════Y══════════════╝{reset}')


# =========================
# BOARD UPDATE
# =========================

def update_dashboard(p_board, new_pos, old_pos, token, is_new_token=False, color=None):
    token_display = str(token)
    if color == 'red':
        token_display = f'\033[91m{token_display}\033[0m'
    else:
        token_display = f'\033[93m{token_display}\033[0m'
    if is_new_token:
        if p_board[old_pos][0] in ['▔', ' ']:
            p_board[old_pos]=[' ',None,None,None]
        for i in range(4):
            if p_board[new_pos][i]=='▔':
                p_board[new_pos][i]=token_display
                break
    else:
        found= False
        for i in range(4):
            if p_board[old_pos][i]==token_display:
                p_board[old_pos][i]='▔'
                break
        for i in range(4):
            if p_board[new_pos][i]=='▔':
                p_board[new_pos][i]=token_display
                found=True
                break
        if not found:
            print("New position is full!")
    print_dashboard(p_board)
# =========================
# VALIDATION
# =========================

def is_token_won(game, token,color):
    return game['p_tokens_win'][color][token]
def is_token_on_board(game, token,color):
    return not game['p_tokens'][color].count(int(token)) > 0
def is_token_in_home(game,token,color):
    return game['p_tokens'][color].count(int(token)) > 0
def all_token_on_board(game,color):
    return not game['p_tokens'][color] == []
def no_token_to_move(game,color):
    compute_len = len(game['p_tokens'][color])
    if compute_len == 4:
        return False
    else:
        count = 0
        for key ,val in game['p_tokens_win'][color].items():
            if val:
                count=count+1
        if count+compute_len==4:
            return False
    return True

def validate_input(game, choice,color):
    if choice.lower() == 'no':
        return False
    elif choice not in ['1', '2', '3', '4']:
        print('Invalid Input')
        return True
    elif is_token_won(game, choice,color):
        print('Token Win Select Another Token.')
        return True
    return False

def check_token_killing(board, game,new_pos, color,token1):
    if new_pos in [0, 9, 13, 22, 26, 35, 39, 48]:
        return False
    if color == 'red':
        yellow_list= [f'\033[93m{1}\033[0m',f'\033[93m{2}\033[0m',f'\033[93m{3}\033[0m',f'\033[93m{4}\033[0m']
        for i in range(4):
           if board[new_pos][i] in yellow_list:
               token=board[new_pos][i]
               yard_positions = game['yard_path']['yellow']
               for pos in yard_positions:
                   if board[pos][0] == '▔':
                       board[pos][0] = token
                       break
               board[new_pos][i]='▔'
               killed_token = int(token.replace('\033[93m', '').replace('\033[0m', ''))
               if killed_token not in game['p_tokens']['yellow']:
                   game['p_tokens']['yellow'].append(killed_token)
               game['p_tokens_pos']['yellow'][str(killed_token)] = -1
               print(f'Player \033[91m Red \033[0m  kill Player \033[93m Yellow \033[0m  token')
               game['tokens_kill']['red']=True
               return True
        return False
    else:
        red_list= [f'\033[91m{1}\033[0m', f'\033[91m{2}\033[0m', f'\033[91m{3}\033[0m', f'\033[91m{4}\033[0m']
        for i in range(4):
            if board[new_pos][i] in red_list:
                token = board[new_pos][i]
                yard_positions = game['yard_path']['red']
                for pos in yard_positions:
                    if board[pos][0] == '▔':
                        board[pos][0] = token
                        break
                board[new_pos][i] ='▔'
                killed_token = int(token.replace('\033[91m', '').replace('\033[0m', ''))
                if killed_token not in game['p_tokens']['red']:
                    game['p_tokens']['red'].append(killed_token)
                game['p_tokens_pos']['red'][str(killed_token)] = -1
                game['tokens_kill']['yellow']=True
                print(f'Player \033[93m Yellow \033[0m  kill Player \033[91m Red \033[0m  token')
                return True
    return False
# =========================
# TOKEN MOVEMENT
# =========================

def move_red_token(board_view, game, steps, token, add_new):
    token_str = str(token)
    prev = game['p_tokens_pos']['red'][token_str]
    new = prev + steps
    if add_new:
        game['p_tokens_pos']['red'][token_str] = 0
        game['p_tokens']['red'].remove(int(token))
        old_pos = game['yard_path']['red'][int(token) - 1]
        new_pos = game['main_path']['red'][0]
        update_dashboard(board_view, new_pos, old_pos, token, True, 'red')
        return False
    elif 0 <= new <= 56:
        if new <= 50:
            game['p_tokens_pos']['red'][token_str] = new
            prev = game['main_path']['red'][prev]
            new_pos = game['main_path']['red'][new]
            if check_token_killing(board_view, game, new_pos, 'red', token):
                update_dashboard(board_view, new_pos, prev, token, False, 'red')
                return True
            update_dashboard(board_view, new_pos, prev, token, False, 'red')
            return False
        elif new <= 56 and game['tokens_kill']['red']:
            game['p_tokens_pos']['red'][token_str] = new
            prev = game['main_path']['red'][prev]
            new_pos = game['main_path']['red'][new]
            if new == 56:
                game['p_tokens_win']['red'][token_str] = True
                update_dashboard(board_view, new_pos, prev, token, False, 'red')
                return True
            update_dashboard(board_view, new_pos, prev, token, False, 'red')
            return False
        else:
            print("Invalid move: not enough blocks remaining.")

def move_yellow_token(board_view, game, steps, token, add_new):
    token_str=str(token)
    prev=game['p_tokens_pos']['yellow'][token_str]
    new=prev+steps
    if add_new:
        game['p_tokens_pos']['yellow'][token_str]=0
        game['p_tokens']['yellow'].remove(int(token))
        old_pos=game['yard_path']['yellow'][int(token)-1]
        new_pos=game['main_path']['yellow'][0]
        update_dashboard(board_view,new_pos, old_pos,token,True,'yellow')
        return False
    elif 0<=new<=56:
        if new <=50:
            game['p_tokens_pos']['yellow'][token_str] = new
            prev = game['main_path']['yellow'][prev]
            new_pos = game['main_path']['yellow'][new]
            if  check_token_killing(board_view,game,new_pos,'yellow',token):
                update_dashboard(board_view, new_pos, prev, token, False, 'yellow')
                return True
            update_dashboard(board_view, new_pos, prev, token, False, 'yellow')
            return False

        elif new<=56 and game['tokens_kill']['yellow']:
            game['p_tokens_pos']['yellow'][token_str] = new
            prev = game['main_path']['yellow'][prev]
            new_pos = game['main_path']['yellow'][new]
            if new == 56:
                update_dashboard(board_view, new_pos, prev, token, False, 'yellow')
                game['p_tokens_win']['yellow'][token_str] = True
                return True
            update_dashboard(board_view, new_pos, prev, token, False, 'yellow')
            return False
        else:
            print("Invalid move: not enough blocks remaining.")
            return -1
def choose_token(game, dice, color):
    result = [False, -1]

    if dice == 6 and all_token_on_board(game,color):
        while True:
            choice = input('Which new token do you want to insert? (No for None): ')
            if choice.lower() == 'no':
                while True:
                    token = input('Which token do you want to move? ')
                    if validate_input(game, token, color):
                        continue
                    elif is_token_in_home(game,token,color):
                        print('Token In Home.')
                        continue
                    result = [False, int(token)]
                    return result
            elif validate_input(game, choice,color):
                continue
            elif is_token_on_board(game, choice,color):
                print('Token Already On Board.')
                continue
            else:
                result = [True, int(choice)]
                return result

    elif len(game['p_tokens'][color]) < 4 and no_token_to_move(game,color):
        while True:
            token = input('Which token do you want to move? ')
            if validate_input(game, token,color):
                continue
            elif is_token_in_home(game,token,color):
                print('Token In Home.')
                continue
            result = [False, int(token)]
            return result

    return result

def player_move(board_view, game, dice_list, color):
    rep_or_not=False
    while True:
        for dice in dice_list:
            add_new, token = choose_token(game, dice, color)
            if token == -1:
                return False
            if color == 'red':
                rep_or_not = move_red_token(board_view, game, dice, token, add_new)
            else:
                rep_or_not = move_yellow_token(board_view, game, dice, token, add_new)
        if rep_or_not == -1:
            continue
        if rep_or_not:
            return True
        else:
            return False
    return False

def player_turn(player):
    import random
    import time
    moves = []
    while True:
        input(f"=== {player}'s Turn ===\nPress Enter to roll the dice...")
        print('Loading...', end='', flush=True)

        roll = random.randint(1, 6)
        time.sleep(0.5)
        print(f'   {roll}')
        moves.append(roll)
        if moves.count(6)==3:
            print('Move declared.')
            return []
        if roll != 6:
            return moves