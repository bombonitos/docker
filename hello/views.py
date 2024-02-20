from django.views.generic import ListView
from django.db.models import Q
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Cart, Kitty

def index(request):
    return render(request, "index.html")

def base(request):
    return render(request, "base.html")

def catalog(request):
    kitty = Kitty.objects.all()
    return render(request, "catalog.html",{'kitty': kitty})

def cart(request):
    return render(request, "cart.html")

def contact(request):
    return render(request, "contact.html")

def profile(request):
    return render(request, "profile.html")


class Search(ListView):
    template_name = "index.html"
    context_object_name = "kitty"

    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        if not query:
            return redirect('/search/')  # Исправлен путь для перенаправления на страницу поиска
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        query = self.request.GET.get('q')
        results = Kitty.objects.filter(Q(name__icontains=query))
        return results

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context

# Представление для регистрации пользователя
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Аккаунт создан для ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)

# Представление для входа пользователя
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Используйте объект пользователя, а не строку
            return redirect('index')
        else:
            messages.info(request, 'Имя пользователя или пароль неверны')
    context = {}
    return render(request, 'login.html', context)

# Представление для выхода пользователя
def logoutUser(request):
    logout(request)
    return redirect('login')



from django.shortcuts import render, get_object_or_404
from .models import Kitty  # Импортируйте вашу модель

def product_detail(request, product_id):
    kitty = get_object_or_404(Kitty, id=product_id)
    return render(request, 'product_detail.html', {'kitty': kitty})



# Представление для выхода пользователя
def logoutUser(request):
    logout(request)
    return redirect('login')
def about(request):
    # ваш код для обработки запроса
    return render(request, 'about.html')
def reviews(request):
    # Ваш код для обработки запроса
    return render(request, 'reviews.html')
def profile(request):
    # Ваш код для обработки запроса
    return render(request, 'profile.html')


def delete_user(request):
    user = request.user
    user.delete()
    return redirect('login')


# Представление для выхода пользователя
def logoutUser(request):
    logout(request)
    return redirect('login')
def about(request):
    # ваш код для обработки запроса
    return render(request, 'about.html')
def reviews(request):
    # Ваш код для обработки запроса
    return render(request, 'reviews.html')
def profile(request):
    # Ваш код для обработки запроса
    return render(request, 'profile.html')


def politics(request):
    # Ваш код для обработки запроса
    return render(request, 'politics.html')
def tovar(request):
    # Ваш код для обработки запроса
    return render(request, 'tovar.html')

def confidence(request):
    # Ваш код для обработки запроса
    return render(request, 'confidence.html')

def about(request):
    # Ваш код для обработки запроса
    return render(request, 'about.html')


def delete_user(request):
    user = request.user
    user.delete()
    return redirect('login')


class Search(ListView):
    template_name = 'catalog.html'
    context_object_name = 'kitty'


    def get_queryset(self):
        return Kitty.objects.filter(name__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context



