from django.shortcuts import render

from .models import ReuniaoCastelo
from .forms import ReuniaoCasteloForm

def criar_reuniao_castelo(request):
    if request.method == 'POST':
        form = ReuniaoCasteloForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReuniaoCasteloForm
    
    return render(request, 'form.html', {'form': form})
        

