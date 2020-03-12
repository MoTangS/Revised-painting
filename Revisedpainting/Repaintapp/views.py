from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.


def index(request):
    return render(request,'index.html')