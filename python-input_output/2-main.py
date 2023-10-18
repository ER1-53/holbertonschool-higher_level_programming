#!/usr/bin/python3
append_write = __import__(&#39;2-append_write&#39;).append_write

nb_characters_added = append_write(&quot;file_append.txt&quot;, &quot;This School is so cool!\n&quot;)
print(nb_characters_added)

