from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(req):
    return render(req,'mainapp/index.html')


def signuppage(req):
    return render(req,'mainapp/signup_final.html')

def lawsignuppage(req):
        return render(req,'mainapp/lawyersignup.html')

def signinpage(req):
        return render(req,'mainapp/signin.html')
