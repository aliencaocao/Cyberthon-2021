import requests

HOST = 'aiodmb3uswokssp2pp7eum8qwcsdf52r.ctf.sg:50501'
ENDPOINTS = {
        'init': f'http://{HOST}/init',
        'buy': f'http://{HOST}/buy'
    }

balance = 0
shop = {}


def cls():
    print('\033[2J\033[H')

def menu():
    cls()
    print(' ________                                __       __                        __     ')
    print('/        |                              /  \     /  |                      /  |    ')
    print('$$$$$$$$/   ______    ______    ______  $$  \   /$$ |  ______    ______   _$$ |_   ')
    print('    /$$/   /      \  /      \  /      \ $$$  \ /$$$ | /      \  /      \ / $$   |  ')
    print('   /$$/   /$$$$$$  |/$$$$$$  |/$$$$$$  |$$$$  /$$$$ | $$$$$$  |/$$$$$$  |$$$$$$/   ')
    print('  /$$/    $$    $$ |$$ |  $$/ $$ |  $$ |$$ $$ $$/$$ | /    $$ |$$ |  $$/   $$ | __ ')
    print(' /$$/____ $$$$$$$$/ $$ |      $$ \__$$ |$$ |$$$/ $$ |/$$$$$$$ |$$ |        $$ |/  |')
    print('/$$      |$$       |$$ |      $$    $$/ $$ | $/  $$ |$$    $$ |$$ |        $$  $$/ ')
    print('$$$$$$$$/  $$$$$$$/ $$/        $$$$$$/  $$/      $$/  $$$$$$$/ $$/          $$$$/  ')
    print('')
    print('-----------------------------------------------------------------------------------')
    print(f' Credits: {balance}')
    print('-----------------------------------------------------------------------------------')

    for k, v in shop.items():
        print(f'{k} ({v} Credits)')

    print('-----------------------------------------------------------------------------------')
    print('P.S: Type \'Exit\' to leave')
    print('-----------------------------------------------------------------------------------')
    print('')

print('[+] Loading Store...')

session = requests.Session()
r = session.get(ENDPOINTS['init'])

if r.status_code == 200:
    balance = r.json()['balance']
    shop = r.json()['shop']
else:
    print('[-] Error: Cannot connect to ZeroMart!')
    exit(0)

while True:
    menu()
    choice = input('Choice: ')

    if choice == 'Exit':
        print('KTHXBAI!')
        exit(0)

    if choice not in shop.keys():
        print(f'[-] Invalid option: {choice}')
        input('Press Enter to continue...')
        continue

    r = session.post(ENDPOINTS['buy'], json={'item': choice})

    if r.status_code != 200:
        print('[-] Error: Cannot connect to ZeroMart!')
        exit(0)

    print(f"[+] {r.json()['message']}")

    if 'balance' in r.json().keys():
        balance = r.json()['balance']

    input('Press Enter to continue...')
