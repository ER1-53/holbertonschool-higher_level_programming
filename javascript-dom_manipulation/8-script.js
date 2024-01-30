document.addEventListener('DOMContentLoaded', function() {
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
      .then(response => response.json())
      .then(data => {
        let sayHello = document.getElementById('hello');
        sayHello.textContent = data.hello;
      })
      .catch(error => console.error(error));
  });
