from django.shortcuts import render

# Create your views here.
def home(request):
  #returns the template file available & the request itself
  return render(request, 'customers/home.html')