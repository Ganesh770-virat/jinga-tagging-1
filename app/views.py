from django.shortcuts import render

# Create your views here.
def hello(request):
    d = {'a':'gani','age':'31','gender':'male'}
    return render(request,'gani.html',context=d)
# jinga tagging  is advanced level writing tags in html pages
# is also known as template tags
# 1 dictonary create in views .
# in html pages we need to give {{key value}} it is given as output in 'FE'
