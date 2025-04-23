import random
import faker
from models.post import Post
from models.user import User
from schemas.user import UserPydantic, UserReg, UserRegV2

fake = faker.Faker("ru_RU")

if __name__ == "__main__":
    # User.create('bob1','qwe123', 'foo@bar.ru')
    # User.create('alice1','123qwe123', 'foo12@bar.ru', phone='+79998889988')

    # post1 = Post.create(user_id=7, title='Заголовок', contnet='Содержимое')
    # print(post1)
    # print(post1.contnet)


    # posts_data = [
    #     {
    #         "user_id": 7,
    #         "title": fake.street_title(),
    #         "contnet": fake.text(random.randint(100, 500)),
    #     }
    #     for _ in range(10)
    # ]
    
    # print(*posts_data, sep="\n")
    
    #################
    
    # posts = Post.get_per_user_id(user_id = 7)
    
    # for post in posts:
    #     print(post.to_dict())
    
    
    #################
    
    # users = User.get_all()
    # for user in users:
        ###
        
        # user = user.to_dict()
        # user.pop('password')
        # print(user)
        
        ####
        
        # print(user.profile)
        # print(user.profile.to_dict())
        
        ####
        
        # user_pydantic = UserPydantic.model_validate(user)
        # print(user_pydantic)
        # print(dict(user_pydantic))
        # print(user_pydantic.profile)
    ########
    
    
    
    user_data = [
        {
            "username": fake.user_name(),
            "password": fake.password(),
            "name": fake.name(),
            "email": fake.email(),
            "phone": fake.phone_number(),
        }
        for _ in range(2)
    ]
    
    
    for data in user_data:
        print('\n\n'+'-'*20)
        print(data)
        
        print('-'*20)
        # try:
        #     user_reg_pydantic = UserReg(**data)
        #     print(user_reg_pydantic)
        # except Exception as e:
        #     print(f'Пользовтель {data["username"]} получил ошибку {e}')
        print('-'*20)
        try:
            user_reg_pydantic = UserRegV2(**data)
            print(user_reg_pydantic)
        except Exception as e:
            print(f'Пользовтель {data["username"]} получил ошибку {e}')
        