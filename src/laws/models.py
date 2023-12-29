from django.db import models


class AdministrativeOffencesCodeChapter(models.Model):
    number = models.SmallIntegerField(verbose_name='номер главы')
    name = models.TextField(verbose_name='название')
    created_at = models.DateTimeField(
        verbose_name='дата создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='дата последнего обновления',
        auto_now=True
    )
    
    def __str__(self) -> str:
        return str(self.number)


class AdministrativeOffencesCode(models.Model):
    CONJUNCTIONS = [
        ('OR', 'или'),
        ('AND', 'и'),
    ]
    
    chapter = models.ForeignKey(
        to=AdministrativeOffencesCodeChapter,
        verbose_name='глава',
        related_name='chapter',
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    number = models.FloatField(verbose_name='номер статьи')
    text = models.TextField(verbose_name='текст')
    notification = models.BooleanField(
        verbose_name='предупреждение',
        null=True, blank=True
    )
    conjunction_1 = models.CharField(
        verbose_name='союз',
        max_length=3,
        choices=CONJUNCTIONS,
        null=True, blank=True
    )
    penalty = models.CharField(
        verbose_name='сумма штрафа',
        max_length=300,
        null=True, blank=True
    )
    conjunction_2 = models.CharField(
        verbose_name='союз',
        max_length=3,
        choices=CONJUNCTIONS,
        null=True, blank=True
    )
    deprivation_driver_license = models.CharField(
        verbose_name='срок лишение ВУ',
        max_length=300,
        null=True, blank=True
    )
    conjunction_3 = models.CharField(
        verbose_name='союз',
        max_length=3,
        choices=CONJUNCTIONS,
        null=True, blank=True
    )
    arrest = models.CharField(
        verbose_name='срок ареста',
        max_length=300,
        null=True, blank=True
    )
    addition = models.TextField(
        verbose_name='дополнение',
        null=True, blank=True
    )
    created_at = models.DateTimeField(
        verbose_name='дата создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='дата последнего обновления',
        auto_now=True
    )
    
    def __str__(self) -> str:
        return str(self.number)


class CriminalCodeChapter(models.Model):
    number = models.SmallIntegerField(verbose_name='номер главы')
    name = models.TextField(verbose_name='название')
    created_at = models.DateTimeField(
        verbose_name='дата создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='дата последнего обновления',
        auto_now=True
    )
    
    def __str__(self) -> str:
        return str(self.number)


class CriminalCode(models.Model):
    CONJUNCTIONS = [
        ('OR', 'или'),
        ('AND', 'и'),
    ]
    
    chapter = models.ForeignKey(
        to=CriminalCodeChapter,
        verbose_name='глава',
        related_name='chapter',
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    number = models.FloatField(verbose_name='номер статьи')
    text = models.TextField(verbose_name='текст')
    penalty = models.CharField(
        verbose_name='сумма штрафа',
        max_length=300,
        null=True, blank=True
    )
    conjunction = models.CharField(
        verbose_name='союз',
        max_length=3,
        choices=CONJUNCTIONS,
        null=True, blank=True
    )
    compensation = models.BooleanField(
        verbose_name='возмещение ущерба',
        null=True, blank=True
    )
    conjunction_2 = models.CharField(
        verbose_name='союз',
        max_length=3,
        choices=CONJUNCTIONS,
        null=True, blank=True
    )
    arrest = models.CharField(
        verbose_name='срок ареста',
        max_length=300,
        null=True, blank=True
    )
    addition = models.TextField(
        verbose_name='дополнение',
        null=True, blank=True
    )
    created_at = models.DateTimeField(
        verbose_name='дата создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='дата последнего обновления',
        auto_now=True
    )
    
    def __str__(self) -> str:
        return str(self.number)
