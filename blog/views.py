from django.shortcuts import render
from django.utils import timezone
from .models import Zadanie


def lista_zadan(request):
    q = request.GET.get("q", "").strip()
    status = request.GET.get("status", "").strip()


    zadania = Zadanie.objects.all().order_by("termin", "-priorytet")

    if status in {"todo", "doing", "done"}:
        zadania = zadania.filter(status=status)

    if q:
        zadania = zadania.filter(tytul__icontains=q)

    dzis = timezone.localdate()

    baza = zadania
    bez_terminu = baza.filter(termin__isnull=True).exclude(status="done")
    zalegle = baza.filter(termin__lt=dzis).exclude(status="done")
    na_dzis = baza.filter(termin=dzis).exclude(status="done")
    nadchodzace = baza.filter(termin__gt=dzis).exclude(status="done")
    zrobione = baza.filter(status="done")
    wszystkie = baza.order_by("termin", "-priorytet")

    return render(request, "blog/lista_zadan.html", {
        "q": q,
        "status": status,
        "dzis": dzis,
        "bez_terminu": bez_terminu,
        "zalegle": zalegle,
        "na_dzis": na_dzis,
        "nadchodzace": nadchodzace,
        "zrobione": zrobione,
        "wszystkie": wszystkie,
    })
