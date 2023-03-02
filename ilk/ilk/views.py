from django.shortcuts import render



def index (request):
    if request.method == 'POST':
      num1=request.POST.get('num1')
      num2=request.POST.get('num2')

        
      return render(request,'sonuc.html', {'num1': num1, 'num2': num2})
  
    else:
      return render(request,"index.html")


def sonuc(request):
  return render(request, "sonuc.html")