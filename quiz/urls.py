from django.urls import path
from . import views
from .views import QuestionListView
from django.conf.urls import url
urlpatterns = [ 
  path('', QuestionListView.as_view(), name='home'),
  path('<int:pk>',views.detail, name='question_text_detail'),
    path('<int:question_id>/check/', views.check, name='check')
]