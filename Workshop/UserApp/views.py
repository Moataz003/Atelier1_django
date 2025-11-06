from urllib import request
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm  
def register(request):
   
   if request.method == 'POST':
       form = CustomUserCreationForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('login')
   else:
       form = CustomUserCreationForm()

   return render(request, 'C:/Users/brhmi/OneDrive/Bureau/cours_django/Workshop/template/register.html', {'form': form})
