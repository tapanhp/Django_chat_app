from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def not_found(request):
    return render(request, 'error/NotFound.html')


@login_required
def server_error(request):
    return render(request, 'error/servererror.html')
