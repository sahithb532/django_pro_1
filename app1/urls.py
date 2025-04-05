from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('proj1/', views.proj1, name='proj1'),
    path('projects/', views.projects, name='projects'),
    path('singlepost/', views.singlepost, name='singlepost'),
]