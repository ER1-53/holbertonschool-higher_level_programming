#!/usr/bin/python3
write_file = __import__(&#39;1-write_file&#39;).write_file

nb_characters = write_file(&quot;my_first_file.txt&quot;, &quot;This School is so cool!\n&quot;)
print(nb_characters)

