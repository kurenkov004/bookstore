from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth import authenticate, login, logout # type: ignore
from django.contrib.auth.forms import AuthenticationForm # type: ignore

def login_view(request):
#initialize
  error_message = None
  form = AuthenticationForm()

  if request.method == 'POST':
    form = AuthenticationForm(data=request.POST)

#check if form is valid
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')

      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect('sales:records')
    else:
      error_message = 'oops, something went wrong'
  context = {
    'form': form,
    'error_message': error_message
  }
  return render(request, 'auth/login.html', context)
      




def logout_view(request):
  logout(request)
  return redirect('login') #refers to the previously defined "name" of the login view
  #all this view does is re-direct the user to the "login" page