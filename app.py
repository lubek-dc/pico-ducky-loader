#Scripts:
#RickRoll Permanent Repair: C:\Users\Borys\Desktop\t\ducky\Scripts\RickrollPermanentRepair\payload.dd
#Rickroll NonPermament: C:\Users\Borys\Desktop\t\ducky\Scripts\RickrollNonPermanent\payload.dd
#Rickroll Permanent: C:\Users\Borys\Desktop\t\ducky\Scripts\RickrollPermanent\payload.dd
import shutil
import os
import time
import configparser

config = configparser.ConfigParser()
scripts = []

if __name__ == '__main__':
    print(Fore.RED + "  ____          _____  _    _  _____ ____               _                      __ _   ")
    print(" |  _ \   /\   |  __ \| |  | |/ ____|  _ \             | |                    / _| |  ")
    print(" | |_) | /  \  | |  | | |  | | (___ | |_) |   ___ _   _| |__   ___  ___  ___ | |_| |_ ")
    print(" |  _ < / /\ \ | |  | | |  | |\___ \|  _ <   / __| | | | '_ \ / _ \/ __|/ _ \|  _| __|")
    print(" | |_) / ____ \| |__| | |__| |____) | |_) | | (__| |_| | |_) |  __/\__ \ (_) | | | |_ ")
    print(" |____/_/    \_\_____/ \____/|_____/|____/   \___|\__,_|_.__/ \___||___/\___/|_|  \__|" + Fore.GREEN)
    #get the path of this script
    # check if the scripts.ini exists
    # if not create it
    # example scripts.ini:
    # [paths]
    # badusb = C:/
    # [rickroll]
    # delay = 30 #Delay in seconds before the music starts
    # create a new file named scripts.ini
    # example scripts.ini:
    # [RickrollPermanent]
    # path = \RickrollPermanent\payload.dd
    # displayname = Rickroll Permanent
    # description = This is a permanent rickroll use with caution 
    # placeholders = false
    # delayplaceholder = {DELAY} # in your script at first line create DELAY {DELAY}
    # [RickrollNonPermanent]
    # path = \RickrollNonPermanent\payload.dd
    # displayname = Rickroll Non Permanent
    # description = This is a non permanent rickroll this is more safe because it will be deleted after restart
    # placeholders = true
    # delayplaceholder = {DELAY} # in your script at first line create DELAY {DELAY}
    if not os.path.exists('scripts.ini'):
        with open('scripts.ini', 'w') as configfile:
            config.write(configfile)
    else:
        # assign the config.ini to scripts table
        config.read('scripts.ini')
        for section in config.sections():
            if section == 'paths':
                continue
            if section == 'rickroll':
                continue
            script = {}
            script['path'] = config.get(section, 'path')
            script['displayname'] = config.get(section, 'displayname')
            script['description'] = config.get(section, 'description')
            script['placeholders'] = config.get(section, 'placeholders')
            script['delayplaceholder'] = config.get(section, 'delayplaceholder')
            script['delay'] = config.get(section, 'delay')
            script['name'] = config.get(section, 'name')
            
            scripts.append(script)
    if not os.path.exists('config.ini'):
        config.read('config.ini')
        print("Configuring Procedure Starting...")
        pico_path = input('Enter the path to your bad usb (Raspberry Pi Pico like g:/ or c:/ etc.): ')
        config['paths'] = {'badusb': pico_path}
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        print("Configuring Procedure Finished")
    else:
        config.read('config.ini')
        pico_path = config['paths']['badusb']
        print('Bad USB Path: ' + pico_path)
            
    path = os.path.dirname(os.path.realpath(__file__))
    print('Path: ' + path)

    inp1 = input("Do you want to repair Rickroll or create a new one?\n(1) Upload\n(2) Edit\n(3) Create\n(4) Exit\n")
    if inp1 == "1":
        for script in scripts:
            scriptindex = str(scripts.index(script))
            print(Fore.BLUE+"("+scriptindex+") "+script['displayname'] + ": " + script['description'])
        inp = input("Enter Script ID: ")
        os.system('cls')
        # copy contents of the payload.dd to this script and add to first line "DELAY (Here you will paste config[rickroll][delay]and convert it from seconds to miliseconds) )"
        payloaddd = open(path + scripts[int(inp)]['path'], 'r')
        payloaddd_contents = payloaddd.read()
        payloaddd.close()
        payloaddd_contents = payloaddd_contents.replace(scripts[int(inp)]['delayplaceholder'], str(int(scripts[int(inp)]['delay'])*1000))
        # make a new payload.dd named payload.dd.new
        payloaddd_new = open(path + scripts[int(inp)]['path']+'.new', 'w')
        payloaddd_new.write(payloaddd_contents)
        payloaddd_new.close()

        #copy it to the bad usb and rename it to payload.dd
        shutil.copyfile(path + scripts[int(inp)]['path']+'.new', pico_path + 'payload.dd')

        #delete the payload.dd.new
        #os.remove(path + '/RickrollNonPermanent/payload.dd.new')

        
        print("[LOGS] "+scripts[int(inp)]['displayname'] + " has been uploaded to " + pico_path + 'payload.dd')
        time.sleep(2)
        print("Thank you for using our uploading system :)")
        time.sleep(2)
        print("[LOGS] Exiting...")
        time.sleep(2)
        exit()
        
    elif inp1 == "2":
        #print("(1) RickRoll Edit")
        #inp = input("Enter Script ID: ")
        #if inp == "1":
        #    delay = input("Enter Delay in seconds: ")
        #    config['rickroll']['delay'] = delay 
        #    with open('scripts.ini', 'w') as configfile:
        #        config.write(configfile)
        #    print("[LOGS] Rickroll's Delay Has Been Changed")
        #    time.sleep(2)
        #    exit()
        for script in scripts:
            scriptsindex = scripts.index(script)
            print(Fore.BLUE+ "("+str(scriptsindex)+") "+script['displayname'] + ": " + script['description'] + Fore.GREEN)
        inp = input("Enter Script ID: ")
        os.system('cls')
        # open script.ini and edit the delay
        
        config.read('scripts.ini')
        print(Fore.BLUE + "What do you want to edit?")
        print(Fore.GREEN +"(1) Delay")
        print("(2) Description")
        print("(3) Display Name")
        print("(4) Path")
        print("(5) Placeholders")
        print("(6) Exit")
        inp2 = input("Enter Option: ")
        inp = int(inp)
        if inp2 == "1":
            config.read('scripts.ini')
            delay = input("Enter Delay In Seconds: ")
            sections = config.sections()
            for section in sections:
                # if sections 'index' is equal to inp then edit the description
                if section == scripts[int(inp)]['name']:
                    config[section]['delay'] = delay

            with open('scripts.ini', 'w') as configfile:
                config.write(configfile)
            print("[LOGS] Script's Delay Has Been Changed")
            time.sleep(2)
            exit()
        elif inp2 == "2":
            config.read('scripts.ini')
            description = input("Enter Description: ")
            sections = config.sections()
            for section in sections:
                # if sections 'index' is equal to inp then edit the description
                if section == scripts[int(inp)]['name']:
                    config[section]['description'] = description

            with open('scripts.ini', 'w') as configfile:
                config.write(configfile)
            print("[LOGS] Script's Description Has Been Changed")
            time.sleep(2)
            exit()
        elif inp2 == "3":
            config.read('scripts.ini')
            displayname = input("Enter Display Name: ")
            sections = config.sections()
            for section in sections:
                # if sections 'index' is equal to inp then edit the description
                if section == scripts[int(inp)]['name']:
                    config[section]['displayname'] = displayname

            with open('scripts.ini', 'w') as configfile:
                config.write(configfile)
            print("[LOGS] Script's Display Name Has Been Changed")
            time.sleep(2)
            exit()
        elif inp2 == "4":
            config.read('scripts.ini')
            path = input("Enter Path: ")
            sections = config.sections()
            for section in sections:
                # if sections 'index' is equal to inp then edit the description
                if section == scripts[int(inp)]['name']:
                    config[section]['path'] = path

            with open('scripts.ini', 'w') as configfile:
                config.write(configfile)
            print("[LOGS] Script's Path Has Been Changed")
            time.sleep(2)
            exit()
        elif inp2 == "5":
            config.read('scripts.ini')
            delayplaceholder = input("Enter Delay Placeholder: ")
            sections = config.sections()
            for section in sections:
                # if sections 'index' is equal to inp then edit the description
                if section == scripts[int(inp)]['name']:
                    config[section]['delayplaceholder'] = delayplaceholder

            with open('scripts.ini', 'w') as configfile:
                config.write(configfile)
            print("[LOGS] Script's Placeholder Has Been Changed")
            time.sleep(2)
            exit()

        elif inp2 == "6":
            exit()
        else:
            print("[LOGS] Invalid Option")
            time.sleep(2)
            exit()
    elif inp1 == "3":# register a new script
        os.system('cls')
        print("Welcome To script Registrer")

        name = input("Enter Script ID (Wihout spaces): ")
        #if name contains spaces then ask again and say that name is invalid because it contains spaces
        if " " in name:
            print("[WARNING] Name Contains Spaces")
            time.sleep(2)
            exit()
        displayname = input("Enter Display Name: ")
        description = input("Enter Description: ")
        delay = input("Enter Delay In Seconds: ")
        delayplaceholder = input("Enter Delay Placeholder: ")
        path = input("Enter Path (Path from this folder to payload.dd /Rickroll/payload.dd <--- must be in this format): ")

        config.read('scripts.ini')
        config.add_section(name)
        config[name]['name'] = name
        config[name]['path'] = path
        config[name]['displayname'] = displayname
        config[name]['description'] = description
        config[name]['placeholders'] = "true"
        config[name]['delayplaceholder'] = delayplaceholder
        config[name]['delay'] = delay
        
        with open('scripts.ini', 'w') as configfile:
            config.write(configfile)
        print("[LOGS] Script Has Been Registered")
        time.sleep(2)
        exit()
    elif inp1 == "4":
        exit()


