from django.contrib import admin
from .models import Post

# Register your models here.


admin.site.register(Post)  # 관리자 페이지에서 만든 모델을 보려면 이 코드로 모델 등록
