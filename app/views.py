from django.shortcuts import render

# Create your views here.
def if_condition(request):
    d={'a':'321','b':'211'}
    return render(request,'if_condition.html',d)


def if_else_condition(request):
    d={'a':'20','b':'25'}
    return render(request,'if_else_condition.html',d)


def if_elif_else_condition(request):
    d={'a':'200','b':'','c':'224'}
    return render(request,'if_elif_else_condition.html',d)


def nested_if_condition(request):
    d={'a':'200','b':'198','c':'108'}
    return render(request,'nested_if_condition.html',d)


def for_loop(request):
    d={'name':'DJANGO'}
    return render(request,'for_loop.html',d)