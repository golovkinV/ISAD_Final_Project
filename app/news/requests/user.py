from news.models import User
from news.models import News


def get_user_by_id(id: int):
    return User.objects.get(id=id)


def get_user_news(id: int):
    return News.objects.filter(user_id=id)
