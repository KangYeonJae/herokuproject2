from django.shortcuts import render,get_object_or_404,redirect
from .forms import NoticeForm
from .models import Notice
from django.utils import timezone

# Create your views here.
def post(request):
    if request.method=="POST":
        form=NoticeForm(request.POST)
        if form.is_valid():
            notice=form.save(commit=False)
            notice.update_date=timezone.now()
            notice.save()
            return redirect('show')
    else:
        form=NoticeForm()
        return render(request,'post.html',{'form':form})

def show(request):
    notices=Notice.objects.order_by('-id')
    return render(request,'show.html',{'notices':notices})

def detail(request,notice_id):
    notice_detail=get_object_or_404(Notice, pk=notice_id)
    return render(request,'detail.html',{'notice':notice_detail})

def edit(request,pk):
    notice=get_object_or_404(Notice,pk=pk)
    if request.method=="POST":
        form=NoticeForm(request.POST,instance=notice)
        if form.is_valid():
            notice=form.save(commit=False)
            notice.update_date=timezone.now()
            notice.save()
            return redirect('show')
    else:
        form=NoticeForm(instance=notice)
        return render(request,'edit.html',{'form':form})

def delete(request,pk):
    notice=Notice.objects.get(id=pk)
    notice.delete()
    return redirect('show')