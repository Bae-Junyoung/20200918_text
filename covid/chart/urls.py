from django.urls import path
from chart import views


app_name = 'chart'
urlpatterns = [
    path('line-chart', views.main_view, name='line-chart'),
    path('bar-chart', views.sub_view, name='bar-chart'),
]
