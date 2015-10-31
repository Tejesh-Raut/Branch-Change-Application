from django.shortcuts import render
from .models import RollNo
from .forms import RollForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def logout_view(request):
    logout(request)
    rolls = RollNo.objects.all()
    return render(request, 'bc/index.html', {'rolls':rolls})

def roll_list(request):
	rolls = RollNo.objects.all()
	return render(request, 'bc/roll_list.html', {'rolls':rolls})

@login_required
def roll_detail(request, pk):
    roll = get_object_or_404(RollNo, pk=pk)
    return render(request, 'bc/roll_detail.html', {'roll': roll})

   

@login_required
def roll_new(request):
    #if request.method == "POST":
    #	form = PostForm(request.POST)
	#else:
    #
    if request.method == "POST":
        form = RollForm(request.POST)
        if form.is_valid():
            roll = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            roll.rollno_text !='' 
            roll.save()
            return redirect('bc.views.roll_detail', pk=roll.pk)
    else:
        form = RollForm()
    form = RollForm()
    return render(request, 'bc/roll_edit.html', {'form': form})

def roll_edit(request, pk):
    roll = get_object_or_404(RollNo, pk=pk)
    if request.method == "POST":
        form = RollForm(request.POST, instance=roll)
        if form.is_valid():
            roll = form.save(commit=False)
            #roll.author = request.user
            #roll.published_date = timezone.now()
            roll.save()
            return redirect('bc.views.roll_detail', pk=roll.pk)
    else:
        form = RollForm(instance=roll)
    return render(request, 'bc/roll_edit.html', {'form': form})