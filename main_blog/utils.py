from .models import Category, Article


class DataForSideBarAndNavigation:

    @staticmethod
    def get_category():
        return Category.objects.all()

    @staticmethod
    def get_new_articles():
        return Article.objects.all().order_by('-time_create')[:4]

    @staticmethod
    def get_count_article():
        return Article.objects.all().count

    @staticmethod
    def get_count_category():
        return Category.objects.all().count

    def get_data_for_sidebar_and_nav(self):
        context = {
            'categories': self.get_category(),
            'new_articles': self.get_new_articles(),
            'count_article': self.get_count_article(),
            'count_category': self.get_count_category()
        }
        return context
