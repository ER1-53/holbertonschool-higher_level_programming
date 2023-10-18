#!/usr/bin/python3
to_json_string = __import__(&#39;3-to_json_string&#39;).to_json_string

my_list = [1, 2, 3]
s_my_list = to_json_string(my_list)
print(s_my_list)
print(type(s_my_list))

my_dict = { 
    &#39;id&#39;: 12,
    &#39;name&#39;: &quot;John&quot;,
    &#39;places&#39;: [ &quot;San Francisco&quot;, &quot;Tokyo&quot; ],
    &#39;is_active&#39;: True,
    &#39;info&#39;: {
        &#39;age&#39;: 36,
        &#39;average&#39;: 3.14
    }
}
s_my_dict = to_json_string(my_dict)
print(s_my_dict)
print(type(s_my_dict))

try:
    my_set = { 132, 3 }
    s_my_set = to_json_string(my_set)
    print(s_my_set)
    print(type(s_my_set))
except Exception as e:
    print(&quot;[{}] {}&quot;.format(e.__class__.__name__, e))

