from django.shortcuts import render
from .models import Node, World, VPS, Country

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

def infonode(request ,node_name):
    
    return render(request, node_name + 'guide.html', )

def guide(request ,node_name, node_guide):
    return render(request, 'main/guide/' + node_guide + '.html')

def world(request, node_name):
    world = World.objects.filter(name = node_name)
    vps = VPS.objects.filter(name = node_name)
    country = Country.objects.filter(name = node_name)

    return render(request, 'main/world.html', {'node': node_name, 'world': world, 'vps': vps, 'country': country})