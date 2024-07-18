from django.db import models
from accounts.models import PetInfo, UserInfo


class Book(models.Model):
    title = models.CharField(max_length=128)
    pet = models.OneToOneField(PetInfo, on_delete=models.CASCADE, related_name='pet_book')
    author = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='my_books')
    description = models.CharField(max_length=500, default='')
    cover = models.ImageField(blank=True, null=True, upload_to='book_covers')
    last_updated = models.DateField(null=True)

    def __str__(self):
        return self.title


class Page(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='pages')
    author = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='my_pages')
    body = models.TextField(default='')
    created_at = models.DateField(auto_now_add=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.body # 애매하지만 일단 body로 설정, 확인 후 주석 삭제 바람 
    
def page_image_upload_path(instance, filename):
    return f'page_images/{instance.page.id}/{filename}'

class PageImage(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to=page_image_upload_path)

    def __int__(self):
        return self.id
    

class Note(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='notes')
    author = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='my_notes')
    body = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.body