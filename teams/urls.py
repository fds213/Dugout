import views
from django.urls import path
from . import views

app_name = 'users'
from . import views

app_name = 'users'

urlpatterns = [
    path('register/',
         views.register_user, name='register'),  # 회원가입
    path('login/', views.login_user,
         name='login'),  # 로그인
    path('logout/', views.logout_user,
         name='logout'),  # 로그아웃
]

urlpatterns = [
    path('', views.team_list, name='team_list'),
    path('compare/', views.compare_teams, name='compare_teams'),
]