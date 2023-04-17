from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.db import IntegrityError


class Grade(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Назва класу')
    is_active = models.BooleanField(verbose_name='Виводити на сторінці', default=True)
    slug = models.SlugField(max_length=255, unique=True, verbose_name="slug")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
       # return reverse ('subjects', kwargs={'slug':self.slug})
       # return f"/courses/n/"
         return f"/courses/{self.slug}/"

    class Meta:
        verbose_name = 'Клас'
        verbose_name_plural = 'Класи'


class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Назва предмету")
    order = models.IntegerField(blank=False, verbose_name="Порядок виводу", default=1)
    is_active = models.BooleanField(default=True, verbose_name="Виводити на сторінці")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="slug")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предмети'


class GradeSubject(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.PROTECT, verbose_name="Клас")
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, verbose_name="Предмет")
    name = models.CharField(max_length=150, unique=True, verbose_name="Клас-Предмет (заповнюється автоматично)", default='', editable=False)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(verbose_name="Активно", default=True)
    additional_id = models.CharField(max_length=10, blank=True, unique=True, db_index=True, verbose_name="Додатковий ID", default='', editable=False)
    slug_grade = models.SlugField(max_length=255, blank=True, db_index=True, verbose_name="slug класу (заповнюється автоматично)", default='', editable=False)
    slug_subject = models.SlugField(max_length=255, blank=True, db_index=True, verbose_name="slug предмету (заповнюється автоматично)", default='', editable=False)

    def __str__(self):
        return self.grade.name+' - '+self.subject.name

    def save(self):
        super(GradeSubject, self).save()
        if not self.name:
            self.name = (self.grade.name) + ' - ' + (self.subject.name)
            super(GradeSubject, self).save()
        if not self.additional_id:
            self.additional_id = str(self.grade.id) + '-' + str(self.subject.id)
            super(GradeSubject, self).save()
        if not self.slug_grade:
            self.slug_grade = (self.grade.slug)
            super(GradeSubject, self).save()
        if not self.slug_subject:
            self.slug_subject = (self.subject.slug)
            super(GradeSubject, self).save()

    class Meta:
        verbose_name = 'Зв"язок Клас - Предмет'
        verbose_name_plural = 'Зв"язки Клас - Предмет'

'''
    def save_model(self, request, obj, form, change):
        try:
            obj.save()
        except IntegrityError as e:
            raise ValidationError(e)
'''
