import sqlite3
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from libraryapp.models import Librarian, model_factory
from ..connection import Connection


def get_librarian(librarian_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Librarian)

        db_cursor = conn.cursor()
        db_cursor.execute("""
      SELECT
          l.id,
          l.location_id,
          l.user_id,
          u.first_name,
          u.last_name,
          u.email
      FROM libraryapp_librarian l
      JOIN auth_user u on l.user_id = u.id
      WHERE l.id = ?
      """, (librarian_id,))

    return db_cursor.fetchone()


@login_required
def librarian_details(request, librarian_id):
    if request.method == "GET":
        librarian = get_librarian(librarian_id)

        template = "librarians/details.html"
        context = {
            "librarian": librarian
        }

        return render(request, template, context)
