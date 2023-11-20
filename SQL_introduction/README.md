# 

<p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/272/rtcwz.jpg" alt="" loading='lazy' style="" /></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/jRAhwW4u4YvZtLtMGU2_6g" title="What is Database &amp; SQL?" target="_blank">What is Database &amp; SQL?</a> </li>
<li><a href="/rltoken/s3m_emsaSthyY041Wacgxg" title="Install MySQL (MySQL Server)" target="_blank">Install MySQL (MySQL Server)</a></li>
<li><a href="/rltoken/m_0RMf4RcC5NrHyjY1xN3w" title="A Basic MySQL Tutorial" target="_blank">A Basic MySQL Tutorial</a> </li>
<li><a href="/rltoken/-Qrnbp5eKmo7ajPDZekjfg" title="Basic SQL statements: DDL and DML" target="_blank">Basic SQL statements: DDL and DML</a> (<em>no need to read the chapter &ldquo;Privileges&rdquo;</em>)</li>
<li><a href="/rltoken/wXN5s1qexSTMh--NkTF1_w" title="Basic queries: SQL and RA" target="_blank">Basic queries: SQL and RA</a> </li>
<li><a href="/rltoken/7khGjnehvjHnqNZ9yizggg" title="SQL technique: functions" target="_blank">SQL technique: functions</a> </li>
<li><a href="/rltoken/xnJcopQTZyUke3LdAkOwow" title="SQL technique: subqueries" target="_blank">SQL technique: subqueries</a> </li>
<li><a href="/rltoken/QEr3XcBPhIR-E8NSSn1nzg" title="What makes the big difference between a backtick and an apostrophe?" target="_blank">What makes the big difference between a backtick and an apostrophe?</a> </li>
<li><a href="/rltoken/DGejihlnOkkNq-qJFM15MA" title="MySQL Cheat Sheet" target="_blank">MySQL Cheat Sheet</a> </li>
<li><a href="/rltoken/ePNUeloWxfiXwec7HeKe7Q" title="MySQL 8.0 SQL Statement Syntax" target="_blank">MySQL 8.0 SQL Statement Syntax</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/6bUOgrGi5Yd_I65Jp9bAfg" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What&rsquo;s a database</li>
<li>What&rsquo;s a relational database</li>
<li>What does SQL stand for</li>
<li>What&rsquo;s MySQL</li>
<li>How to create a database in MySQL</li>
<li>What does <code>DDL</code> and <code>DML</code> stand for</li>
<li>How to <code>CREATE</code> or <code>ALTER</code> a table</li>
<li>How to <code>SELECT</code> data from a table</li>
<li>How to <code>INSERT</code>, <code>UPDATE</code> or <code>DELETE</code> data</li>
<li>What are <code>subqueries</code></li>
<li>How to use MySQL functions</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be executed on Ubuntu 20.04 LTS using <code>MySQL 8.0</code> (version 8.0.25)</li>
<li>All your files should end with a new line</li>
<li>All your SQL queries should have a comment just before (i.e. syntax above)</li>
<li>All your files should start by a comment describing the task</li>
<li>All SQL keywords should be in uppercase (<code>SELECT</code>, <code>WHERE</code>&hellip;)</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

<h2>More Info</h2>

<h3>Comments for your SQL file:</h3>

<pre><code>$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
</code></pre>

<h3>Install MySQL 8.0 on Ubuntu 20.04 LTS</h3>

<pre><code>$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
</code></pre>

<p>Connect to your MySQL server:</p>

<pre><code>$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type &#39;help;&#39; or &#39;\h&#39; for help. Type &#39;\c&#39; to clear the current input statement.

mysql&gt;
mysql&gt; quit
Bye
$
</code></pre>

<h3>Use the sandbox to run MySQL</h3>

<p><strong>In the container, credentials are <code>root/root</code></strong></p>

<ul>
<li>Ask for container <code>Ubuntu 20.04</code></li>
<li>Connect via SSH</li>
<li>OR connect via the Web terminal</li>
<li>In the container, you should start MySQL before playing with it:</li>
</ul>

<pre><code>$ service mysql start                                                   
* Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$
</code></pre>

<p><strong>In the container, credentials are <code>root/root</code></strong></p>


<details>
<summary>Click to see: Tasks</summary>

<h3 class="panel-title">
0. List databases
</h3>

Write a script that lists all databases of your MySQL server.</p>

<pre><code>guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database                                                                                     
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys        
guillaume@ubuntu:~/$ 
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>SQL_introduction</code></li>
<li>File: <code>0-list_databases.sql</code></li>
</ul>
</div>

<h3 class="panel-title">
1. Create a database
</h3>

Write a script that creates the database <code>hbtn_0c_0</code> in your MySQL server.</p>

