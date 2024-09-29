from django.urls import path
from django.views.decorators.cache import cache_page

from diary.apps import DiaryConfig
from diary.views import DiaryListView, DiaryDetailView, DiaryCreateView, DiaryUpdateView, DiaryDeleteView, \
    SearchPageView, HomePageView

app_name = DiaryConfig.name

urlpatterns = [

    path('', DiaryListView.as_view(), name='diaryentry_list'),
    path('diary/<int:pk>/', DiaryDetailView.as_view(), name='diaryentry_detail'),
    path('diary/create', DiaryCreateView.as_view(), name='diaryentry_create'),
    path('diary/<int:pk>/update', DiaryUpdateView.as_view(), name='diaryentry_update'),
    path('diary/<int:pk>/delete', DiaryDeleteView.as_view(), name='diaryentry_delete'),
    path('search/', SearchPageView.as_view(), name='search_results'),
    path('', HomePageView.as_view(), name='home'),

]
