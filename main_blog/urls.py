from django.urls import path
from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('article/<slug:article_slug>', DetailArticle.as_view(), name='article/'),
    path('article/', RandomArticleView.as_view(), name='random_article'),
    path('category/<slug:categories_slug>', CategoriesView.as_view(), name='category/'),
    path('create_account/', CreateAccountView.as_view(), name='create_account'),
    path('sign_in/', LoginUserView.as_view(), name='sign_in'),
    path('search_article/', SearchArticle.as_view(), name='search_article'),
    path('logout/', logout_from_account, name='logout'),

]