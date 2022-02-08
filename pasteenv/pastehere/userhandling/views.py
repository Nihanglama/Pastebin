from urllib import request
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import redirect,render
from pastebin.forms import UserRegister
from django.contrib.messages import success,error



class UserLogin(LoginView):
    template_name='userhandling/login.html'
    fields='__all__'
    
    def get_success_url(self) -> str:
        return reverse_lazy('home')

    def get(self,*args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        else:
            error(request,'incorrect username or password')
        return super(UserLogin,self).get(*args, **kwargs)


    

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    form=UserRegister
    template='userhandling/register.html'
    if request.method=='POST':
        form=UserRegister(request.POST)
        if form.is_valid:
            form.save()
            success(request,'usercreated successfully')
            return redirect('Login')

    context_object_name={'form':form}
    return render(request,template,context_object_name)
            




            
    






