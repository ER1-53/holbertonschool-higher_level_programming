fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    let listTitle = document.getElementById('list_movies');
	data.results.forEach(movie => {
		let li = document.createElement('li');
		li.textContent = movie.title;
		listTitle.appendChild(li);
	})
  })
  .catch(error => console.error(error));
