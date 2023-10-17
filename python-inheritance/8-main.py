#!/usr/bin/python3
Rectangle = __import__(&#39;8-rectangle&#39;).Rectangle

r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print(&quot;Rectangle: {} - {}&quot;.format(r.width, r.height))
except Exception as e:
    print(&quot;[{}] {}&quot;.format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print(&quot;[{}] {}&quot;.format(e.__class__.__name__, e))

