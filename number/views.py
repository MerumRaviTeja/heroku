from django.shortcuts import render,redirect
from django.http import HttpResponse
from number.forms import *
from django.core.exceptions import ValidationError
from django.core.mail import send_mail, BadHeaderError,EmailMessage
def chat(request):
    form=chatbox()
    if request.method=='POST':
        form=chatbox(request.POST)
        if form.is_valid():
            cname=request.POST.get('chater',' ')
            cmail=request.POST.get('chatermail',' ')
            cmsg=request.POST.get('message',' ')
            request.session[cmail]=cname+"  "+cmsg
            From="raviteja260982@gmail.com"
            To=cmail
            Sub="Dear "+cname 
            Message="Thank you "+cname+" we will get back to you within 24hrs." 
            try:
               mail = EmailMessage(Sub,From,Message,[To])
               mail.send()
               comment="Thank you "+cname
               return render(request,'chat.html',{'commentar':comment})
            except:
                return redirect(playerlogins)
        else:
            return redirect(playerlogins)
def puzzle(request):
    import random 
    a=str(random.randrange(999999999))
    b=[char for char in a]
    if len(b)==9:
             request.session['sample'] = b
             context={'one':b[0],'two':b[1],'three':b[2],'four':b[3],'five':b[4],'six':b[5],'seven':b[6],'eight':b[7],'nine':b[8]}
             return render(request,'home.html',context)
    elif True:
        return redirect(puzzle)
def output(request,count):
    context = {'score': str(count)}
    return render(request,'result.html', context)
def puzzlegame(request):
       form = AddNumbersForm()
       value = request.session['sample']
       if request.method == 'POST':
           count = 0
           if value[0]==request.POST.get('box1',' '):
               count+=1
           if value[1]==request.POST.get('box2',' '):
               count+= 1
           if value[2]==request.POST.get('box3',' '):
               count+=1
           if value[3]==request.POST.get('box4',' '):
               count+=1
           if value[4]==request.POST.get('box5',' '):
               count+=1
           if value[5]==request.POST.get('box6',' '):
               count+=1
           if value[6]==request.POST.get('box7',' '):
               count+=1
           if value[7]==request.POST.get('box8',' '):
               count+=1
           if value[8]==request.POST.get('box9',' '):
               count+=1
           duplicate_sname=request.session['player']
           if data.objects.filter(Enter_Name=duplicate_sname).exists():
               updates=data.objects.get(Enter_Name=duplicate_sname)
               if count>updates.Score:
                       updates.Score=count
                       updates.save()
               else:
                   return redirect(output, count)
           else:
                duplicate=data(Enter_Name=duplicate_sname,Score=count)
                duplicate.save()
           return redirect(output,count)
       return render(request,'table.html')
def mailsending(request):
    From="raviteja260982@gmail.com"
    play=request.session['player']
    record=data.objects.get(Enter_Name=play)
    To=record.Email_Address
    Sub="Dear "+play
    Message="Your Name and Security Code of gamer boy are: "+play+' ,'+record.Securitycode
    try:
               mail = EmailMessage(Sub,From,Message,[To])
               mail.send()
               return render(request,'mail.html',{'player':play})
    except:
                return HttpResponse("Oops something happen")
def recovery(request,player):
        another_name=player+", You have entered Wrong securitycode"
        return render(request,'recovery.html',{'another_name':another_name})
def playerlogins(request):
    form = login()
    if request.method == 'POST':
        form = login(request.POST)
        if form.is_valid():
            player = form.cleaned_data['Enter_Name']
            player=player.lower()
            code = form.cleaned_data['Securitycode']
            mail=form.cleaned_data['Email_Address']
            request.session['mail']=mail
            request.session['player']=player
            request.session['code']=code
            editableform= form.save(commit=False)
            if data.objects.filter(Enter_Name=player).exists() and data.objects.filter(Securitycode=code).exists():
                  return redirect(puzzle)
            if data.objects.filter(Enter_Name=player).exists():
                  return redirect(recovery,player)
            else:
                editableform.Enter_Name=player.lower()
                editableform.save()
                form.save_m2m()
                return redirect(puzzle)
        else:
            return redirect(playerlogins)
    else:
        another_name=0
        boarding=data.objects.all().order_by('-Score')[:13]
        return render(request,'Demo.html', {'form': form,'boarding':boarding,'another_name':another_name})