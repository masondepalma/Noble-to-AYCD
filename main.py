import json

filename = str(input('''
Enter 5 digits in your noble export file. 
EX. filename:noble-67088.json, enter: 67088

Enter:'''))
with open(f'./noble-{filename}.json', "r") as dbFile:
    data = json.load(dbFile)
    #getting profile list
    profileGroups = []
    gc = 0 
    for i in data['profileGroups']['order']:
        a = {
            "groupName":data['profileGroups']['groups'][i]['name'],
            "groupID":str(i),
            "groupNum":gc
        }
        profileGroups.append(a)
        gc += 1 
    for i in profileGroups:
        print(f"[{i['groupNum']}] Group Name: {i['groupName']} Group ID: {i['groupID']}")
    profileGroupToExport = str(input("Copy and enter group ID to use:"))
    profileIDlist = str(data['profileGroups']['groups'][profileGroupToExport]['profiles'])
    profileList = data['profiles']
    newProfileList = []
    a = 1
    for i in profileList:
        if str(i) in str(profileIDlist):
            print(f"Found profile {a}")
            a += 1
            activeProfile = profileList[i]
            activeProfile.pop('id')
            activeProfile['profileGroup'] == ""
            newProfileList.append(activeProfile)
    with open('./output.json','w+') as outputFile:
        outputFile.write(str(newProfileList))
    

