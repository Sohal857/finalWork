from django.urls import path
from . import views
from .views import register, user_login
# SET THE NAMESPACE!
app_name = 'reg_user'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('reg/', views.index,name='index'),
    path('special/', views.special,name='special'),
    path('logout/', views.user_logout, name='logout'),
]
