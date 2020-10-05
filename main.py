from manager import Manager

myID = ''
token = ''
api = ''

host = "localhost"
port = "1521"
sid = "xe"
user = "STUD"
password = "123"

friendsMyFriends = dict()

manager = Manager({"vkOptions": {
                 "myID": myID,
                 "token": token,
                 "api": api,
               },
         "dbOptions": {
             "user": user,
             "password": password,
             "host": host,
             "port": port,
             "sid": sid,
         }})


me = manager.getInfo(myID)
print(me)
# список моих друзей
myFriends = manager.getFriends(me)
for friend in myFriends:
    friendsMyFriends[friend["id"]] = manager.getFriends(friend)

print("Took all friends")

formattedData = manager.formatData(myFriends, friendsMyFriends)
print(formattedData)
