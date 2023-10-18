#!/usr/bin/python3
&quot;&quot;&quot;
12-main
&quot;&quot;&quot;
pascal_triangle = __import__(&#39;12-pascal_triangle&#39;).pascal_triangle

def print_triangle(triangle):
    &quot;&quot;&quot;
    Print the triangle
    &quot;&quot;&quot;
    for row in triangle:
        print(&quot;[{}]&quot;.format(&quot;,&quot;.join([str(x) for x in row])))


if __name__ == &quot;__main__&quot;:
    print_triangle(pascal_triangle(5))

