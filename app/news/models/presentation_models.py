from .db_models import User, News


# Base classes
class BaseUser:

    def __init__(self, user: User):
        self.id = user.id
        self.first_name = user.first_name
        self.last_name = user.last_name
        self.email = user.email
        self.gender = user.gender.name


class BaseNews:

    def __init__(self, news: News):
        self.id = news.id
        self.title = news.title
        self.summary = news.summary
        self.body = news.body
        self.category = Category(news.category.name)
        self.created_at = news.created_at


class UserProfile(BaseUser):

    def __init__(self, user: User):
        super().__init__(user)
        self.all_news = [BaseNews(news) for news in list(user.news_set.all())]

    def get_statistics(self):
        categories = list([news.category for news in self.all_news])
        categories_count = dict(zip(categories, [categories.count(category) for category in categories]))
        statistics = [NewsStatistic(key, value) for key, value in categories_count.items()]
        return statistics


class Category:
    __colors_dict = {
        'Films': 'bg-primary',
        'IT': 'bg-success',
        'Games': 'bg-danger',
        'Books': 'bg-warning',
        'Society': 'bg-info'
    }

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def get_category_color(self):
        category = self.name
        return self.__colors_dict[category]


class NewsStatistic:

    def __init__(self, category: Category, count: int):
        self.category = category
        self.count = count


class NewsListData(BaseNews):

    def __init__(self, news: News):
        super().__init__(news)
        self.user = BaseUser(news.user)
