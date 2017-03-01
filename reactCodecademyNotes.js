
// codecademy-content React Course

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

// .map creates a list of JSX elements 

var strings = ['Home', 'Shop', 'About Me'];
// call .map on this array of strings, and the .map call returns a new array
// <li>s 
var listItems = strings.map(function(string){
    return <li>{string}</li>;
});

// will evaluate to an array because it's the returned value of .map 
<ul>{listItems}</ul>


var React = require('react');
var ReactDOM = require('react-dom');

var people = ['Rowe', 'Prevost', 'Gare'];

var peopleLIs = people.map(function(person){
  // return statement goes here:
return <li>{person}</li>;
});

// ReactDOM.render goes here:
ReactDOM.render(<ul>{peopleLIs}</ul>, document.getElementById('app'));

// key is a JSX attribute. The value should be something unique, similar to a 
// id attribute
// React uses keys to internally keep track of lists 
// Not all lists have to have keys but a list needs to have keys if either of 
// the following are true:
    // the list-items have memory from one render to the next
    // a list's order might be shuffled

var React = require('react');
var ReactDOM = require('react-dom');

var people = ['Rowe', 'Prevost', 'Gare'];

// pass in i as well as person to add to a key parameter 
var peopleLIs = people.map(function(person, i){
  // each time a person is returned the key will change to keep uniqueness
return <li key={'person_' + i}>{person}</li>;
});

ReactDOM.render(<ul>{peopleLIs}</ul>, document.getElementById('app'));

// Every JSX element is secretly a call to React.createElement(); 
var greatestDivEver = <div>i am div</div>;

// The above code is the same as:
var greatestDivEver = React.createElement(
"div",
null,
"i am div"
);
//==============================================================================
// Your First React Component
// A component is a small, reusable chunk of code that is responsible for one job
// ReactDOM is a Javascript object that is returned
// called the React library
var React = require('react');
// for interacting with the DOM (like ReactDOM.render())
var ReactDOM = require('react-dom');

// creates a react class called MyComponentClass
// component class variable names must begin with capital letters
var MyComponentClass = React.createClass({
  render: function () {
    return <h1>Hello world</h1>;
  }
});


ReactDOM.render(
  <MyComponentClass />,
  document.getElementById('app')
);

// Every component must come from a component class 
// A component class is like a factory that creates components 
React.createClass(); // creates a component class
// takes one argument and it must be a Javascript object which provides 
// instructions explaining to your component class how to build a React component

// have to include the render function (its value is a function) 
// has to have a return statement (usually returns a JSX expression)

// To make a React component, you write a JSX element 
// give it the same name as your component class

// JSX uses capitalization to distinguish between the two (HTML and JSX)

// to call a component's render function, pass that component to ReactDOM.render
ReactDOM.render(
    <MyComponentClass />,
    document.getElementById('app')
);

//==============================================================================
// import modules
var React = require('react');
var ReactDOM = require('react-dom');

// create Component Class called QuoteMaker
var QuoteMaker = React.createClass({
  render: function () {
    return 
// multiline JSX should be wrapped with parenetheses!
    (
      <blockquote>
        <p>
          The world is full of objects, more or less interesting; I do not wish to add any more.
        </p>
        <cite>
          <a target="_blank"
            href="http://bit.ly/1WGzM4G">
            Douglas Huebler
          </a>
        </cite>
      </blockquote>
    );
  }
});

// Render QuoteMaker using React.DOM.render();
ReactDOM.render(
  <QuoteMaker />,
  document.getElementById('app')
);

// Another example

var React = require('react');
var ReactDOM = require('react-dom');

// redPanda object
var redPanda = {
  src: 'http://bit.ly/1U92LL3',
  alt: 'Red Panda',
  width:  '200px'
};


var RedPanda = React.createClass({
  render: function () {
    return (
      <div>
        <h1>Cute Red Panda</h1>
        <img 
        // call on the redPanda properties here in the React Component
          src={redPanda.src} 
          alt={redPanda.alt} 
          width={redPanda.width} />
      </div>
    );
  }
});

// render the redPanda component
ReactDOM.render(
  <RedPanda />,
  document.getElementById('app')
);

// A render function must have a return statement but it can also have simple
// calculations that need to happen right before the component renders 
var Random = React.createClass({
  render: function () {

    // First, some logic that must happen
    // before rendering:
    var n = Math.floor(Math.random()*10+1);

    // Next, a return statement
    // using that logic:
    return <h1>The number is {n}!</h1>;
  }
});

// using conditional statements inside render function 
var React = require('react');
var ReactDOM = require('react-dom');

var TodaysPlan = React.createClass({
  render: function () {
    var task;
    if (!apocalypse) {
      task = "learn React.js"
    } else {
      task = "run around"
    }

    return <h1>Today I am going to {task}!</h1>;
  }
});

