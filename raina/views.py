from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d={'name':'ms','age':33}
    return render (request,'jinja_print.html',context=d)
    
def jinja_print(request):
    d1={'name':'fds','age':28}
    return render (request,'jinja_print.html',context=d1)

def jinja_print(request):
    d2={'name':'djB','age':39}
    return render (request,'jinja_print.html',context=d2)