<ul>
<li>If the database <code>hbtn_0c_0</code> already exists, your script should not fail</li>
<li>You are not allowed to use the <code>SELECT</code> or <code>SHOW</code> statements</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database
information_schema
hbtn_0c_0
mysql
performance_schema
guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ 
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>SQL_introduction</code></li>
<li>File: <code>1-create_database_if_missing.sql</code></li>
</ul>
</div>

<h3 class="panel-title">
2. Delete a database
</h3>

Write a script that deletes the database <code>hbtn_0c_0</code> in your MySQL server.</p>

<ul>
<li>If the database <code>hbtn_0c_0</code> doesn&rsquo;t exist, your script should not fail</li>
<li>You are not allowed to use the <code>SELECT</code> or <code>SHOW</code> statements</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database                                                                                     
hbtn_0c_0                                                                                    
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys        
guillaume@ubuntu:~/$ cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database                                                                                                                                                                  
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys        
guillaume@ubuntu:~/$ 
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>SQL_introduction</code></li>
<li>File: <code>2-remove_database.sql</code></li>
</ul>
</div>

<h3 class="panel-title">
3. List tables
</h3>

Write a script that lists all the tables of a database in your MySQL server.</p>

<ul>
<li>The database name will be passed as argument of <code>mysql</code> command (in the following example: <code>mysql</code> is the name of the database)</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
Enter password: 
Tables_in_mysql                                                                              
columns_priv                                                                                 
component                                                                                    
db                                                                                           
default_roles                                                                                
engine_cost                                                                                  
func                                                                                         
general_log                                                                                  
global_grants                                                                                
gtid_executed                                                                                
help_category                                                                                
help_keyword                                                                                 
help_relation                                                                                
help_topic                                                                                   
innodb_index_stats                                                                           
innodb_table_stats                                                                           
password_history                                                                             
plugin                                                                                       
procs_priv                                                                                   
proxies_priv                                                                                 
replication_asynchronous_connection_failover                                                 
replication_asynchronous_connection_failover_managed                                         
role_edges                                                                                   
server_cost                                                                                  
servers                                                                                      
slave_master_info                                                                            
slave_relay_log_info                                                                         
slave_worker_info                                                                            
slow_log                                                                                     
tables_priv                                                                                  
time_zone                                                                                    
time_zone_leap_second                                                                        
time_zone_name                                                                               
time_zone_transition                                                                         
time_zone_transition_type                                                                    
user
guillaume@ubuntu:~/$ 
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>SQL_introduction</code></li>
<li>File: <code>3-list_tables.sql</code></li>
</ul>
</div>

<h3 class="panel-title">
4. First table
</h3>

Write a script that creates a table called <code>first_table</code> in the current database in your MySQL server.</p>

<ul>
<li><code>first_table</code> description:

<ul>
<li><code>id</code> INT</li>
<li><code>name</code> VARCHAR(256)</li>
</ul></li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
<li>If the table <code>first_table</code> already exists, your script should not fail</li>
<li>You are not allowed to use the <code>SELECT</code> or <code>SHOW</code> statements</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Tables_in_hbtn_0c_0
first_table
guillaume@ubuntu:~/$ 
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>SQL_introduction</code></li>
<li>File: <code>4-first_table.sql</code></li>
</ul>
</div>

<h3 class="panel-title">
5. Full description
</h3>

Write a script that prints the following description of the table <code>first_table</code> from the database <code>hbtn_0c_0</code> in your MySQL server.</p>

