#!/usr/bin/python3
BaseGeometry = __import__(&#39;7-base_geometry&#39;).BaseGeometry

bg = BaseGeometry()

bg.integer_validator(&quot;my_int&quot;, 12)
bg.integer_validator(&quot;width&quot;, 89)

try:
    bg.integer_validator(&quot;name&quot;, &quot;John&quot;)
except Exception as e:
    print(&quot;[{}] {}&quot;.format(e.__class__.__name__, e))

try:
    bg.integer_validator(&quot;age&quot;, 0)
except Exception as e:
    print(&quot;[{}] {}&quot;.format(e.__class__.__name__, e))

try:
    bg.integer_validator(&quot;distance&quot;, -4)
except Exception as e:
    print(&quot;[{}] {}&quot;.format(e.__class__.__name__, e))

