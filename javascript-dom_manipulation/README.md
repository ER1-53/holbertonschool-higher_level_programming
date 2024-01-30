# JS DOM manipulation

<h1>JavaScript DOM Manipulation</h1>

<h2>Resources</h2>

<h3>Read or watch:</h3>

<ul>
<li><a href="/rltoken/J3eODWe9y3RX1szVXZrD4Q" title="What is JavaScript?" target="_blank">What is JavaScript?</a></li>
<li><a href="/rltoken/R6U3tUAdKDqDDhsYJw1JrQ" title="Introduction to the DOM" target="_blank">Introduction to the DOM</a></li>
<li><a href="/rltoken/VBwvMfwoElIcvVa-Rc9LJg" title="Document Interface" target="_blank">Document Interface</a></li>
<li><a href="/rltoken/3f2toV3UxRn01mxEV3o9Xg" title="Element Class" target="_blank">Element Class</a></li>
<li><a href="/rltoken/xiqFAXX9ZYKHQ0R_STL9Tg" title="Locating DOM elements using selectors" target="_blank">Locating DOM elements using selectors</a></li>
<li><a href="/rltoken/wpSFF7uL4ZQJ5LE3PXI5Uw" title="CSS Selectors" target="_blank">CSS Selectors</a></li>
<li><a href="/rltoken/GunCAsRgUiuvrDkp07w6jw" title="CSS Diner" target="_blank">CSS Diner</a> Play with Selectors</li>
<li><a href="/rltoken/gj5edptaWMeVZXkfPnzvPA" title="Client-side Web APIs" target="_blank">Client-side Web APIs</a>

<ul>
<li><a href="/rltoken/MXI686trnIVFrvaIig5JWw" title="Introduction to web APIs" target="_blank">Introduction to web APIs</a></li>
<li><a href="/rltoken/J98Ezd-CKsVoI4TYPNbVeA" title="Manipulating documents" target="_blank">Manipulating documents</a></li>
<li><a href="/rltoken/iFjVRw0SGECiqfJlcG-ONQ" title="Fetching data from the server" target="_blank">Fetching data from the server</a></li>
</ul></li>
<li><a href="/rltoken/zaVe3KcXBF2woAXTo9TQCA" title="What went wrong? Troubleshooting JavaScript" target="_blank">What went wrong? Troubleshooting JavaScript</a></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/pGqFy8d950j1zgO0VJQEPA" title="explain to anyone" target="_blank">explain to anyone</a>, without the help of Google:</p>

<h3>General</h3>

<ul>
<li>How to select HTML elements in JavaScript</li>
<li>What are differences between ID, class and tag name selectors</li>
<li>How to modify an HTML element style</li>
<li>How to get and update an HTML element content</li>
<li>How to modify the DOM</li>
<li>How to make a request with XmlHTTPRequest</li>
<li>How to make a request with Fetch API</li>
<li>How to listen/bind to DOM events</li>
<li>How to listen/bind to user events</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: All of them.</li>
<li>All your files will be interpreted on Chrome browser (version 57.0 or later)</li>
<li>All your files should end with a new line</li>
<li>A mandatory <code>README.md</code> file with meaningful information about the content, should be placed at the root folder of the project.</li>
<li>Your code should be <code>semistandard</code> compliant</li>
<li>You are not allowed to use var</li>
<li>HTML should not reload for each action: DOM manipulation, update values, fetch data…</li>
</ul>


<details>
<summary>Click to see: Tasks</summary>

<h3 class="panel-title">
0. Color Me
</h3>

