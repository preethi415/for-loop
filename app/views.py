from django.shortcuts import render

# Create your views here.
def forloop(request):
    data='preethi'
    d={'name':data}
    return render(request,'forloop.html',d)
