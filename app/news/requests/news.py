from news.models import News


def get_all_news():
    return News.objects.order_by('-created_at')


def get_news_by_id(id: int):
    return News.objects.get(id=id)


def get_news_by_category(id: int):
    return News.objects.filter(category_id=id)
