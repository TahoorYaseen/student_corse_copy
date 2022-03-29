from django.urls import path
from .views import RegisterView,LoginView, UserView,LogoutView,getuserId,CourseView
# ,, 
app_name = 'baseapp'
urlpatterns = [
    path('register', RegisterView.as_view() ,name='register'),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    # path('getID',getuserId ),
    path('course',CourseView.as_view(),name='course'),
    path('course/<str:pk>',CourseView.as_view())


]