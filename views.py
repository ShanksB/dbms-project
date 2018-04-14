from django.shortcuts import render
# Create your views here.

from .forms import RegisterStudentForm, LoginStudentForm

from .router import *

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from .models import Student


def homepage(request):
    message = request.session.get('message')
    request.session['message'] = None

    return render(request, 'examApplication/home_page.html', {'message': message})


def register_student(request):
    # if is_logged_in(request):
    #     return handle_already_logged_in_error(request)

    if request.method == "POST":
        form = RegisterStudentForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['message'] = 'Registration Successful, Now you can login'
            return redirect("home_page")
    else:
        form = RegisterStudentForm()

    return render(request, 'examApplication/student/register.html', {'form': form})

def login_student(request):
    if is_logged_in(request):
        return handle_already_logged_in_error(request)

    message = 'none'
    if 'message' in request.session:
    	message = request.session['message']
    	request.session['message'] = None
    	print("ok i am executed, ")
    
    error = None

    if request.method == "POST":
        form = LoginStudentForm(request.POST or None)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"], password=form.cleaned_data['password'])
            if user is not None and user.profile.type == 'u':
                login(request, user)
                return redirect('dashboard', permanent=True)
            else:
                error = 'incorrect username and password'
        else:
            error = 'invalid data entered'
    else:
        form = LoginStudentForm()
	
    return render(request, 'examApplication/student/login.html', {'form': form, 'user':'student', 'message':message})



@login_required(login_url='/login')
def dashboard(request):
    if request.user.profile.type == 'u':
      	user = Student.objects.get(EmailId = request.user.username)
      	message = None
      	error = None
      	if 'message' in request.session:
      		message = request.session['message']
      		request.session['message'] = None
   
      	return render(request, 'examApplication/student/dashboard.html', {"user": user, "error": error})
    return handle_lacks_privileges_error(request)


@login_required(login_url='home_page')
def logout_view(request):
    profile = request.user.profile.type
    logout(request=request)
    request.session['message'] = 'Successfully logged out'
    if profile == 'a':
        return redirect('login_admin')
    elif profile == 'u':
        return redirect('login_student')
 