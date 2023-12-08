from django.shortcuts import render

def things_view(request):
    return render(request, 'things/things_page.html')