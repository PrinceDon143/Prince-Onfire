import requests
import sys
import os
import time
from platform import system

def liness():
    print('\u001b[37m' +
          '---------------------------------------------------')

def send_comments():
    os.system('clear')

    # Stylish colored logo
    logo = '''
                                
                         \u001b[32m@@@@@@@    @@@@@@    @@@@@@   @@@@@@@  
                         \u001b[32m@@@@@@@@  @@@@@@@@  @@@@@@@   @@@@@@@  
                         \u001b[32m@@!  @@@  @@!  @@@  !@@         @@!    
                         \u001b[32m!@!  @!@  !@!  @!@  !@!         !@!    
                         \u001b[32m@!@@!@!   @!@  !@!  !!@@!!      @!!    
                         \u001b[32m!!@!!!    !@!  !!!   !!@!!!     !!!    
                         \u001b[32m!!:       !!:  !!!       !:!    !!:    
                         \u001b[32m:!:       :!:  !:!      !:!     :!:    
                         \u001b[32m ::       ::::: ::  :::: ::      ::    
                         \u001b[32m :         : :  :   :: : :       :     
                                                                                                                                                      Author :: Bholwa
                                '''

    print(logo.center(os.get_terminal_size().columns))

    # Rest of the code follows...    

    # Manually set the password
    password = "Prince"

    entered_password = input("\u001b[33m" + "Enter password: ").strip()

    # Check if entered password matches the one provided
    if password != entered_password:
        print('\u001b[31m' + '[-] <==> Incorrect Password!')
        sys.exit()

    # Read tokens from file
    token_file_path = input("\u001b[33m" + "Enter Token file path: ").strip()
    with open(token_file_path, 'r') as file:
        tokens = file.readlines()
    num_tokens = len(tokens)

    requests.packages.urllib3.disable_warnings()

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }

    # Password check
    if password != entered_password:
        print('\u001b[31m' + '[-] <==> Incorrect Password!')
        sys.exit()

    access_tokens = [token.strip() for token in tokens]

    # Prompt the user to enter post ID
    post_id = input("\u001b[33m" + "Enter post ID: ").strip()

    # Prompt the user to enter text file path
    comment_file_path = input("\u001b[33m" + "Enter comment file path: ").strip()

    with open(comment_file_path, 'r') as file:
        comments = file.readlines()

    num_comments = len(comments)
    max_tokens = min(num_tokens, num_comments)

    # Prompt the user to enter speed
    speed = int(input("\u001b[33m" + "Enter speed (in seconds): ").strip())

    liness()

    while True:
        try:
            for token_index, access_token in enumerate(access_tokens, start=1):
                profile_name = f"Profile {token_index}"
                # Check login status of the access token
                check_url = "https://graph.facebook.com/v15.0/me?access_token=" + access_token
                check_response = requests.get(check_url)
                if check_response.ok:
                    profile_data = check_response.json()
                    account_name = profile_data.get("name", "Unknown")
                    print(f"\u001b[32m[+] {account_name} ({profile_name}) login status: Active")
                else:
                    print(f"\u001b[31m[x] {profile_name} login status: Inactive")
            liness()  # This line should be inside the try block
            for comment_index in range(num_comments):
                token_index = comment_index % max_tokens
                access_token = access_tokens[token_index]
                # Rest of your code for sending comments

                comment = comments[comment_index].strip()

                url = f"https://graph.facebook.com/{post_id}/comments"
                parameters = {'access_token': access_token,
                              'message': comment}
                response = requests.post(url, json=parameters, headers=headers)

                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                profile_name = f"Profile {token_index + 1}"
                if response.ok:
                    print("\u001b[32m" + "[+] Comment {} on Post {} sent by {}: {}".format(
                        comment_index + 1, post_id, profile_name, comment))
                    print("\u001b[32m" + "  - Time: {}".format(current_time))
                    liness()
                else:
                    print("\u001b[31m" + "[x] Failed to send comment {} on Post {} with {}: {}".format(
                        comment_index + 1, post_id, profile_name, comment))
                    print("\u001b[31m" + "  - Time: {}".format(current_time))
                    liness()
                time.sleep(speed)

            print("\n\u001b[32m" + "[+] All comments sent. Restarting the process...\n")
        except Exception as e:
            print("\u001b[31m" + "[!] An error occurred: {}".format(e))

