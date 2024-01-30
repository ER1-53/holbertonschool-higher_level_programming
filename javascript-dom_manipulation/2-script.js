let addClass = document.getElementById('red_header');
addClass.addEventListener("click", function() {
  let header = document.querySelector("header");
  header.className += "red";
});
