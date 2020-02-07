from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(req):
    return render(req,'mainapp/index.html')


def signuppage(req):
    # registered = False


    #
    #     # Get info from "both" forms
    #     # It appears as one form to the user on the .html page
    #     user_form = UserForm(data=request.POST)
    #     profile_form = UserProfileInfoForm(data=request.POST)
    #
    #     # Check to see both forms are valid
    #     if user_form.is_valid() and profile_form.is_valid():
    #
    #         # Save User Form to Database
    #         user = user_form.save()
    #
    #         # Hash the password
    #         user.set_password(user.password)
    #
    #         # Update with Hashed password
    #         user.save()
    #
    #         # Now we deal with the extra info!
    #
    #         # Can't commit yet because we still need to manipulate
    #         profile = profile_form.save(commit=False)
    #
    #         # Set One to One relationship between
    #         # UserForm and UserProfileInfoForm
    #         profile.user = user
    #
    #         # Check if they provided a profile picture
    #         if 'profile_pic' in request.FILES:
    #             print('found it')
    #             # If yes, then grab it from the POST form reply
    #             profile.profile_pic = request.FILES['profile_pic']
    #
    #         # Now save model
    #         profile.save()
    #
    #         # Registration Successful!
    #         registered = True
    #
    #     else:
    #         # One of the forms was invalid if this else gets called.
    #         print(user_form.errors,profile_form.errors)
    #
    # else:
    #     # Was not an HTTP post so we just render the forms as blank.
    #     user_form = UserForm()
    #     profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    # return render(request,'basic_app/registration.html',
    #                       {'user_form':user_form,
    #                        'profile_form':profile_form,
    #                        'registered':registered})
    return render(req,'mainapp/signup_final.html')

def lawsignuppage(req):
    return render(req,'mainapp/lawyersignup.html')

def signinpage(req):
    if req.method == 'POST':
        username=req.POST['usrname']
        print(username)
        email=req.POST['emailname']
        print(email)
        send_mail('Lawyers Inc Verification',
        'Thank you for registering Your Account is now Activated',
        'winstonpais@live.in',
        [str(email)],
        fail_silently=False)
    return render(req,'mainapp/signin.html')