<ul>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
<li>You are not allowed to use the <code>DESCRIBE</code> or <code>EXPLAIN</code> statements</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Table   Create Table                                                                         
first_table     CREATE TABLE `first_table` (\n  `id` int DEFAULT NULL,\n  `name` varchar(256) DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci        
guillaume@ubuntu:~/$ 
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>SQL_introduction</code></li>
<li>File: <code>5-full_table.sql</code></li>
</ul>
</div>

<h3 class="panel-title">
6. List all in table
</h3>

Write a script that lists all rows of the table <code>first_table</code> from the database <code>hbtn_0c_0</code> in your MySQL server.</p>

<ul>
<li>All fields should be printed</li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ 
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>SQL_introduction</code></li>
<li>File: <code>6-list_values.sql</code></li>
</ul>
</div>

<h3 class="panel-title">
7. First add
</h3>

Write a script that inserts a new row in the table <code>first_table</code> (database <code>hbtn_0c_0</code>) in your MySQL server.</p>

<ul>
<li>New row:

<ul>
<li><code>id</code> = <code>89</code></li>
<li><code>name</code> = <code>Best School</code></li>
</ul></li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
id  name
89  Best School
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
id  name
89  Best School
89  Best School
89  Best School
guillaume@ubuntu:~/$ 
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>SQL_introduction</code></li>
<li>File: <code>7-insert_value.sql</code></li>
</ul>
</div>

<h3 class="panel-title">
8. Count 89
</h3>

Write a script that displays the number of records with <code>id = 89</code> in the table <code>first_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>

<ul>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
Enter password: 
3
guillaume@ubuntu:~/$ 
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>SQL_introduction</code></li>
<li>File: <code>8-count_89.sql</code></li>
</ul>
</div>

<h3 class="panel-title">
9. Full creation
</h3>

Write a script that creates a table <code>second_table</code> in the database <code>hbtn_0c_0</code> in your MySQL server and add multiples rows.</p>

<ul>
<li><code>second_table</code> description:

<ul>
<li><code>id</code> INT</li>
<li><code>name</code> VARCHAR(256)</li>
<li><code>score</code> INT</li>
</ul></li>
<li>The database name will be passed as an argument to the <code>mysql</code> command</li>
<li>If the table <code>second_table</code> already exists, your script should not fail</li>
<li>You are not allowed to use the <code>SELECT</code> and <code>SHOW</code> statements</li>
<li>Your script should create these records:

<ul>
<li><code>id</code> = 1, <code>name</code> = &ldquo;John&rdquo;, <code>score</code> = 10</li>
<li><code>id</code> = 2, <code>name</code> = &ldquo;Alex&rdquo;, <code>score</code> = 3</li>
<li><code>id</code> = 3, <code>name</code> = &ldquo;Bob&rdquo;, <code>score</code> = 14</li>
<li><code>id</code> = 4, <code>name</code> = &ldquo;George&rdquo;, <code>score</code> = 8</li>
</ul></li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ 
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>SQL_introduction</code></li>
<li>File: <code>9-full_creation.sql</code></li>
</ul>
</div>

<h3 class="panel-title">
10. List by best
</h3>

Write a script that lists all records of the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>

<ul>
<li>Results should display both the score and the name (in this order)</li>
<li>Records should be ordered by score (top first) </li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
14  Bob
10  John
8   George
3   Alex
guillaume@ubuntu:~/$ 
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>SQL_introduction</code></li>
<li>File: <code>10-top_score.sql</code></li>
</ul>
</div>

<h3 class="panel-title">
11. Select the best
</h3>

Write a script that lists all records with a <code>score &gt;= 10</code> in the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>

<ul>
<li>Results should display both the score and the name (in this order)</li>
<li>Records should be ordered by score (top first)</li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
14  Bob
10  John
guillaume@ubuntu:~/$ 
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>SQL_introduction</code></li>
<li>File: <code>11-best_score.sql</code></li>
</ul>
</div>

<h3 class="panel-title">
12. Cheating is bad
</h3>

Write a script that updates the score of Bob to <code>10</code> in the table <code>second_table</code>.</p>

<ul>
<li>You are not allowed to use Bob&rsquo;s id value, only the <code>name</code> field</li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
10  John
10  Bob
8   George
3   Alex
guillaume@ubuntu:~/$ 
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>SQL_introduction</code></li>
<li>File: <code>12-no_cheating.sql</code></li>
</ul>
</div>

<h3 class="panel-title">
13. Score too low
</h3>

Write a script that removes all records with a <code>score &lt;= 5</code> in the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>

<ul>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 13-change_class.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
10  John
10  Bob
8   George
guillaume@ubuntu:~/$ 
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>SQL_introduction</code></li>
<li>File: <code>13-change_class.sql</code></li>
</ul>
</div>

<h3 class="panel-title">
14. Average
</h3>

Write a script that computes the score average of all records in the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>

<ul>
<li>The result column name should be <code>average</code></li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
average
9.3333
guillaume@ubuntu:~/$ 
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>SQL_introduction</code></li>
<li>File: <code>14-average.sql</code></li>
</ul>
</div>

<h3 class="panel-title">
15. Number by score
</h3>

Write a script that lists the number of records with the same score in the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>

<ul>
<li>The result should display:

<ul>
<li>the <code>score</code></li>
<li>the number of records for this <code>score</code> with the label <code>number</code></li>
</ul></li>
<li>The list should be sorted by the number of records (descending)</li>
<li>The database name will be passed as an argument to the <code>mysql</code> command</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   number
10  2
8   1
guillaume@ubuntu:~/$ 
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>SQL_introduction</code></li>
<li>File: <code>15-groups.sql</code></li>
</ul>
</div>

<h3 class="panel-title">
16. Say my name
</h3>

Write a script that lists all records of the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>

<ul>
<li>Don&rsquo;t list rows without a <code>name</code> value</li>
<li>Results should display the score and the name (in this order)</li>
<li>Records should be listed by descending score </li>
<li>The database name will be passed as an argument to the <code>mysql</code> command</li>
</ul>

<p>In this example, new data have been added to the table <code>second_table</code>.</p>

<pre><code>guillaume@ubuntu:~/$ cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
18  Aria
12  Aria
10  John
10  Bob
guillaume@ubuntu:~/$ 
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>SQL_introduction</code></li>
<li>File: <code>16-no_link.sql</code></li>
</ul>
</div>

</details>
