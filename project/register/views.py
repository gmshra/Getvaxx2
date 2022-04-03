from django.shortcuts import render
from .models import User
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

def index(request):
	if request.method == "POST":
		fname = request.POST["firstname"]
		lname = request.POST["lastname"]
		uname = request.POST["username"]
		email = request.POST["email"]
		passw = request.POST["password"]
		

		data = User(first_name = fname , last_name = lname , email_id = email , user_name = uname , password = passw)
		data.save()
		return HttpResponse("<h1> data saved sucessfully</h1>")


	return render(request, 'index.html')



def homepage(request):
    return render(request, 'Index.html')

