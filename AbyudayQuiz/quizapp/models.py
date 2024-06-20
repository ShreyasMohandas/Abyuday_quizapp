from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Teacher(models.Model):
    teacher=models.OneToOneField(User,on_delete=models.CASCADE,limit_choices_to={'groups__name':'Teachers'})

    def __str__(self) -> str:
        return self.teacher.username
    
class Student(models.Model):
    student=models.OneToOneField(User,on_delete=models.CASCADE,limit_choices_to={'groups__name':'Students'})
    teacher=models.ForeignKey(Teacher,related_name='students',on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.student.username
    
class Test(models.Model):
    techer=models.ForeignKey(Teacher,related_name='tests_created',on_delete=models.CASCADE)
    test_name=models.CharField(max_length=200)
    test_data=models.JSONField()
    file_path=models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.test_name
    
class TestAttempt(models.Model):
    student=models.ForeignKey(Student,related_name="test_attempted",on_delete=models.CASCADE)
    test=models.ForeignKey(Test,related_name="tests",on_delete=models.CASCADE)
    submitted_data=models.JSONField()
    obtained_marks=models.PositiveBigIntegerField()
    total_marks=models.PositiveBigIntegerField()

    class Meta:
        unique_together = ('student' , 'test')

    def __str__(self) -> str:
        return self.test.test_name
    
class TopicTags(models.Model):
    test=models.ForeignKey(Test,related_name='topic_test',on_delete=models.CASCADE)
    student=models.ForeignKey(Student,related_name='topics',on_delete=models.CASCADE)
    tags=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.tags
