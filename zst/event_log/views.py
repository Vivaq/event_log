import sqlite3
import os
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from models import LogAttempts, Errors, ConfigurationChanged
from forms import Filter


@csrf_exempt
def show_db(request):
    display = {'logattempts': 'none', 'errors': 'none', 'configurationchanged': 'none'}

    if request.method == 'GET':
        show_db.queries = {'logattempts': ['SELECT * FROM event_log_logattempts', '', ''],
                           'errors': ['SELECT * FROM event_log_errors', '', ''],
                           'configurationchanged': ['SELECT * FROM event_log_configurationchanged', '', '']}
        show_db.logs = LogAttempts.objects.raw(show_db.queries['logattempts'][0])
        show_db.errors = Errors.objects.raw(show_db.queries['errors'][0])
        show_db.configurations = ConfigurationChanged.objects.raw(show_db.queries['configurationchanged'][0])

    else:
        form = Filter(request.POST)
        if form.data.get('option') == 'Filter':
            (table, filter_txt) = form.data.get('filter_fields').split(':')
            if validate(filter_txt):
                show_db.queries[table][1] = " where " + filter_txt if filter_txt not in ['', ' '] else ''
            display[table] = ''

        elif form.data.get('option') == 'Delete':
            (table, delete_filter) = form.data.get('filter_fields').split(':')
            if validate(delete_filter):
                query = "DELETE FROM event_log_" + table + " where " + delete_filter
                db = sqlite3.connect(os.getcwd() + '/db.sqlite3')
                c = db.cursor()
                c.execute(query)
                db.commit()
            display[table] = ''

        else:
            sort_txt = form.data.items()[1]
            table = sort_txt[0]
            field = sort_txt[1].lower()
            show_db.queries[table][2] = ' order by ' + field
            display[table] = ''
        show_db.logs = LogAttempts.objects.raw(''.join(show_db.queries['logattempts']))
        show_db.errors = Errors.objects.raw(''.join(show_db.queries['errors']))
        show_db.configurations = ConfigurationChanged.objects.raw(''.join(show_db.queries['configurationchanged']))

    return render(
        request=request,
        template_name='event_log/LogViewer.html',
        context={
            'logs': show_db.logs.query,
            'errors': show_db.errors.query,
            'configurations': show_db.configurations.query,
            'form': Filter(),
            'display': display
        }
    )


def validate(txt):
    return False if ';' in txt else any(' ' not in field for field in ''.join(txt.split(' and ')).split(' or '))


@csrf_exempt
def add_log(request):
    to_insert = json.loads(request.body)
    record = to_insert.values()[0]

    if to_insert.keys()[0] == 'E':
        Errors(
            id=int(record[0]),
            source=record[1],
            event_date=record[2],
            why=record[3],
            danger=int(record[4]),
        ).save()

    elif to_insert.keys()[0] == 'CC':
        ConfigurationChanged(
            id=int(record[0]),
            source=record[1],
            event_date=record[2],
            description=record[3]
        ).save()

    elif to_insert.keys()[0] == 'LA':
        LogAttempts(
            id=int(record[0]),
            source=record[1],
            event_date=record[2],
            succeeded=record[3]
        ).save()

    return HttpResponse("Success")
