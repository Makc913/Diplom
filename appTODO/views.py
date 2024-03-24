from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import TaskForm, CategoryForm
from .models import Task


# Create your views here.
def start(request):
    """
    Главная страница
    :param request: объект HttpRequest, содержащий информацию о запросе
    :return: объект HttpResponse, содержащий ответ
    """
    if request.user.is_authenticated:
        # Отображение шаблона "home.html", если пользователь аутентифицирован
        return render(request,"home.html", {})
    else:
        return render(request, "no_log.html", {})

def all_users(request):
    """
    Get all users
    :param request: объект HttpRequest, содержащий информацию о запросе
    :return: объект HttpResponse, содержащий ответ
    """
    # Получение всех пользователей из базы данных
    users = User.objects.all()
    context = {
        'users': users,
    }

    # Отображение шаблона 'listusers.html' с контекстом
    return render (request, "listusers.html", context)


def pers_user(reqest, user_id):
    """
    Получение объекта пользователя по его идентификатору
    :param reqest: Запрос от клиента
    :param user_id: Идентификатор пользователя
    :return: Ответ с отображением шаблона и контекстом
    """
    user = get_object_or_404(User, pk=user_id)  # Получение объекта пользователя по идентификатору
    context = {
        'user': user,  # Создание контекста с объектом пользователя
    }
    return render(reqest, 'pers_user.html', context)  # Отображение шаблона 'pers_user.html' с передачей контекста

def create_task(request):
    """
    Create Task
    :param request: объект HttpRequest, содержащий информацию о запросе
    :return: объект HttpResponse, содержащий ответ
    """
    if request.method == "POST":
        # Если метод запроса POST, создаем экземпляр формы с данными из запроса
        form = TaskForm(request.POST)
        if form.is_valid():
            # Если форма действительна, сохраняем данные формы
            form.save()
            # Перенаправляем пользователя на главную страницу
            return redirect('/')
    else:
        # Если метод запроса GET, создаем пустой экземпляр формы
        form = TaskForm()
    # Создание контекста для передачи данных в шаблон
    context = {
        'form': form
    }

    # Отображение шаблона 'create_task.html' с контекстом
    return render(request, 'create_task.html', context)

def create_category(request):
    """
    :param request: объект HttpRequest, содержащий информацию о запросе
    :return: объект HttpResponse, содержащий ответ
    """
    if request.method == "POST":
        # Если метод запроса POST, создаем экземпляр формы с данными из запроса
        form = CategoryForm(request.POST)
        if form.is_valid():
            # Если форма действительна, сохраняем данные формы
            form.save()
            # Перенаправляем пользователя на главную страницу
            return redirect('/')
    else:
        # Если метод запроса GET, создаем пустой экземпляр формы
        form = CategoryForm()
        # Создание контекста для передачи данных в шаблон
        context = {

        'form': form
    }
    # Отображение шаблона 'create_category.html' с контекстом
    return render(request, "create_category.html", context)


def get_task_user(request):
    """
    Get all tasks for user (GET)
    Получить все задачи для пользователя
    :param request: объект HttpRequest, содержащий информацию о запросе
    :return: объект HttpResponse, содержащий ответ
    """
    # Получение ID пользователя из запроса
    user_id = request.user.id
    # Получение всех задач, созданных данным пользователем
    task = Task.objects.filter(created_by=user_id)
    # Вывод ID пользователя и его имени в консоль (для отладки)
    print(user_id, request.user.username)
    # Создание контекста для передачи данных в шаблон
    context = {
        'task': task,
    }
    # Отображение шаблона 'get_task_user.html' с контекстом
    return render(request, "get_task_user.html", context)

def user_detail(request):
    """
    Возвращает детали пользователя на основе переданного 'user_id'
    :param request: Запрос от клиента
    :return: Ответ с отображением шаблона и контекстом
    """
    user = None  # Инициализация переменной user

    if request.method == 'POST':  # Проверка метода запроса
        user_id = request.POST.get('user_id')  # Получение значения 'user_id' из POST-запроса
        try:
            user = User.objects.get(id=user_id)  # Поиск пользователя по заданному 'user_id'
        except User.DoesNotExist:  # Обработка исключения, если пользователь не найден
            user = None

    return render(request, 'user_detail.html', {'user': user})  # Отображение шаблона 'user_detail.html' с передачей контекста

def user_task(request):
    """
    Отображает список задач пользователя.

    :param request: Запрос от клиента.
    :return: Отрендеренный шаблон с списком задач.
    """
    user = request.user
    tasks = Task.objects.filter(created_by=user)
    return render(request, 'user_task.html', {'tasks': tasks})