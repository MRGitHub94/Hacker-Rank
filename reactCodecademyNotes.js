// This won't compile correctly but serve as general notes to remember syntax
// and general patterns while taking the React Course

// import modules
var React = require('react');
var ReactDOM = require('react-dom');

//JSX syntax for react
var myDiv = <div className="big"> I AM A BIG DIV </div>

// render the var myDiv and attach to the html element app
ReactDOM.render(myDiv, document.getElementById('app'));


// Self-closing tags with JSX
<br /> 
img src="http://www.placekitten.com" />

// Example of JSX expressions written inside a JS file use {}

var React = require('react');
var ReactDOM = require('react-dom');

ReactDOM.render(
  <h1>{2 + 3}</h1>,
  document.getElementById('app')
); 

// shows 2+3 = 5

var React = require('react');
var ReactDOM = require('react-dom');

// Write code here:
var math = <h1>2 + 3 = {2 + 3}</h1>;


ReactDOM.render(math, document.getElementById('app'));

// can access variables while inside a JSX expresson even if those variables 
// were declared on the outside
var React = require('react');
var ReactDOM = require('react-dom');

var theBestString = 'tralalalala i am da best';

ReactDOM.render(<h1>{theBestString}</h1>, document.getElementById('app'));

// setting variable attributes

var React = require('react');
var ReactDOM = require('react-dom');

var goose = 'https://s3.amazonaws.com/codecademy-content/courses/React/react_photo-goose.jpg';

// Declare new variable here:
var gooseImg = <img src={goose} />;

ReactDOM.render(
  gooseImg,
  document.getElementById('app')
);

// JSX elements can have event listeners like HTML 
// can give a JSX element a special attribute 

function myFunc() {
    alert('Make myFunc the pFunc...');
}

<img onClick={myFunc} />

// Valid event names https://facebook.github.io/react/docs/events.html#supported-events

// Cannot inject an if statement into a JSX expression 

var React = require('react');
var ReactDOM = require('react-dom');

// this works because the if else statements are not in curly braces (not injected in between JSX tags)
if (user.age >= drinkingAge) {
  var message = (
    <h1>
      Hey, check out this alcoholic beverage!
    </h1>
  );
} else {
  var message = (
    <h1>
      Hey, check out these earrings I got at Claire's!
    </h1>
  );
}

ReactDOM.render(
  message, 
  document.getElementById('app')
);

// Another example

var React = require('react');
var ReactDOM = require('react-dom');

function coinToss () {
  // This function will randomly return either 'heads' or 'tails'.
  return Math.random() < 0.5 ? 'heads' : 'tails';
}

var pics = {
  kitty: 'https://s3.amazonaws.com/codecademy-content/courses/React/react_photo-kitty.jpg',
  doggy: 'https://s3.amazonaws.com/codecademy-content/courses/React/react_photo-puppy.jpeg'
};

// if/else statement begins here:
if (coinToss() == 'heads') {
   var img = <img src={pics.kitty}/>
       } 
else { var img = <img src={pics.doggy} />;
     
};

ReactDOM.render(img, document.getElementById('app'));


// JSX compact way to write conditionals - ternary operator 

var headline = (
  <h1>
    { age >= drinkingAge ? 'Buy Drink' : 'Do Teen Stuff' }
  </h1>
);

// in the above example, if age is greater than or equal to drinkingAge, then 
// headline will equal <h1>Buy drink</h1>. Otherwise, headline will equal
// <h1> Do teen stuff </h1>

var React = require('react');
var ReactDOM = require('react-dom');

function coinToss () {
  // Randomly return either 'heads' or 'tails'.
  return Math.random() < 0.5 ? 'heads' : 'tails';
}

var pics = {
  kitty: 'https://s3.amazonaws.com/codecademy-content/courses/React/react_photo-kitty.jpg',
  doggy: 'https://s3.amazonaws.com/codecademy-content/courses/React/react_photo-puppy.jpeg'
};

// if coinToss is heads then display kitty otherwise display doggy
var img = <img src={pics[coinToss() == 'heads' ? 'kitty' : 'doggy']} />;

ReactDOM.render(
    img, 
    document.getElementById('app')
);

// && works best in conditionals that will sometimes do an action but other 
// times will do nothing at all 

var tasty = (
  <ul>
    <li>Applesauce</li>
    { !baby && <li>Pizza</li> }
    { age > 15 && <li>Brussels Sprouts</li> }
    { age > 20 && <li>Oysters</li> }
    { age > 25 && <li>Grappa</li> }
  </ul>
);