from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sample(request):
    return HttpResponse("<h1 coloure><marquee>DHTF of POWER STAR PAVAN KALYAN</marquee></h1> ")

def sample1(request):
    return HttpResponse('<marquee><h1>Hloo Hiiii My Self Kalyan Naidu..........</h1><marquee>')