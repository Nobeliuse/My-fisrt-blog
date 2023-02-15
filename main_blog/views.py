from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView


from .forms import RegisterUserForm, LoginUserForm
from .models import Article, Category
from .utils import DataForSideBarAndNavigation


class Home(DataForSideBarAndNavigation, View):
    template_name = 'main_blog/index.html'

    def get(self, request):
        posts = Article.objects.all().order_by('?')[:4]
        context = {
            'title': 'My first blog',
            'posts': posts,
        }
        context = context | self.get_data_for_sidebar_and_nav()
        return render(request, self.template_name, context=context)


class DetailArticle(DataForSideBarAndNavigation, View):
    template_name = 'main_blog/detail_page.html'

    def get(self, request, article_slug):
        model = Article.objects.get(slug=article_slug)
        context = {
            'post': model,
            'title': model.title,
        }
        context = context | self.get_data_for_sidebar_and_nav()
        return render(request, self.template_name, context=context)


class RandomArticleView(DataForSideBarAndNavigation, View):
    template_name = 'main_blog/detail_page.html'

    def get(self, request):
        post = Article.objects.order_by("?").first()
        context = {
            'post': post,
            'title': post.title,
        }
        context = context | self.get_data_for_sidebar_and_nav()
        return render(request, self.template_name, context=context)


class CategoriesView(DataForSideBarAndNavigation, View):
    template_name = 'main_blog/index.html'

    def get(self, request, categories_slug):
        cat = Category.objects.get(slug=categories_slug)
        print(cat)
        posts = Article.objects.filter(category=cat.id)
        print(posts)
        context = {
            'posts': posts,
            'title': posts[0].category,
        }
        context = context | self.get_data_for_sidebar_and_nav()
        return render(request, self.template_name, context=context)


class SearchArticle(DataForSideBarAndNavigation, View):
    template_name = 'main_blog/index.html'

    def post(self, request):
        query = self.request.POST.get('q')
        object_list = Article.objects.filter(Q(title__icontains=query))
        context = {
            'posts': object_list,
            'title': f'Search - {query}',
        }
        context = context | self.get_data_for_sidebar_and_nav()
        return render(request, self.template_name, context=context)


class CreateAccountView(CreateView):
    form_class = RegisterUserForm
    template_name = 'main_blog/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'main_blog/login.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')


def logout_from_account(request):
    logout(request)
    return redirect('home')
