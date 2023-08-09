#!/usr/bin/node

const request = require('request');

const movie_id = process.argv[2];

const movie_url = `https://swapi-api.hbtn.io/api/films/${movie_id}`;

request(movie_url, async (err, res, body) => {
  err && console.log(err);

  const charactersArray = JSON.parse(res.body).characters;
  for (const character of charactersArray) {
    await new Promise((resolve, reject) => {
      request(character, (err, res, body) => {
        err && console.log(err);

        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
