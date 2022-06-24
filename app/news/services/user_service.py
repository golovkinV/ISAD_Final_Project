from news.models.db_models import User
from news.models.db_models import News
from news.models.presentation_models import NewsListData, UserProfile


def get_user_by_id(id: int):
    user = User.objects.get(id=id)
    return UserProfile(user)


def get_user_news(id: int):
    users_news = News.objects.filter(user_id=id).order_by('-created_at')
    return [NewsListData(news) for news in users_news]