def Subscraption():
    os.system('git pull')
    time.sleep(1)
    uuid = str(os.geteuid())+"#"+str(os.geteuid())
    id = "Premium-Tool-"+"".join(uuid)
    os.system('clear')

    # Stylish colored logo
    logo = '''
                                
                   \u001b[32m@@@@@@@   @@@  @@@   @@@@@@   @@@       @@@  @@@  @@@   @@@@@@   
                   \u001b[32m@@@@@@@@  @@@  @@@  @@@@@@@@  @@@       @@@  @@@  @@@  @@@@@@@@  
                   \u001b[32m@@!  @@@  @@!  @@@  @@!  @@@  @@!       @@!  @@!  @@!  @@!  @@@  
                   \u001b[32m!@   @!@  !@!  @!@  !@!  @!@  !@!       !@!  !@!  !@!  !@!  @!@  
                   \u001b[32m@!@!@!@   @!@!@!@!  @!@  !@!  @!!       @!!  !!@  @!@  @!@!@!@!  
                   \u001b[32m!!!@!!!!  !!!@!!!!  !@!  !!!  !!!       !@!  !!!  !@!  !!!@!!!!  
                   \u001b[32m!!:  !!!  !!:  !!!  !!:  !!!  !!:       !!:  !!:  !!:  !!:  !!!  
                   \u001b[32m:!:  !:!  :!:  !:!  :!:  !:!   :!:      :!:  :!:  :!:  :!:  !:!  
                   \u001b[32m :: ::::  ::   :::  ::::: ::   :: ::::   :::: :: :::   ::   :::  
                   \u001b[32m:: : ::    :   : :   : :  :   : :: : :    :: :  : :     :   : :  
                                                                                                                                                      Author :: Prince
                                '''

    print(logo.center(os.get_terminal_size().columns))

    print("\033[1;39m You Get Approved for Using Command  Paid Tool \033[1;37m")
    print("\n\033[1;39m Your Key :\u001b[36m "+id);time.sleep(0.1)
    print ('\u001b[37m' +
          '---------------------------------------------------')
    try:
        httpCaht = requests.get("https://prince88000ueu.blogspot.com/2024/04/post-convo-toll.html").text
        if id in httpCaht:
            print("\n\033[1;39m Congrats You get approved successful And Enjoy")
            msg = str(os.geteuid())
            time.sleep(1)
            pass
        else: 
            print("\n\033[1;39m Your Key Not approved please  Say to Admin")
            time.sleep(0.1)
            input('\n\nTool Ka Approval Lene Ke Liye Owner Ko Key Send Kro')
            tks = ('Hello%20prince%20Sir%20!%20Please%20Approve%20My%20Key%20!That%20My%20Key%20:%20'+id)
            os.system('am start https://wa.me/+994409445548?text='+tks), Subscraption()
            time.sleep(1)
            exit()
    except Exception as e:
        print(e)
        time.sleep(2)
        Subscraption()
    except:
        sys.exit()

def Prince():
    Subscraption()  # Move the subscription process to the beginning
    os.system('clear')  # Indent this line to be inside the bholwa() function
    print(logo)
    print(f'\033[1;92m[1] Convo Tool ')
    print(f'\033[1;92m[2] Post Tool ')
    print("-------------------------------------------")
    abhii = input('\033[1;92m Choose Option : ')
    if abhii =='1':
        os.system('cd && git clone https://github.com/PrinceDon143/Prince-Onfire')
        os.system('rm -rf Prince-Onfire;cd && cd Prince-Onfire;git pull;python PrinceFire.py')
    elif abhii =='2':
        send_comments()

if __name__ == '__main__':
    logo = '''
                                
                   \u001b[32m@@@@@@@   @@@  @@@   @@@@@@   @@@       @@@  @@@  @@@   @@@@@@   
                   \u001b[32m@@@@@@@@  @@@  @@@  @@@@@@@@  @@@       @@@  @@@  @@@  @@@@@@@@  
                   \u001b[32m@@!  @@@  @@!  @@@  @@!  @@@  @@!       @@!  @@!  @@!  @@!  @@@  
                   \u001b[32m!@   @!@  !@!  @!@  !@!  @!@  !@!       !@!  !@!  !@!  !@!  @!@  
                   \u001b[32m@!@!@!@   @!@!@!@!  @!@  !@!  @!!       @!!  !!@  @!@  @!@!@!@!  
                   \u001b[32m!!!@!!!!  !!!@!!!!  !@!  !!!  !!!       !@!  !!!  !@!  !!!@!!!!  
                   \u001b[32m!!:  !!!  !!:  !!!  !!:  !!!  !!:       !!:  !!:  !!:  !!:  !!!  
                   \u001b[32m:!:  !:!  :!:  !:!  :!:  !:!   :!:      :!:  :!:  :!:  :!:  !:!  
                   \u001b[32m :: ::::  ::   :::  ::::: ::   :: ::::   :::: :: :::   ::   :::  
                   \u001b[32m:: : ::    :   : :   : :  :   : :: : :    :: :  : :     :   : :  
                                                                                                                                                      Author :: Prince
                                '''
    Prince()
