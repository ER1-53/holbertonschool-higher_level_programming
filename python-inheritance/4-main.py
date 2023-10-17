#!/usr/bin/python3
inherits_from = __import__(&#39;4-inherits_from&#39;).inherits_from

a = True
if inherits_from(a, int):
    print(&quot;{} inherited from class {}&quot;.format(a, int.__name__))
if inherits_from(a, bool):
    print(&quot;{} inherited from class {}&quot;.format(a, bool.__name__))
if inherits_from(a, object):
    print(&quot;{} inherited from class {}&quot;.format(a, object.__name__))

