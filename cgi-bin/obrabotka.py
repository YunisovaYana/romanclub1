#!/usr/bin/env python3

import cgi

our_form = cgi.FieldStorage()

in_name = our_form.getfirst("in_name", "не задано")

print("Content-type: text/html")
print()
print()

