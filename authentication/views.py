import imp
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import View
from django.contrib.auth import get_user_model

User=get_user_model()

# Create your views here.
class CreateSuperUser(View):
    def get(self,request):


        return render(request,'create_nurse_user.html')

    def post(self,request):
        data=request.POST
        print(data)
        user=User.objects.create_superuser(username=data['username'],password=data['password'])

        print(user)

        return redirect(reverse('home-page'))


