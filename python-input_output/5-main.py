#!/usr/bin/python3
save_to_json_file = __import__(&#39;5-save_to_json_file&#39;).save_to_json_file

filename = &quot;my_list.json&quot;
my_list = [1, 2, 3]
save_to_json_file(my_list, filename)

filename = &quot;my_dict.json&quot;
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
save_to_json_file(my_dict, filename)

try:
    filename = &quot;my_set.json&quot;
    my_set = { 132, 3 }
    save_to_json_file(my_set, filename)
except Exception as e:
    print(&quot;[{}] {}&quot;.format(e.__class__.__name__, e))

