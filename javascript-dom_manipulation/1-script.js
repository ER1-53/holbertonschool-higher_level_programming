const changeColor = document.getElementById("red_header");
changeColor.addEventListener("click", function() {
  let header = document.querySelector("header");
  header.style.color = "#FF0000";
});
