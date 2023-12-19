import urllib.parse as parse
from django.http import  JsonResponse
from django.shortcuts import redirect, render
from .models import Pasteitem
from django.contrib.auth.decorators import login_required
import os
import subprocess
from django.contrib.messages import success
from .forms import Update_profile


def Home(request):
    template='pastebin/home.html'
    return render(request,template)

@login_required(login_url='Login')
def Postpaste(request):
    data= parse.parse_qs((request.body).decode('utf-8'))
    title=data['title'][0]
    language=data['language'][0]
    visibility=data['visibility'][0]
    code=data['code'][0]
    Pasteitem.objects.create(
        user=request.user.customer,
        title=title,
        pasteitems=code,
        languages=language,
        visible=visibility
    )
    return JsonResponse('saved',safe=False)


@login_required(login_url='Login')
def Pasteitems(request):
    pasteitem=request.user.customer.pasteitem_set.all()
    langauges=[language.languages for language in pasteitem]
    other_items=Pasteitem.objects.all().exclude(user=request.user.customer).exclude(visible='private')
    context_object_name={'pasteitems':pasteitem,'others_pastes':other_items}
    template='pastebin/pastelist.html'
    return render(request,template,context_object_name)

@login_required(login_url='Login')
def Deleteitem(request,pk):
    item=request.user.customer.pasteitem_set.get(id=pk)
    print(item)
    item.delete()
    return redirect('mypaste')
   
def Profile(request):
    template_name='pastebin/profile.html'
    form=Update_profile(instance=request.user.customer)
    if request.method=='POST':
        form=Update_profile(request.POST,request.FILES,instance=request.user.customer)
        if form.is_valid():
            form.save()
            success(request,'profile updated successfully..')
    context_object_name={'form':form}

    return render(request,template_name,context_object_name)

def editor(request):
    template='pastebin/editor.html'
    return render(request,template)

def executecode(request):
    data= parse.parse_qs((request.body).decode('utf-8'))
    language=data['languages']
    code=data['code']
    base_dir=os.getcwd()
    paths=base_dir+'/pastebin/tempfiles'
    name='tempcode.'+language[0]
    complete_path=os.path.join(paths,name)
    code_file=open(complete_path,"w")
    code_file.write(code[0])
    code_file.close()
    
    print(language[0])
    if(language[0]=='py'):
        output=None
        output=subprocess.getoutput('python3 '+complete_path)
        print(output)
        if(os.path.exists(complete_path)):
            os.remove(complete_path)
        else:
            print('no file')
    elif(language[0]=='java'):
        output=None
        output=subprocess.getoutput('java '+complete_path)
        print(output)
        if(os.path.exists(complete_path)):
            os.remove(complete_path)
        else:
            print('no file')
    elif(language[0]=='c'):
        output=subprocess.getoutput('gcc {} -o 1'.format(complete_path))
        exe_path='/home/nihang/Documents/Pastebin/pasteenv/pastehere/1'
        if(os.path.exists(exe_path)):    
            output=subprocess.getoutput('./1')
            os.remove(exe_path)
        if(os.path.exists(complete_path)):
            os.remove(complete_path)
        else:
            print('no file')
        print(output)
    elif(language[0]=='cpp'):
        output=subprocess.getoutput('g++ {} -o 2'.format(complete_path))
        exe_path='/home/nihang/Documents/Pastebin/pasteenv/pastehere/2'
        if(os.path.exists(exe_path)):    
            output=subprocess.getoutput('./2')
            os.remove(exe_path)
            print(output)
        if(os.path.exists(complete_path)):
            os.remove(complete_path)
        else:
            print('no file')
        
    else:
        output='We will add editor for {} in comming updates'.format(language[0])
    return JsonResponse(output,safe=False)
