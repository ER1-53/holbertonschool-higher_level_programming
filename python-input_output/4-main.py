#!/usr/bin/python3
from_json_string = __import__(&#39;4-from_json_string&#39;).from_json_string

s_my_list = &quot;[1, 2, 3]&quot;
my_list = from_json_string(s_my_list)
print(my_list)
print(type(my_list))

s_my_dict = &quot;&quot;&quot;
{&quot;is_active&quot;: true, &quot;info&quot;: {&quot;age&quot;: 36, &quot;average&quot;: 3.14}, 
&quot;id&quot;: 12, &quot;name&quot;: &quot;John&quot;, &quot;places&quot;: [&quot;San Francisco&quot;, &quot;Tokyo&quot;]}
&quot;&quot;&quot;
my_dict = from_json_string(s_my_dict)
print(my_dict)
print(type(my_dict))

try:
    s_my_dict = &quot;&quot;&quot;
    {&quot;is_active&quot;: true, 12 }
    &quot;&quot;&quot;
    my_dict = from_json_string(s_my_dict)
    print(my_dict)
    print(type(my_dict))
except Exception as e:
    print(&quot;[{}] {}&quot;.format(e.__class__.__name__, e))

