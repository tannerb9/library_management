import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from libraryapp.models import Library
from libraryapp.models import model_factory
from ..connection import Connection


@login_required
def library_list(request):
    if request.method == 'GET':
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

            all_libraries = db_cursor.fetchall()

            template_name = 'libraries/list.html'
            context = {
                'all_libraries': all_libraries
            }

            return render(request, template_name, context)
