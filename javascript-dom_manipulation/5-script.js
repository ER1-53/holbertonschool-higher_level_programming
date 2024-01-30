let element = document.getElementById("update_header");

element.addEventListener("click", function() {
	let changeTexte = document.querySelector("header");
	changeTexte.textContent = "New Header!!!";
});
