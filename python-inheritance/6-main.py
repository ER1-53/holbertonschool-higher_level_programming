#!/usr/bin/python3
BaseGeometry = __import__(&#39;6-base_geometry&#39;).BaseGeometry

bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print(&quot;[{}] {}&quot;.format(e.__class__.__name__, e))

