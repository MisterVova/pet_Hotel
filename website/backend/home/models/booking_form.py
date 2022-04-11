from django.db import models


class BookingForm(models.Model):
    arrival_date = models.DateTimeField( verbose_name='Дата заезда')
    departure_date = models.DateTimeField( verbose_name='Дата выезда')
    adults = models.PositiveSmallIntegerField(verbose_name="Взрослые")
    children = models.PositiveSmallIntegerField(verbose_name="Дети")

    email = models.EmailField(verbose_name='Email')
    comment = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"с {self.arrival_date}  по {self.departure_date}. Взрослые {self.adults} Дети {self.children}"

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'
