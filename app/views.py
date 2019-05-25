from django.shortcuts import render

def a(request):
	print("hi")
	return render(request, 'a.html')

def b(request):
	return render(request, 'b.html')

def c(request):
	return render(request, 'c.html')

def d(request):
	return render(request, 'd.html')

def e(request):
	return render(request, 'e.html')

def f(request):
	return render(request, 'f.html')

def g(request):
	return render(request, 'g.html')

def h(request):
	return render(request, 'h.html')

def index(request): 
	return render(request, "index.html")
