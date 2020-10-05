from vk.vkManager import VKManager
from db.db import BD


class Manager:

    # Считаем количество общих друзей
    @staticmethod
    def getMutualCount(friend, f, fMyFriends):
        count = 0
        try:
            f1 = fMyFriends[friend["id"]]
            f2 = fMyFriends[f]
        except KeyError:
            return count
        if isinstance(f1, list) and len(f1) >= len(f2):
            for f in f1:
                for ff in f2:
                    if f["id"] == ff["id"]:
                        count += 1
        else:
            for f in f2:
                for ff in f1:
                    if f["id"] == ff["id"]:
                        count += 1
        return count

    def __init__(self, options):
        self.vkManager = VKManager(options["vkOptions"])
        #self.db = BD(options["dbOptions"])
        self.mutualFriends = dict()

    def getInfo(self, id):
        if id and isinstance(id, str):
            return self.vkManager.getBaseInfo(id)[0]
        return "Не введен id"

    def getFriends(self, user):
        if user:
            return self.vkManager.getFriends(user["id"])
        return "Ошибка с юзером"

    def formatData(self, friends, friendsMyFriends):
        answer = dict()
        # будут храниться данные всех своих друзей
        answer["users"] = dict()
        # Будут храниться данные об общих друзьях
        answer["mutual"] = dict()
        # Убираем мертвых
        fMyFriends = dict()
        for friend in friendsMyFriends:
            if len(friendsMyFriends[friend]) != 0:
                fMyFriends[friend] = friendsMyFriends[friend]
        # Запоминаем данные по каждому своему другу
        for friend in friends:
            answer["users"][friend['id']] = friend
        # Для каждого своего друга создает в answer-е словарик
        for friend in friends:
            answer["mutual"][friend["id"]] = dict()
            # Открывает цикл по всем друзьям друзей и проверяем на наличие совпадений с другом выше
            for f in fMyFriends:
                # Что-то делаем только в случае, если работаем с двумя разными людьми
                if f != friend["id"]:
                    answer["mutual"][friend["id"]][f] = dict()
                    # Запоминаем список друзей друга
                    elem = fMyFriends[f]
                    # Ищем в списке друзей друга friend. Если найдено совпадение, значит они друзья,
                    # считаем количество общих друзей
                    for keys in elem:
                        if keys["id"] == friend["id"]:
                            answer["mutual"][friend["id"]][f]["isMutual"] = True
                            answer["mutual"][friend["id"]][f]["count"] = self.getMutualCount(friend, f, fMyFriends)
        return answer
