#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const movieEndpoint = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

function sendRequest(characterList, index) {
  if (characterList.length === index) {
    return;
  }

  request(characterList[index], (error, response, body) => {
    if (error) {
      console.error(`Error fetching character at index ${index}: ${error.message}`);
    } else if (response.statusCode !== 200) {
      console.error(`Failed to fetch character at index ${index}: ${response.statusCode}`);
    } else {
      try {
        const character = JSON.parse(body).name;
        console.log(character);
        sendRequest(characterList, index + 1);
      } catch (parseError) {
        console.error(`Error parsing character data at index ${index}: ${parseError.message}`);
      }
    }
  });
}

request(movieEndpoint, (error, response, body) => {
  if (error) {
    console.error(`Error fetching movie data: ${error.message}`);
  } else if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie data: ${response.statusCode}`);
  } else {
    try {
      const characterList = JSON.parse(body).characters;
      sendRequest(characterList, 0);
    } catch (parseError) {
      console.error(`Error parsing movie data: ${parseError.message}`);
    }
  }
});
