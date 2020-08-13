from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Lancamentos, Misturados
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q

def Index(request):
    context = {"lancamentos": Lancamentos.objects.order_by("?").all(),
               "misturados": Misturados.objects.order_by("?").all()
    }
    return render(request, "index.html", context)
        
def About(request):
    return render(request, "about.html")
    
def Movie(request, pk):
    context = {"lancamento": Lancamentos.objects.get(id=pk)
    }
    return render(request, "movie.html", context)
    

def Mix(request, pk):
    context = {"misturado": Misturados.objects.get(id=pk)
    }
    return render(request, "mix.html", context)
    
def Search(request):
    if request.method == "POST":
        srch = request.POST["srh"]
        
        if srch:
            match = Lancamentos.objects.filter(Q(nome_film__icontains=srch) |
            Q(descricao__icontains=srch)) 
            matchh = Misturados.objects.filter(Q(nome_film__icontains=srch) | 
            Q(simpose__icontains=srch))
            if match:
                return render(request, "search.html", {"sr": match})
            if matchh:
                return render(request, "search.html", {"srr": matchh})
            else:
                messages.error(request, "Nenhum resultado encontrado...")
                
        else:
            return HttpResponseRedirect("/procurar/")
            
    return render(request, "search.html")   
