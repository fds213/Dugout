from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register_user(request):
    if request.method == 'POST':  # POST 요청일 경우 폼 처리
        form = UserCreationForm(request.POST)
        if form.is_valid():  # 폼이 유효하면
            form.save()  # 유저를 저장
            messages.success(request, "회원가입이 완료되었습니다!")
            return redirect('users:login')  # 로그인 페이지로 리디렉션
    else:  # GET 요청일 경우 빈 폼 보여주기
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


# Create your views here.
