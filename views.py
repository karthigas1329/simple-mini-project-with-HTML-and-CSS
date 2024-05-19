from django.shortcuts import render
def test(request):
	return render(request,'apps/index.html')
	
# Create your views here.
