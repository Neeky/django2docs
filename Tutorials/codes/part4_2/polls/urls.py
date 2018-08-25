from .views import index,detail,vote,results
from django.urls import path
from . import views

app_name="polls" #通过一个叫app_name的变量来作为app的命名空间
#urlpatterns=[
#    path('',index,name='index'),
#    path('<int:question_id>/',detail,name='detail'),
#    path('<int:question_id>/results/',results,name='results'),
#    path('<int:question_id>/vote/',vote,name='vote'),
#]

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
#注意vote并没有pk参数而是保留着question_id参数,这个主要是因为vote不是通过generic view实现的
