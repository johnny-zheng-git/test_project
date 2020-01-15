class Config():
    SECRET_KEY = 'zhengwenqaing'
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/flaskr"
    # MAX_OVERFLOW = 5,  # max_overflow=5 必须大写
    SQLALCHEMY_COMMIT_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    DEBUG = False
    TESTING = False
    DB = {
        "user": "root",
        "pwd": "cPHWFPtp55WE4Z1q",
        "host": "cdb-ovrbs6o6.cd.tencentcdb.com",
        "port": 10055,
        "db": "test2"
    }

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return f"mysql+pymysql://{self.DB['user']}:{self.DB['pwd']}@{self.DB['host']}:{self.DB['port']}/{self.DB['db']}"


class ProduceConfig(Config):
    DB = {
        "user": "root",
        "pwd": "cPHWFPtp55WE4Z1q",
        "host": "cdb-ovrbs6o6.cd.tencentcdb.com",
        "port": 10055,
        "db": "test2"
    }
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:cPHWFPtp55WE4Z1q@cdb-ovrbs6o6.cd.tencentcdb.com:10055/test2"


class DevelopmentConfig(Config):
    DB = {
        "user": "root",
        "pwd": "123456",
        "host": "127.0.0.1",
        "port": 3306,
        "db": "flaskr"
    }
    DEBUG = True


class TestingConfig(Config):
    DB = {
        "user": "root",
        "pwd": "123456",
        "host": "127.0.0.1",
        "port": 3306,
        "db": "flaskr"
    }
    TESTING = True
