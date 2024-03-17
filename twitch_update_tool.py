import time
import requests
from datetime import datetime

hp1_id = 539
hp2_id = 7665
hp3_id = 3470
hp4_id = 16893
hp5_id = 11074
hp6_id = 20646
hp71_id = 28415
hp72_id = 29000

hp1 = ["HP1PS1", "HP1PC"]
hp2 = ["HP2PS1", "HP2PC100", "HP2PCEXT"]
hp3 = ["HP3GBA", "HP3PC"]
hp4 = ["HP4GBA", "HP4PC"]
hp5 = ["HP5PC"]
hp6 = ["HP6PC"]
hp71 = ["HP71PC"]
hp72 = ["HP72PC"]

refresh_intervall = 15

all_hp_strings = [hp1, hp2, hp3, hp4, hp5, hp6, hp71, hp72]

new_title = "[🔴LIVE 24/7] Harry Potter TV ⚡ Relax, Sleep, Work, Study with Harry 🧙 !info !discord !gamelist⚡ @oldschoolpotter"
new_game_category = None
current_game_category = None

filePathSecrets = "C:/Users/Administrator/Desktop/Ressourcen/twitchsecrets.txt" 
#line1 = client_id
#line2 = secret_token
twitchSecrets = []

filePathTuna = "C:/Users/Administrator/Desktop/Ressourcen/tuna_output.txt"
textTuna = None

with open(filePathSecrets) as file:
    twitchSecrets = file.read().splitlines()

client_id = twitchSecrets[0]
access_token = twitchSecrets[1]
channel_name = 'oldschoolpotter'

url = f'https://api.twitch.tv/helix/streams?user_login={channel_name}'

headers = {
        'Client-ID': client_id,
        'Authorization': f'Bearer {access_token}'
}

def showData():
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print(f'Alle Daten: {data}')

    else:
        print("Fehler beim Abrufen der Kanalinformationen.")

def getCurrentCategoryID():
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        current_title = data#['data'][0]['title']
        #print(data)
        if len(data['data']) >= 1:
            current_game_category1 = data['data'][0]['game_id']
            
            print("Stream is online. Data found!")
            print("Current Game Category ID: " + str(current_game_category1))
            #return current_game_category1
            return data['data'][0]['game_id']
        else:
            print("Stream is offline. Can't find Data.")
    else:
        print("Fehler beim Abrufen der Kanalinformationen.")

def changeTitle(newTitle):
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        current_title = data#['data'][0]['title']
        current_id = data['data'][0]['user_id']
        current_title = data['data'][0]['title']
        #print(f'Aktueller Titel des Streams: {current_title}')
        #print(f'Broadcaster ID: {current_id}')
        
        update_url = f'https://api.twitch.tv/helix/channels?user_login={channel_name}'

        update_data = {
            'broadcaster_id': current_id,
            'title': newTitle
        }

        update_response = requests.patch(update_url, json=update_data, headers=headers)

    else:
        print("Fehler beim Abrufen der Kanalinformationen.")

def changeGameCategory(newGameCategory):
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        current_title = data#['data'][0]['title']
        current_id = data['data'][0]['user_id']
        current_game = data['data'][0]['game_id']
        #print(f'Aktueller Titel des Streams: {current_title}')
        #print(f'Broadcaster ID: {current_id}')
        
        update_url = f'https://api.twitch.tv/helix/channels?user_login={channel_name}'

        update_data = {
            'broadcaster_id': current_id,
            'game_id': newGameCategory
        }

        update_response = requests.patch(update_url, json=update_data, headers=headers)

    else:
        print("Fehler beim Abrufen der Kanalinformationen.")


