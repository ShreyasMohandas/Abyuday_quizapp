from django.contrib import admin
from quizapp.models import *

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Test)
admin.site.register(TestAttempt)
admin.site.register(TopicTags)