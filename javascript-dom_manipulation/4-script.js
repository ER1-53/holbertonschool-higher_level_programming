let element = document.getElementById("add_item");

element.addEventListener("click", function() {
    let changeClass = document.querySelector(".my_list");
    let newItem = document.createElement("li");
    newItem.innerHTML = "item";
    changeClass.appendChild(newItem);
})
