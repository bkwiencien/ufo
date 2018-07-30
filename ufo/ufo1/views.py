from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

# ufo = pd.read_csv('http://bit.ly/uforeports', parse_dates=['Time'])

# Create your views here.
def index(request):
    my_dict = {"insert_me":"list will go here"}
    df = ufo = pd.read_csv('http://bit.ly/uforeports', parse_dates=['Time'])
    df = df.head(200)
    l_dict = {"listo":df.to_html()}
   # print(df)
    return render(request,"index.html",context=l_dict)