from django.contrib import admin
from .models import Book,Student,IssuedBook

admin.site.register(Book)
admin.site.register(Student)
admin.site.register(IssuedBook)
