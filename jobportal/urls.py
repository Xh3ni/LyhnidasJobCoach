from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path('job/', views.job_search_list, name='job-search-list'),
    path('job/<slug>', views.job_detail, name='job-detail'),
]
