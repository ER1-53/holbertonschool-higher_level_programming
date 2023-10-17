#!/usr/bin/python3
is_kind_of_class = __import__(&#39;3-is_kind_of_class&#39;).is_kind_of_class

a = 1
if is_kind_of_class(a, int):
    print(&quot;{} comes from {}&quot;.format(a, int.__name__))
if is_kind_of_class(a, float):
    print(&quot;{} comes from {}&quot;.format(a, float.__name__))
if is_kind_of_class(a, object):
    print(&quot;{} comes from {}&quot;.format(a, object.__name__))

