from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from admin_panel.models import CustomUser, Session  # Import the CustomUser model from admin_panel
from .models import Session_booking
from .forms import SessionBookingForm
from django.http import HttpResponse
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        users = CustomUser.objects.all()
        for user in users:
            if username == user.username and password == user.password:
                # Redirect to user_dashboard with username as part of the URL
                return redirect('user_dashboard', username=username)
        
        # If no user matches the credentials, render the login page with an error message
        return render(request, 'userlogin.html', {'error_message': 'Invalid username or password'})
    
    # Handle GET requests (display login form)
    return render(request, 'userlogin.html')  

def user_dashboard(request, username):
    session = Session.objects.all()
    # Pass the username to the template for display
    return render(request, 'user_templates/user_dashboard.html', {'username': username, 'session': session})


def book_session(request):
    if request.method == 'POST':
        session_id = request.POST.get('session')
        username = request.POST.get('username')
        session = Session.objects.get(pk=session_id)
        
        # Check if the session is already booked
        if Session_booking.objects.filter(session=session).exists():
            messages.error(request, f'Session "{session.subject}" is already booked by another user.')
            return redirect('user_dashboard', username=username)
        
        form = SessionBookingForm(request.POST)
        if form.is_valid():
            session_booking = form.save()
            messages.success(request, f'Session "{session.subject}" booked successfully.')
            return redirect('user_dashboard', username=username)
    
    return redirect('user_dashboard', username=request.POST.get('username'))
