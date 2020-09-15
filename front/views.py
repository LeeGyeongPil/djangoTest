from django.shortcuts import render, redirect

from .models import FrontBoard
from .forms import BoardRegForm, BoardUpdateForm
# Create your views here.
def index(request):
    boards = FrontBoard.objects.raw('SELECT boardidx,subject,regdate FROM front_board ')
    return render(request, 'index.html', {'boards' : boards})
    
def view(request,boardidx):
    board = FrontBoard.objects.raw('SELECT boardidx,subject,files,regdate FROM front_board WHERE boardidx  = %s',[boardidx])[0]
    return render(request, 'view.html', {'board' : board})
    
def write(request):
    if request.method == "POST":
        form = BoardRegForm(request.POST,request.FILES)
        if form.is_valid():
            # commit = False : DB에 저장을 바로 하지 않음
            board = form.save(commit = False)
            board.boardSave()
            return redirect('index')
    else:
        form = BoardRegForm()
        return render(request, 'write.html', {'form':form})
     
def modify(request,boardidx):
    board = FrontBoard.objects.raw('SELECT boardidx,subject,files FROM front_board WHERE boardidx  = %s',[boardidx])[0]
    if request.method == "POST":
        print(request.FILES)
        form = BoardUpdateForm(request.POST,request.FILES,instance = board)
        if form.is_valid():
            board = form.save()
            board.boardSave()
            return redirect(f'/view/{boardidx}')
    else:
        form = BoardUpdateForm(request.POST or None,instance = board)
        return render(request, 'modify.html', {'form':form})
        
def delete(request,boardidx):
    board = FrontBoard.objects.get(boardidx=boardidx)
    board.delete()
    return redirect(index)