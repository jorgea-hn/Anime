from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import logout


# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('usuario')
#         password = request.POST.get('contrasena')
#         if username == 'jorge' and password == '2023':
#             return redirect('lista:vistos')
#         else:
#             login_error = True
#             return render(request, 'login.html', {'login_error': login_error})
#     else:
#         return render(request, 'login.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('contrasena')
        if username == 'carolina' and password == '2023':
            request.session['logged_in'] = True
            return redirect('lista:vistos')
        else:
            login_error = True
            return render(request, 'login.html', {'login_error': login_error})
    else:
            return render(request, 'login.html')
    

def logout_view(request):
    request.session.flush()
    return redirect('login')