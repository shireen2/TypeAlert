console.log ('The bot is starting');

var Twit = require('twit');
var config = require ('./config');
var T = new Twit(config);

// Search Twitter for the keyword '...'
function search_tweet () {
  var params = {
    q: 'Ryerson',
    lang: 'eu' ,
    count:5
  }
  T.get('search/tweets', params, recievedData);

  function recievedData (err, data, response) {
    console.log(data);
  };

}

// Send a tweet every 1 min
 setInterval (post_tweet, 1000*60);

// Post a tweet
function post_tweet () {

  var rand = Math.floor(Math.random()*100);
  var tweet = {
    status: 'Fist time coding in node.js Here is a random number '+ rand + ' have a nice day! :)',
  }
  T.post('statuses/update', tweet, tweeted );

  function tweeted (err, data, response) {

    console.log(data);
  }
}

search_tweet();
post_tweet();
