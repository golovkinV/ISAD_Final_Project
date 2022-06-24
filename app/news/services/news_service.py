from news.models.db_models import News
from news.models.presentation_models import NewsListData, BaseNews


def get_all_news():
    all_news = News.objects.order_by('-created_at')
    return [NewsListData(news) for news in all_news]


def get_news_by_id(id: int):
    news = News.objects.get(id=id)
    return BaseNews(news)


def get_news_by_category(id: int):
    filtered_news = News.objects.filter(category_id=id).order_by('-created_at')
    return [NewsListData(news) for news in filtered_news]