def checkTunaTextFileAndChangeCategory():
    while True:

        with open(filePathTuna) as file:
            textTuna = file.read().splitlines()

        print("Tuna Text: " + textTuna[0])

        for hpArrayToCompare in all_hp_strings: #get all arrays inside all_hp_strings

            for hpStringToCompare in hpArrayToCompare: #get all items from current array to get the string
                #print(hpStringToCompare)

                for game in hp1:
                    if hpStringToCompare == game and textTuna[0] == game:
                        if str(getCurrentCategoryID()) != str(hp1_id):
                            print("Changing to HP1...\n")
                            new_game_category = hp1_id
                            newTitle = "[🔴LIVE 24/7] Harry Potter TV ⚡ Now: Harry Potter 1 ⚡ Relax, Sleep, Work, Study with Harry 🧙"
                            changeGameCategory(new_game_category)
                            changeTitle(newTitle)
                            print("Changed to HP1\n")
                        else:
                            print("Already Changed to HP1\n")
                        

                for game in hp2:
                    if hpStringToCompare == game and textTuna[0] == game:
                        if str(getCurrentCategoryID()) != str(hp2_id):
                            print("Changing to HP2...\n")
                            new_game_category = hp2_id
                            newTitle = "[🔴LIVE 24/7] Harry Potter TV ⚡ Now: Harry Potter 2 ⚡ Relax, Sleep, Work, Study with Harry 🧙"
                            changeGameCategory(new_game_category)
                            changeTitle(newTitle)
                            print("Changed to HP2\n")
                        else:
                            print("Already Changed to HP2\n")

                for game in hp3:
                    if hpStringToCompare == game and textTuna[0] == game:
                        if str(getCurrentCategoryID()) != str(hp3_id):
                            print("Changing to HP3...\n")
                            new_game_category = hp3_id
                            newTitle = "[🔴LIVE 24/7] Harry Potter TV ⚡ Now: Harry Potter 3 ⚡ Relax, Sleep, Work, Study with Harry 🧙"
                            changeGameCategory(new_game_category)
                            changeTitle(newTitle)
                            print("Changed to HP3\n")
                        else:
                            print("Already Changed to HP3\n")

                for game in hp4:
                    if hpStringToCompare == game and textTuna[0] == game:
                        if str(getCurrentCategoryID()) != str(hp4_id):
                            print("Changing to HP4...\n")
                            new_game_category = hp4_id
                            newTitle = "[🔴LIVE 24/7] Harry Potter TV ⚡ Now: Harry Potter 4 ⚡ Relax, Sleep, Work, Study with Harry 🧙"
                            changeGameCategory(new_game_category)
                            changeTitle(newTitle)
                            print("Changed to HP4\n")
                        else:
                            print("Already Changed to HP4\n")

                for game in hp5:
                    if hpStringToCompare == game and textTuna[0] == game:
                        if str(getCurrentCategoryID()) != str(hp5_id):
                            print("Changing to HP5...\n")
                            new_game_category = hp5_id
                            newTitle = "[🔴LIVE 24/7] Harry Potter TV ⚡ Now: Harry Potter 5 ⚡ Relax, Sleep, Work, Study with Harry 🧙"
                            changeGameCategory(new_game_category)
                            changeTitle(newTitle)
                            print("Changed to HP5\n")
                        else:
                            print("Already Changed to HP5\n")
                
                for game in hp6:
                    if hpStringToCompare == game and textTuna[0] == game:
                        if str(getCurrentCategoryID()) != str(hp6_id):
                            print("Changing to HP6...\n")
                            new_game_category = hp6_id
                            newTitle = "[🔴LIVE 24/7] Harry Potter TV ⚡ Now: Harry Potter 6 ⚡ Relax, Sleep, Work, Study with Harry 🧙"
                            changeGameCategory(new_game_category)
                            changeTitle(newTitle)
                            print("Changed to HP6\n")

                        else:
                            print("Already Changed to HP6\n")

                for game in hp71:
                    if hpStringToCompare == game and textTuna[0] == game:
                        if str(getCurrentCategoryID()) != str(hp71_id):
                            print("Changing to HP7.1...\n")
                            print("    " + str(getCurrentCategoryID()))
                            print("    " + str(hp71_id))
                            new_game_category = hp71_id
                            newTitle = "[🔴LIVE 24/7] Harry Potter TV ⚡ Now: Harry Potter 7.1 ⚡ Relax, Sleep, Work, Study with Harry 🧙"
                            changeGameCategory(new_game_category)
                            changeTitle(newTitle)
                            print("Changed to HP7.1\n")

                        else:
                            print("Already Changed to HP7.1\n")

                for game in hp72:
                    if hpStringToCompare == game and textTuna[0] == game:
                        if str(getCurrentCategoryID()) != str(hp72_id):
                            print("Changing to HP7.2...\n")
                            new_game_category = hp72_id
                            newTitle = "[🔴LIVE 24/7] Harry Potter TV ⚡ Now: Harry Potter 7.2 ⚡ Relax, Sleep, Work, Study with Harry 🧙"
                            changeGameCategory(new_game_category)
                            changeTitle(newTitle)
                            print("Changed to HP7.2\n")
                        else:
                            print("Already Changed to HP7.2\n")
        
        now = datetime.now()
        print(now.strftime("%d/%m/%Y %H:%M:%S"))
        print("---------------------------")
        #print(current_game_category)
        #print(new_game_category)

        time.sleep(refresh_intervall) #wait for refresh_intervall till continue loop

checkTunaTextFileAndChangeCategory() #start loop