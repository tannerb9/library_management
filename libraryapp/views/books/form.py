import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from libraryapp.models import Book, Library, model_factory
from .details import get_book
from ..connection import Connection


def get_libraries():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Library)

        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            l.id,
            l.title,
            l.address
        FROM libraryapp_library l
        """)

        return db_cursor.fetchall()


@login_required
def book_form(request):
    if request.method == 'GET':
        libraries = get_libraries()
        template = 'books/form.html'
        context = {
            'all_libraries': libraries
        }

    return render(request, template, context)


@login_required
def book_edit_form(request, book_id):

    if request.method == "GET":
        book = get_book(book_id)
        libraries = get_libraries()

        template = "books/form.html"
        context = {
            "book": book,
            "all_libraries": libraries
        }

    return render(request, template, context)
