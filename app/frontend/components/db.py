import sqlite3
import bcrypt
import pandas as pd


# ___________Connect Database___________
class ConnectDataBase:
    def __init__(self, db_path):
        self._db_path = db_path
        self.conn = sqlite3.connect(self._db_path)
        self.cursor = self.conn.cursor()
        self.df = None

    def get_table(self, table="userstable", key="*"):
        self.df = pd.read_sql(f'SELECT {key} FROM {table}', self.conn)
        return self.df

    def close(self):
        self.cursor.close()
        self.conn.close()

    def __del__(self):
        self.close()

# ___________User Database___________
class UserDataBase(ConnectDataBase):
    def __init__(self, db_path):
        super().__init__(db_path)
        # dbのカラム?の名
        self.__name = "name"
        self.__username = "username"
        self.__password =  "password"
        self.__admin = "admin"
        
        self.__create_user_table()
        self.get_table()

    @property
    def name(self):
        return self.__name  
    @property
    def username(self):
        return self.__username  
    @property
    def password(self):
        return self.__password  
    @property
    def admin(self):
        return self.__admin  

    def __create_user_table(self):
        """
        該当テーブルが無ければ作る
        """
        self.cursor.execute('CREATE TABLE IF NOT EXISTS userstable({} TEXT, {} TEXT unique, {} TEXT, {} INT)'.format(self.name, self.username, self.password, self.admin))

    def _hashing_password(self, plain_password):
        return bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt()).decode()

    def __chk_username_existence(self, username):
        """
        ユニークユーザの確認
        """
        self.cursor.execute('select {} from userstable'.format(self.username))
        exists_users = [_[0] for _ in self.cursor]
        if username in exists_users:
            return True
        
    def add_user(self, name, username, password, admin):
        """
        新しくユーザを追加します
            [args]
                [0] name: str
                [1] username : str (unique)
                [2] password : str
                [3] admin : bool
            [return]
                res: str or None
        """

        if name=="" or username=="" or password=="":
            return
        if self.__chk_username_existence(username):
            return 
        # 登録
        hashed_password = self._hashing_password(password)
        self.cursor.execute('INSERT INTO userstable({}, {}, {}, {}) VALUES (?, ?, ?, ?)'.format(self.name, self.username, self.password, self.admin),
                                (name, username, hashed_password, int(admin)))
        self.conn.commit()
        return f"{name}さんのアカウントを作成しました"
