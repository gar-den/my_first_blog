from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.


class Post(models.Model):  # 모델 정의
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # models.ForeignKey: 다른 모델에 대한 링
	title = models.CharField(max_length=200)  # 글자 수가 제한된 텍스트 정의할 때 사용. 글 제목같이 짧은 문자열 정보 저장에 좋음
	text = models.TextField()  # models.TextField: 글자 수에 제한이 없는 긴 텍스트. 블로그 콘텐츠에 좋음
	created_date = models.DateTimeField(default=timezone.now)  # models.DateTimeField: 날짜와 시간
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):  # double-underscore: dunder
		return self.title
