

from models.user import User
from schemas.user import UserPydantic

all_users = [UserPydantic.model_validate(data) for data in User.get_all()]
print(*all_users)

user = User.get(email = 'foo@bar.ru')[0]
print(user)
print(UserPydantic.model_validate(user))