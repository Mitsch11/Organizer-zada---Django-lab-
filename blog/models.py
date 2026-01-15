from django.db import models
from django.utils import timezone

class Zadanie(models.Model):
    STATUSY = [
        ("todo", "Do zrobienia"),
        ("doing", "W trakcie"),
        ("done", "Zrobione"),
    ]

    PRIORYTETY = [
        (1, "Niski"),
        (2, "Średni"),
        (3, "Wysoki"),
    ]

    tytul = models.CharField(max_length=120)
    opis = models.TextField(blank=True)
    termin = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUSY, default="todo")
    priorytet = models.IntegerField(choices=PRIORYTETY, default=2)
    utworzono = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.tytul
