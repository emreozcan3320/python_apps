from database import Database
from user import User

Database.initialise(database="learning", host="localhost", user="postgres", password="123456")

my_user = User('tarzan@gmail.com', 'tarzan', 'orman', None)

my_user.save_to_db()

user_from_db = User.load_from_db_by_email('tarzan@gmail.com')

print(user_from_db)