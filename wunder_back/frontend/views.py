from django.conf import settings
from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        # return render(request, 'app/index.html')
        return redirect("http://localhost:3000")
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
