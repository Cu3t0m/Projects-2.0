#!/usr/bin/env bash

#--temporary=temporary_run()
#--indefinite=indef_run()

function temporary_run () {
    echo "Running server..."
}


echo "Server is running..."
/usr/bin/env python3 manage.py runserver
