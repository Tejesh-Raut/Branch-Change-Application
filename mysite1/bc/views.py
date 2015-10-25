from django.shortcuts import render
from .models import RollNo
from .forms import RollForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
# Create your views here.


def roll_list(request):
	rolls = RollNo.objects.all()
	return render(request, 'bc/roll_list.html', {'rolls':rolls})

def roll_detail(request, pk):
    roll = get_object_or_404(RollNo, pk=pk)
    return render(request, 'bc/roll_detail.html', {'roll': roll})


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