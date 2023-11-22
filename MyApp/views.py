from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
# Create your views here.

# @login_required(login_url='/login')
# def home(request):
#      return render(request,'home.html')
 
# def signup(request):
#     if request.method == "POST":
#         uname = request.POST.get('username')
#         email = request.POST.get('email')
#         password1 = request.POST.get('password')
#         password2= request.POST.get('confirm-password')
       
       
#         if password1!=password2:
#             return HttpResponse("Your password and confirm password are not Same!!")
#         else:
#             my_user=User.objects.create_user(uname,email,password1)
#             my_user.save()
#             return redirect('login')

#     return render (request,'signup.html')

# def loginUser(request):
#     error_message = ""
#     if request.method=='POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
        
        
#         user = authenticate(username=username,password=password)
#         print(username,password)
#         if user is not None:
#             login(request,user)
#             return redirect('home')
#         else:
#              error_message = "Username or Password is incorrect!"

#     return render(request, 'login.html', {'error_message': error_message})

@login_required(login_url='/login')
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm-password')

        if password1 != password2:
            return HttpResponse("Your password and confirm password are not the same!!")
        else:
            my_user = User.objects.create_user(uname, email, password1)
            my_user.save()
            
            # Automatically log in the user after successful signup
            user = authenticate(username=uname, password=password1)
            login(request, user)

            return redirect('home')

    # If the user is already logged in, redirect to home
    if request.user.is_authenticated:
        return redirect('home')

    return render(request, 'signup.html')

def loginUser(request):
    error_message = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        print(username, password)
        if user is not None:
            login(request, user)
            
            # Redirect to home if the user is already logged in
            if request.user.is_authenticated:
                return redirect('home')
        else:
            error_message = "Username or Password is incorrect!"

    # If the user is already logged in, redirect to home
    if request.user.is_authenticated:
        return redirect('home')

    return render(request, 'login.html', {'error_message': error_message})
    
def LogoutPage(request):
    logout(request)
    return redirect('login')

def ContactPage(request):
    return render(request,'contact.html')


def submit_contact_form(request):
    if request.method == "POST":
        # Process and validate form data
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Include the sender's email address in the email content
        email_content = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"

        # Send an email
        send_mail(
            f"wonderchat page Contact Form Submission: {subject}",
            email_content,
            email,
            ['krishan.chhokar@indicchain.com'],  # Your email address
            fail_silently=False,
        )

        # Redirect to the Thank You page
        return render(request, 'thankyou.html')

    # Handle other cases (GET request or form submission failure)
    return render(request, 'contact.html')

