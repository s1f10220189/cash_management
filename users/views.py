from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CustomUser
from django.contrib.sessions.models import Session

# ユーザー登録画面
def register_view(request):
    if request.method == 'POST':
        # ユーザー名をフォームから取得
        name = request.POST.get('name')
        # データベースにユーザーを保存
        user = CustomUser.objects.create(name=name)
        # セッションにユーザーIDを保存
        request.session['user_id'] = user.id
        # ホーム画面にリダイレクト
        return redirect('home')
    
    # GETリクエストでは登録画面を表示
    return render(request, 'register.html')

# ホーム画面
def home_view(request):
    user_id = request.session.get('user_id')
    
    # セッションが存在しない場合は登録画面にリダイレクト
    if not user_id:
        return redirect('register')
    
    # ユーザー情報をデータベースから取得
    user = CustomUser.objects.get(id=user_id)
    
    # ホーム画面にユーザー情報を渡してレンダリング
    return render(request, 'home.html', {'user': user})
# ログアウト
def logout_view(request):
    request.session.flush()  # セッションをクリア
    return redirect('register')
