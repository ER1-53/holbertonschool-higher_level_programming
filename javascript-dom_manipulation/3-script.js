let element = document.getElementById("toggle_header");

element.addEventListener("click", function() {
  let tagChange = document.querySelector("header");
  if (tagChange.classList.contains("red")) {
    tagChange.classList.remove("red");
    tagChange.classList.add("green");
  } else if (tagChange.classList.contains("green")) {
    tagChange.classList.remove("green");
    tagChange.classList.add("red");
  }
});
