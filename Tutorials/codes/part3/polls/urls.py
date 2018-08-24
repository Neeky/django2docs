from .views import index,detail,vote,results
from django.urls import path

app_name="polls" #通过一个叫app_name的变量来作为app的命名空间
urlpatterns=[
    path('',index,name='index'),
    path('<int:question_id>/',detail,name='detail'),
    path('<int:question_id>/results/',results,name='results'),
    path('<int:question_id>/vote/',vote,name='vote'),
]