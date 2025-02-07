request.get(`https://swapi-api.alx-tools.com/api/films/${id}`, function (err, res) {
  if (err) {
    console.log(err);
  } else {
    console.log(res.body); 
    console.log(JSON.parse(res.body).title);  
  }
});

