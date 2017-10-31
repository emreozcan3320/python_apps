from psycopg2 import pool

# def connect():
#     return psycopg2.connect(database="learning", user="postgres", password="123456", host="localhost")

# databse classı yaratmamızın sebebi pytonun iç işleyiş matığından dolayı
# ilk olarak database bağlanmasını önlemek için diyelim ki bir arayüzün çalışmasını istiyoruz
class Database:
    __connection_pool = None
    @classmethod
    def initialise(cls, **kwargs):
        Database.__connection_pool = pool.SimpleConnectionPool(minconn=1,
                                                               maxconn=10,
                                                               **kwargs
                                                               )
    @classmethod
    def get_connection(cls):
        return cls.__connection_pool.getconn()
    @classmethod
    def return_connection(cls,connection):
        Database.__connection_pool.putconn(connection)
    @classmethod
    def close_all_connections(cls):
        Database.__connection_pool.closeall()

class CursorFromConnectionFromPool:
    def __init__(self):
        self.connection = None
        self.cursor = None
    def __enter__(self):
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exception_type, exception_value, exception_traceback):
        #if we get a error
        # exection_type => hata türü
        # exection_value => hata da depolanmış olan value
        # exection_traceback => where the error is happened
        if exception_value is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        Database.return_connection(self.connection)