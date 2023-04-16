import requests, time
class checker:
    def __init__(self):
        self.available = 0
        self.checked = []

    def checkers(self):
        print("Discord Server: https://discord.gg/tmV3XpxkFJ")
        while True:
            self.username = open('usernames.txt').read().splitlines()
            for user in self.username:
                if user not in self.checked:
                    self.checked.append(user)
                    headers = {
                        'Accept': 'application/json, text/plain, */*',
                        'Accept-Language': 'nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7',
                        'Connection': 'keep-alive',
                        'Content-Type': 'application/json',
                        'MS-CV': 'w95xWjtg87wn3VeLdDxvYP.0',
                        'Origin': 'https://social.xbox.com',
                        'Referer': 'https://social.xbox.com/',
                        'Sec-Fetch-Dest': 'empty',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'cross-site',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
                        'authorization': '',# Paste Xbox Token Between ' and '
                        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'x-xbl-contract-version': '1',
                    }
    
                    json_data = {
                        'gamertag': user,
                        'reservationId': '2535457390568685',
                        'targetGamertagFields': 'gamertag',
                    }
                    try:
                        response = requests.post('https://gamertag.xboxlive.com/gamertags/reserve', headers=headers, json=json_data)
                        if response.json()['classicGamertag'] == user:
                            print(f"{user} Available")
                        elif response.json()['classicGamertag'] != user:
                            print(f"{user} Invalid")
                        else:
                            print("Ratelimited")
                    except Exception as e:
                        print(e)
            else:
                print("exiting in 10 seconds...")
                time.sleep(10)
                exit()
checker().checkers()

