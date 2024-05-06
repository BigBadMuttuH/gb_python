from django.urls import path
from .views import hello, HelloView
from .views import year_post, MonthPost, post_detail, my_view, TemplIf, templ_for, about, index
from .views import author_posts, post_full

urlpatterns = [
    path('hello/', hello, name='hello'),
    path('hello_class/', HelloView.as_view(), name='hello_class'),  # в случае с классом, добавляем as_view
    path('posts/<int:year>/', year_post, name='year_post'),
    path('posts/<int:year>/<int:month>/', MonthPost.as_view(), name='month_post'),
    path('posts/<int:year>/<int:month>/<slug:slug>/', post_detail, name='post_detail'),
    path('', my_view, name='my_view'),
    path('if/', TemplIf.as_view(), name='templ_if'),
    path('for/', templ_for, name='templ_for'),
    path('about/', about, name='about'),
    path('index/', index, name='index'),
    path('author/<int:author_id>/', author_posts, name='author_posts'),
    path('post/<int:post_id>/', post_full, name='post_full'),
]
