import cx_Oracle


class BD:
    def __init__(self, params):
        host = params["host"]
        port = params["port"]
        sid = params["sid"]
        user = params["user"]
        password = params["password"]
        self.dsnStr = cx_Oracle.makedsn(host, port, sid)
        self.con = cx_Oracle.connect(user, password, dsn=self.dsnStr)

    def addFriendInfo(self, *params):
        cur = self.con.cursor()

        id, first_name, last_name, photo = params
        # FIRST_NAME, LAST_NAME, PHOTO = *keys

        query = "INSERT INTO FRIENDS_INFO(ID, FIRST_NAME, LAST_NAME, PHOTO) VALUES (:ID, :FIRST_NAME, :LAST_NAME, :PHOTO)"
        # .format(keys = keys)

        cur.execute(query,
                    {'ID': id, 'FIRST_NAME': first_name, 'LAST_NAME': last_name, 'PHOTO': photo, })
        self.con.commit()
        cur.close()

    def __del__(self):
        self.con.close()