Write a JavaScript script that updates the text color of the <code>header</code> element to red (<code>#FF0000</code>):</p>

<ul>
<li>You must use <code>document.querySelector</code> to select the HTML tag</li>
</ul>

<p>Please test with this HTML file in your browser:</p>

<pre><code>javiercito@ubuntu:~/javascript-dom_manipulation$ cat 0-main.html
<!DOCTYPE html>
<html lang="en">
<head>
<title>Holberton School</title>
</head>
<body>
<header>
First HTML page
</header>
<footer>
Holberton School - 2022
</footer>
<script type="text/javascript" src="0-script.js"></script>
</body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>javascript-dom_manipulation</code></li>
<li>File: <code>0-script.js</code></li>
</ul>
</div>

<h3 class="panel-title">
1. Click and turn red
</h3>

Write a JavaScript script that updates the text color of the <code>header</code> element to red (<code>#FF0000</code>) when the user clicks on the tag with id <code>red_header</code>:</p>

<p>Please test with this HTML file in your browser:</p>

<pre><code>javiercito@ubuntu:~/javascript-dom_manipulation$ cat 1-main.html
<!DOCTYPE html>
<html lang="en">
<head>
<title>Holberton School</title>
</head>
<body>
<header>
First HTML page
</header>
<div id="red_header">Red header</div>
<footer>
Holberton School - 2022
</footer>
<script type="text/javascript" src="1-script.js"></script>
</body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>javascript-dom_manipulation</code></li>
<li>File: <code>1-script.js</code></li>
</ul>
</div>

<h3 class="panel-title">
2. Add `.red` class
</h3>

Write a JavaScript script that adds the class <code>red</code> to the <code>header</code> element when the user clicks on the tag with id <code>red_header</code></p>

<p>Please test with this HTML file in your browser:</p>

<pre><code>javiercito@ubuntu:~/javascript-dom_manipulation$ cat 2-main.html
<!DOCTYPE html>
<html lang="en">
<head>
<title>Holberton School</title>
<style>
.red {
color: #FF0000;
}
</style>
</head>
<body>
<header>
First HTML page
</header>
<div id="red_header">Red header</div>
<footer>
Holberton School - 2022
</footer>
<script type="text/javascript" src="2-script.js"></script>
</body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>javascript-dom_manipulation</code></li>
<li>File: <code>2-script.js</code></li>
</ul>
</div>

<h3 class="panel-title">
3. Toggle classes
</h3>

Write a JavaScript script that toggles the class of the <code>header</code> element when the user clicks on the tag id <code>toggle_header</code>:</p>

<p>The <code>header</code> element must always have one class: <code>red</code> or <code>green</code>, never both in the same time and never empty.
If the current class is <code>red</code>, when the user click on id <code>toggle_header</code> element, the class must be updated to <code>green</code> ; and the reverse.</p>

<p>Please test with this HTML file in your browser:</p>

<pre><code>javiercito@ubuntu:~/javascript-dom_manipulation$ cat 3-main.html
<!DOCTYPE html>
<html lang="en">
<head>
<title>Holberton School</title>
<style>
.red {
color: #FF0000;
}
.green {
color: #00FF00;
}
</style>
</head>
<body>
<header class="green">
First HTML page
</header>
<div id="toggle_header">Toggle header</div>
<footer>
Holberton School - 2022
</footer>
<script type="text/javascript" src="3-script.js"></script>
</body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>javascript-dom_manipulation</code></li>
<li>File: <code>3-script.js</code></li>
</ul>
</div>

<h3 class="panel-title">
4. List of elements
</h3>

Write a JavaScript script that adds a <code>li</code> element to a list when the user clicks on the element with id <code>add_item</code>:</p>

<p>The new element must be: <code><li>Item</li></code>
The new element must be added to the <code>ul</code> element with class <code>my_list</code></p>

<p>Please test with this HTML file in your browser:</p>

<pre><code>javiercito@ubuntu:~/javascript-dom_manipulation$ cat 4-main.html
<!DOCTYPE html>
<html lang="en">
<head>
<title>Holberton School</title>
</head>
<body>
<header>
First HTML page
</header>
<br />
<div id="add_item">Add item</div>
<br />
<ul class="my_list">
<li>Item</li>
</ul>
<footer>
Holberton School - 2022
</footer>
<script type="text/javascript" src="4-script.js"></script>
</body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>javascript-dom_manipulation</code></li>
<li>File: <code>4-script.js</code></li>
</ul>
</div>

<h3 class="panel-title">
5. Change the text
</h3>

Write a JavaScript script that updates the text of the <code>header</code> element to <code>New Header!!!</code> when the user clicks on the element with id <code>update_header</code></p>

<p>Please test with this HTML file in your browser:</p>

<pre><code>javiercito@ubuntu:~/javascript-dom_manipulation$ cat 5-main.html
<!DOCTYPE html>
<html lang="en">
<head>
<title>Holberton School</title>
</head>
<body>
<header>
First HTML page
</header>
<br />
<div id="update_header">Update the header</div>
<br />
<footer>
Holberton School - 2022
</footer>
<script type="text/javascript" src="5-script.js"></script>
</body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>javascript-dom_manipulation</code></li>
<li>File: <code>5-script.js</code></li>
</ul>
</div>

<h3 class="panel-title">
6. Star wars character
</h3>

Write a JavaScript script that fetches the character <code>name</code> from this URL: <code>https://swapi-api.hbtn.io/api/people/5/?format=json</code></p>

<ul>
<li>The name must be displayed in the HTML tag with id <code>character</code>.</li>
<li>You must use the <a href="/rltoken/mov5LF24GCfD957vJ0i7dg" title="Fetch API" target="_blank">Fetch API</a>. </li>
<li>You probably should read something about <a href="/rltoken/sRgTVb2pzsne9C5-2xIJvQ" title="usign Promises" target="_blank">usign Promises</a> later.</li>
</ul>

<p>Please test with this HTML file in your browser:</p>

<pre><code>javiercito@ubuntu:~/javascript-dom_manipulation$ cat 6-main.html
<!DOCTYPE html>
<html lang="en">
<head>
<title>Holberton School</title>
</head>
<body>
<header>
Star Wars character
</header>
<br />
<div id="character"></div>
<br />
<footer>
Holberton School - 2022
</footer>
<script type="text/javascript" src="6-script.js"></script>
</body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>javascript-dom_manipulation</code></li>
<li>File: <code>6-script.js</code></li>
</ul>
</div>

<h3 class="panel-title">
7. Star Wars movies
</h3>

Write a JavaScript script that fetches and lists the <code>title</code> for all movies by using this URL: <code>https://swapi-api.hbtn.io/api/films/?format=json</code></p>

<ul>
<li>All movie titles must be list in the HTML <code>ul</code> element with id <code>list_movies</code></li>
<li>You must use the Fetch API.</li>
</ul>

<p>Please test with this HTML file in your browser:</p>

<pre><code>javiercito@ubuntu:~/javascript-dom_manipulation$ cat 7-main.html
<!DOCTYPE html>
<html lang="en">
<head>
<title>Holberton School</title>
</head>
<body>
<header>
Star Wars movies
</header>
<br />
<ul id="list_movies">
</ul>
<br />
<footer>
Holberton School - 2022
</footer>
<script type="text/javascript" src="7-script.js"></script>
</body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>javascript-dom_manipulation</code></li>
<li>File: <code>7-script.js</code></li>
</ul>
</div>

<h3 class="panel-title">
8. Say Hello!
</h3>

Write a JavaScript script that fetches from <code>https://hellosalut.stefanbohacek.dev/?lang=fr</code> and displays the value of <code>hello</code> from that fetch in the HTML element with id <code>hello</code>.</p>

<ul>
<li>The translation of “hello” must be displayed in the HTML element with id <code>hello</code></li>
<li>Your script must work when it is imported from the <code><head></code> tag</li>
</ul>

<p>Please test with this HTML file in your browser:</p>

<pre><code>javiercito@ubuntu:~/javascript-dom_manipulation$ cat 8-main.html
<!DOCTYPE html>
<html lang="en">
<head>
<title>Holberton School</title>
<script type="text/javascript" src="8-script.js"></script>
</head>
<body>
<header>
Say Hello!
</header>
<br />
<div id="hello"></div>
<br />
<footer>
Holberton School - 2022
</footer>
</body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>javascript-dom_manipulation</code></li>
<li>File: <code>8-script.js</code></li>
</ul>
</div>

</details>
