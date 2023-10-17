#!/usr/bin/python3
is_same_class = __import__(&#39;2-is_same_class&#39;).is_same_class

a = 1
if is_same_class(a, int):
    print(&quot;{} is an instance of the class {}&quot;.format(a, int.__name__))
if is_same_class(a, float):
    print(&quot;{} is an instance of the class {}&quot;.format(a, float.__name__))
if is_same_class(a, object):
    print(&quot;{} is an instance of the class {}&quot;.format(a, object.__name__))

