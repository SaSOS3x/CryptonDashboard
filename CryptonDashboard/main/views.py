from django.shortcuts import render
from .models import Node

def main(request):
    node = Node.objects.all()
    return render(request, 'main/index.html', {'node': node})



def active(request):
    node = Node.objects.filter(status = 'Active')
    return render(request, 'main/index.html', {'node': node})

def upcoming(request):
    node = Node.objects.filter(status = 'Upcoming')
    return render(request, 'main/index.html', {'node': node})

def ended(request):
    node = Node.objects.filter(status = 'Ended')
    return render(request, 'main/index.html', {'node': node})



def newest(request):
    node = Node.objects.order_by('-start')
    return render(request, 'main/index.html', {'node': node})

def raiting(request):
    node = Node.objects.order_by('start')
    return render(request, 'main/index.html', {'node': node})

def complexity(request):
    node = Node.objects.order_by('-Complexity')
    return render(request, 'main/index.html', {'node': node})



def info(request ,node_name):
    node = Node.objects.filter(title = node_name)
    return render(request, 'main/info.html', {'node': node})

def guide(request ,node_name, node_guide):
    return render(request, 'main/guide/' + node_guide + '.html')