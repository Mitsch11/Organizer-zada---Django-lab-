# Organizer zadań – Django

Projekt wykonany w ramach laboratoriów z technologii Django.

## Opis
Aplikacja webowa typu „Organizer zadań”, umożliwiająca zarządzanie zadaniami
z wykorzystaniem panelu administratora Django oraz widoku użytkownika.

## Funkcjonalności
- panel administratora (dodawanie, edycja i usuwanie zadań)
- statusy zadań: Do zrobienia, W trakcie, Zrobione
- priorytety: Niski, Średni, Wysoki
- terminy realizacji zadań
- podział zadań na: Zaległe, Na dziś, Nadchodzące, Zrobione, Wszystkie
- filtrowanie i wyszukiwanie zadań

## Technologie
- Python 3
- Django
- SQLite
- HTML

## Uruchomienie (Windows)
```bat
python -m venv venv
venv\Scripts\activate
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


