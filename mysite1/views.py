from django.http import HttpResponse
from django.shortcuts import render

    

def homepage(request):
    return render(request, 'home.html')



def coutpage(request):
    datav = request.GET['inparea']
    datas = datav.split()
    lenghtOfCount = len(datas)
    
    return render(request, 'count.html',{'n': datav,'l' : lenghtOfCount })
def about(requets):
    return HttpResponse('this is a about page')