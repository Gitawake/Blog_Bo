from django.shortcuts import render
from Blog import models
from django.shortcuts import HttpResponse

# Create your views here.

user_list = [
    {"user": "jack", "pwd": "abc"},
    {"user": "tom", "pwd": "ABC"}
]


def index(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)

        # 添加数据到数据库
        # models.Userinfo.objects.create(user=username, pwd=password)
    # 从数据库读取所有数据
    user_list = models.Userinfo.objects.all()

    return render(request, "index.html", {"data": user_list})
