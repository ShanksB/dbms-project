from django.shortcuts import render
# Create your views here.

from .forms import RegisterStudentForm, LoginStudentForm, FeesApplicationForm

from .router import *

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from .models import Student, Admin, FeesNotification, FeesPayment
from django.utils.timezone import localtime, now


def homepage(request):
    message = None
    if 'message' in request.session:
        message = request.session['message']
        request.session['message'] = None
    return render(request, 'examApplication/home_page.html', {'message': message})


def register_student(request):

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

    return render(request, 'examApplication/student/login.html', {'form': form, 'user': 'student', 'message': message})


@login_required(login_url='/login')
def dashboard(request):
    if request.user.profile.type == 'u':
        user = Student.objects.get(EmailId=request.user.username)
        message = None
        error = None
        if 'message' in request.session:
            message = request.session['message']
            request.session['message'] = None
        application_opened = None
        not_paid = None
        hall_ticket_available = FeesNotification.objects.all().first().HallTicketAvailable
        if FeesNotification.objects.all().count() > 0:
            application_opened = True
            print(FeesNotification.objects.all().count() )
            not_paid = True
        return render(request, 'examApplication/student/dashboard.html', {"user": user, "hall_ticket_available": hall_ticket_available, error: "error", "application_opened": application_opened, "not_paid": not_paid})
    return handle_lacks_privileges_error(request)



@login_required(login_url='login')
def download_hall_ticket(request):
    if request.user.profile.type == 'u':
        return redirect('https://www.google.com/imgres?imgurl=https%3A%2F%2Fassets.change.org%2Fphotos%2F7%2Fwk%2Fbh%2FpUWkBhduwOtRAVV-800x450-noPad.jpg%3F1509858171&imgrefurl=https%3A%2F%2Fwww.change.org%2Fp%2Fwarner-brothers-make-wonder-woman-bisexual&docid=U5oOunR1QHNoJM&tbnid=KgAfpZTcFFK0KM%3A&vet=10ahUKEwiW5rDqr8vaAhVEsI8KHZ78BNQQMwjNASgEMAQ..i&w=799&h=449&client=ubuntu&bih=637&biw=1299&q=wonder%20woman&ved=0ahUKEwiW5rDqr8vaAhVEsI8KHZ78BNQQMwjNASgEMAQ&iact=mrc&uact=8')
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


@login_required(login_url='login')
def pay_fees(request):
    message = None
    error = None
    if request.user.profile.type == 'u':
        if request.method == "POST":
            form = FeesApplicationForm(request.POST or None)
            if form.is_valid():
                fees_notification = FeesNotification.objects.all().first()
                student  = Student.objects.get(EmailId = request.user.username)
                fees_payment = FeesPayment.objects.create(ApplicationId = fees_notification, StudentId = student, PaidFees = str(form['PaidFees'].value()) )
                return redirect('dashboard')
        else:
            form = FeesApplicationForm()
            print('yes here ')
        return render(request, 'examApplication/student/pay_fees.html', {'form':form, 'error': error, 'messages': message})
    return handle_lacks_privileges_error(request)












 # admin starts here


def login_admin(request):
    if is_logged_in(request):
        return handle_already_logged_in_error(request)

    message = None
    if 'message' in request.session:
        message = request.session['message']
        request.session['message'] = None
        print("Ok i am executed, ")

    error = None

    if request.method == "POST":
        form = LoginStudentForm(request.POST or None)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"], password=form.cleaned_data['password'])
            if user is not None and user.profile.type == 'a':
                login(request, user)
                return redirect('dashboard_admin', permanent=True)
            else:
                error = 'Incorrect username and password'
        else:
            error = 'Invalid data entered'
    else:
        form = LoginStudentForm()

    return render(request, 'examApplication/student/login.html', {'form': form, 'user': 'admin', 'message': message})


@login_required(login_url='login_admin')
def dashboard_admin(request):
    if request.user.profile.type == 'a':
        user = Admin.objects.get(EmailId=request.user.username)
        message = None
        error = None
        if 'message' in request.session:
            message = request.session['message']
            request.session['message'] = None

        application_opened = None
        hall_ticket_available = FeesNotification.objects.all().first().HallTicketAvailable
        print(hall_ticket_available)
        if FeesNotification.objects.all().count() == 1:
            application_opened = True
            print(FeesNotification.objects.all().count())

        return render(request, 'examApplication/admin/dashboard.html', {"admin": user, "hall_ticket_available": hall_ticket_available, "error": error, "application_opened": application_opened})
    return handle_lacks_privileges_error(request)


@login_required(login_url='login_admin')
def open_fees_application(request):
    if request.user.profile.type == 'a':
        message = None
        error = None
        if 'message' in request.session:
            message = request.session['message']
            request.session['message'] = None
            fee_notification = FeesNotification.objects.create(StartDate=localtime(
                now()).date(), EndDate='2018-09-01', Description='fees notification working')
            fee_notification.save()
            return redirect('dashboard_admin')


@login_required(login_url='login_admin')
def close_fees_application(request):
    if request.user.profile.type == 'a':
        message = None
        error = None
        if 'message' in request.session:
            message = request.session['message']
            request.session['message'] = None

        return redirect('dashboard_admin')


@login_required(login_url='login_admin')
def extend_fees_date(request):
    if request.user.profile.type == 'a':
        message = None
        error = None
        if 'message' in request.session:
            message = request.session['message']
            request.session['message'] = None
        return redirect('dashboard_admin')


@login_required(login_url='login_admin')
def send_fees_reminder(request):
    if request.user.profile.type == 'a':
        message = None
        error = None
        if 'message' in request.session:
            message = request.session['message']
            request.session['message'] = None
        # fetch from form
        # fees = Fees.objects.create()
        return redirect('dashboard_admin')



#hall ticket printout...
@login_required(login_url='login')
def hall_ticket_printout(request):
    if request.user.profile.type == 'a':
        message = None
        error = None
        if 'message' in request.session:
            message = request.session['message']
            request.session['message'] = None
        fees_notification = FeesNotification.objects.all().first()
        fees_notification.HallTicketAvailable = 'true'
        fees_notification.save()
        
        return redirect('dashboard_admin')
    return handle_lacks_privileges_error(request)