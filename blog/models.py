from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

# 업로드한 이미지를 년, 월, 일 별로 폴더를 나누어서 저장이 되도록 하는게 한곳에 모아서 저장하는거 보다 훨씬 성능개선에 좋다.
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
# 업데이트 시간에 대한 필드 선언과 인자값으로 auto_now=True를 넣어준다.
# 다시 저장할때 마다 그 시각이 저장되도록 한다.
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

# __str__은 관리자 페이지에서 제목과 유일키를 보여주는 기능을 함
# self.pk는 유일키 self.title은 제목을 보여준다.
    def __str__(self):
        return f'[{self.pk}번 {self.title}]'
# get_absolute_url을 정의하고 html에서 a href="{{ p.get_absolute_url }}"게 설정하여 url을 사용할 수 있다.
    def get_absolute_url(self):
        return f'/blog/{self.pk}'