ReactDOM.render(
    <TodaysPlan />,
    document.getElementById('app')
);

// Another example

var React = require('react');
var ReactDOM = require('react-dom');

var fiftyFifty = Math.random() < 0.5;

// React.createClass call begins here:
var TonightsPlan = React.createClass({
  render: function() {
  if (fiftyFifty === true) {
    return <h1>Tonight I'm going out WOOO</h1>
  } else {
    return <h1>Tonight I'm going to bed WOOO</h1> 
    }
  }
});

ReactDOM.render(<TonightsPlan />,
               document.getElementById('app'));

// this refers to the instruction object being passed to React.createClass
var IceCreamGuy = React.createClass({
  food: 'ice cream',

  render: function () {
    return <h1>I like {this.food}.</h1>;
  }
});

var React = require('react');
var ReactDOM = require('react-dom');

var MyName = React.createClass({
    // name property goes here:
name: 'whatever-your-name-is-goes-here',

  render: function () {
    return <h1>My name is {this.name}.</h1>;
  }
});

ReactDOM.render(<MyName />, document.getElementById('app'));

// Render functions often contain event listeners
render: function() {
    return (
        <div onHover={myFunc}>
        </div>
    );
}

// In React, you define event handlers as property values on the instructions
// object. 
React.createClass({
    // event handler
    myFunc: function() {
        alert('Stop it. Stop hovering.');
    },
    render: function() {
        return (
            <div onHover={this.myFunc}>
            </div>;
        );
    }
});

// Another example
var React = require('react');
var ReactDOM = require('react-dom');

var Button = React.createClass({
  scream: function () {
    alert('AAAAAAAAHHH!!!!!');
  },

  render: function () {
    return <button onClick={this.scream}>AAAAAH!</button>;
  }
});

ReactDOM.render(
<Button />, 
document.getElementById('app'));

//==============================================================================
// React apps are made out of components, but what makes React special isn't the 
// components itself but the ways components interact

var OMG = React.createClass({
    render: function() {
        return <h1> Whoa!!! </h1>;
    }
});

// Crazy renders <OMG />
var Crazy = React.createClass({
    render: function() {
        return <OMG />;
    }
});
// If you want to use a variable that's declared in a different file, then you
// have to import the file that you want. 
// this imports the entire file 
var NavBar = require('./NavBar');

// module.exports 
ar faveManifestos = {
  futurist: 'http://bit.ly/1lKuB2I',
  SCUM:     'http://bit.ly/1xWjvYc',
  cyborg:   'http://bit.ly/16sbeoI'
};
// makes it possible for the other file to reference this faveManifestos
module.exports = faveManifestos;

// in a different file, use require to import the first file
console.log(require('./Manifestos').futurist);

//==============================================================================
// Components can pass information to another component
// information that gets passed from one component to another is known as "props"

// To see a component's props object, you use the expression this.props 

render: function() {
    console.log("Props object comin' up!");

  console.log(this.props);

  console.log("That was my props object!");

  return <h1>Hello world</h1>;
}

var React = require('react');
var ReactDOM = require('react-dom');

var PropsDisplayer = React.createClass({
  render: function () {
    var stringProps = JSON.stringify(this.props);

    return (
      <div>
        <h1>CHECK OUT MY PROPS OBJECT</h1>
        <h2>{stringProps}</h2>
      </div>
    );
  }
});

// ReactDOM.render goes here:
ReactDOM.render(<PropsDisplayer />, 
   document.getElementById('app'));

// You can pass information to a React component by giving the component an 
// attribute
<MyComponent foo="bar" />
<Example message="This is some top secret info." />

// You can pass an array 
<Greeting myInfo={["top", "secret", "lol"]} />

<Greeting name="Frarthur" town="Flundon" age={2} haunted={false} />

// You will often want a component to display the information that is passed
// 1. Find the component class that is going to receive that information
// 2. Include this.props.name-of-information in that component class's render 
// function's return statement 

var React = require('react');
var ReactDOM = require('react-dom');

var Greeting = React.createClass({
  render: function () {
    return <h1>Hi there, {this.props.firstName}</h1>;
  }
});

// ReactDOM.render goes here:
ReactDOM.render(
  <Greeting firstName='Rachel' />, 
  document.getElementById('app')
);

// Pass props from component to component
module.exports = Greeting; // on the Greetings.js
// import Greeting in App.js
var React = require('react');
var ReactDOM = require('react-dom');
var Greeting = require('./Greeting');

var App = React.createClass({
  render: function () {
    return (
      <div>
        <h1>
          Hullo and, "Welcome to The Newzz," "On Line!"
        </h1>
        <Greeting name="Rachel"/>
        <article>
          Latest newzz:  where is my phone?
        </article>
      </div>
    );
  }
});

ReactDOM.render(
  <App />, 
  document.getElementById('app')
);

// You can use props to make decisions 