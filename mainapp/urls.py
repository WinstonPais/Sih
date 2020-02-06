from django.conf.urls import url
from mainapp import views

#template tagging
app_name = 'mainapp'
urlpatterns=[
    url(r'^clientsignuppage/$',views.signuppage,name='signUpPage'),
    url(r'^lawyersignuppage/$',views.lawsignuppage,name='LawSignUp'),
    url(r'^signinpage/$',views.signinpage,name='signIn'),
]
