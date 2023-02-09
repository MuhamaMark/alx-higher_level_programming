#!/usr/bin/node

const args = process.argv;
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + args[2], function (err, request) {
  if (err) throw err;
  const json = JSON.parse(request.body);
  console.log(json.title); // Print the HTML for the Google homepage.
});
