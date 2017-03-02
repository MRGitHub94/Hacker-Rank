// =============================================================================
// codecademy-content React Course
// =============================================================================

// import modules
var React = require('react');
var ReactDOM = require('react-dom');

//JSX syntax for react
var myDiv = <div className="big"> I AM A BIG DIV </div>

// render the var myDiv and attach to the html element app
ReactDOM.render(myDiv, document.getElementById('app'));


// Self-closing tags with JSX
<br /> 
<img src="http://www.placekitten.com" />

// Example of JSX expressions written inside a JS file use {}
// shows 2+3 = 5

var React = require('react');
var ReactDOM = require('react-dom');

ReactDOM.render(
  <h1>{2 + 3}</h1>,
  document.getElementById('app')
); 

// Both JSX expressions and JS in React 
var React = require('react');
var ReactDOM = require('react-dom');

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

// inject a variable into the img attribute
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

ReactDOM.render(message, 
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
    } else { var img = <img src={pics.doggy} />;
     
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
  // If math.random is less than half return heads, otherwise return tails
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

// Another Example
var React = require('react');
var ReactDOM = require('react-dom');

var people = ['Rowe', 'Prevost', 'Gare'];

var peopleLIs = people.map(function(person){
return <li>{person}</li>;
});

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

// A component is a small, reusable chunk of code that is responsible for one 
// job
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
React.createClass({}); // creates a component class
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
    return (
// multiline JSX should be wrapped with parenetheses!

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
// Example - multipage example broken up by comments
// You can use props to make decisions 
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
// Home.js
var React = require('react');
var ReactDOM = require('react-dom');
var Welcome = require('./Welcome');

var Home = React.createClass({
  render: function () {
    return <Welcome name='Ludwig van Beethoven' />;
  }
});

ReactDOM.render(
  <Home />, 
  document.getElementById('app')
);
// Greeting.js
var React = require('react');
var ReactDOM = require('react-dom');

var Greeting = React.createClass({
  render: function () {
    if (this.props.signedIn == false) {
      return <h1>GO AWAY</h1>;
    } else {
      return <h1>Hi there, {this.props.name}!</h1>;
    }
  }
});

module.exports = Greeting;
// App.js
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
        // the signedIn prop determines what message Greeting.js renders
        <Greeting name="Alison" signedIn={true}/>
        <article>
          Latest:  where is my phone?
        </article>
      </div>
    );
  }
});

ReactDOM.render(
  <App />, 
  document.getElementById('app')
);

// Put an Event Handler in a Component Class
// You have to define an event handler before you can pass one anywhere
// You define an vent handler as a property on the instructions object, 
// just like the render function

var React = require('react');

var Example = React.createClass({
// this is an event handler right here!
  handleEvent: function () {
    alert('I am an event handler.'
    + '  If you see this message,'
    + ' then I have been called.');
  },

  render: function () {
    return (
      <h1 onClick={this.handleEvent}>
        Hello world
      </h1>
    );
  }
});

// Another example
var React = require('react');
var ReactDOM = require('react-dom');
var Button = require('./Button');

var Talker = React.createClass({
  talk: function () {
  for (var speech = '', i = 0; i < 10000; i++) {
    speech += 'blah ';
  }
  alert(speech);
},

  render: function () {
    return <Button />;
  }
});

ReactDOM.render(
  <Talker />,
  document.getElementById('app')
);
// Pass an Event Handler as a prop
var React = require('react');
var ReactDOM = require('react-dom');
var Button = require('./Button');

var Talker = React.createClass({
  talk: function () {
    for (var speech = '', i = 0; i < 10000; i++) {
      speech += 'blah ';
    }
    alert(speech);
  },
  
  render: function () {
    // pass the event handler as a prop
    // need {this.talk}
    return <Button talk={this.talk} />;
  }
});

ReactDOM.render(
  <Talker />,
  document.getElementById('app')
);
// Button.js renders a <button></button>
// Need to attach talk to the button as an event handler
// You can give that JSX element a special attribute onClick or onHover
// The value should be the event handler that you want to attach
// Button.js (Talker.js is the code snippet above - both interact so that when 
// the user clicks the button the alert box appears)
var React = require('react');

var Button = React.createClass({
  render: function () {
    return (
        // the value is this.props.talk since it's in a different file
      <button onClick={this.props.talk}>
        Click me!
      </button>
    );
  }
});

// handleEvent, onEvent, and this.props.onEvent
// Two names that you can choose this.props.talk
// Both naming choices occur in the parent component class (which means the 
// the component class that defines the event handler and passes it.)

// Your prop name should be the word on plus your event type (ie. onClick)
React.createClass({
  handleHover: function () {
    alert('I am an event handler.');
    alert('I will listen for a "hover" event.');
  },

  render: function () {
    return <Child onHover={this.handleHover} />;
  }
});
module.exports = Button;
// Talker.js using proper naming conventions
var React = require('react');
var ReactDOM = require('react-dom');
var Button = require('./Button');

var Talker = React.createClass({
  handleClick: function () {
    for (var speech = '', i = 0; i < 10000; i++) {
      speech += 'blah ';
    }
    alert(speech);
  },
  
  render: function () {
    return <Button onClick={this.handleClick} />;
  }
});

ReactDOM.render(
  <Talker />,
  document.getElementById('app')
);
//Button.js using proper naming conventions
var React = require('react');

var Button = React.createClass({
  render: function () {
    return (
      <button onClick={this.props.onClick}>
        Click me!
      </button>
    );
  }
});

module.exports = Button;

// this.props.children
// Every component's props object has a property named children 
// this.props.children will return everything in between a component's opening
// and closing JSX tags

// <MyComponentClass /> == <MyComponentClass> </MyComponentClass>

// If a component has more than one child between its JSX tags, then 
// this.props.children will return those children in an array. However if a 
// component has only one child, then this.props.children will return the single
// child, not wrapped in an array

// Example of this:
// App.js
var React = require('react');
var ReactDOM = require('react-dom');
var List = require('./List');

var App = React.createClass({
  render: function () {
    return (
      <div>
        <List type='Living Musician'>
          <li>Sachiko M</li>
          <li>Harvey Sid Fisher</li>
        </List>
        <List type='Living Cat Musician'>
          <li>Nora the Piano Cat</li>
        </List>
      </div>
    );
  }
});

ReactDOM.render(
  <App />, 
  document.getElementById('app')
);
// List.js
var React = require('react');

var List = React.createClass({
  render: function () {
    var titleText = 'Favorite ' + this.props.type;
    if (this.props.children instanceof Array) {
        titleText += 's';
    }
    return (
      <div>
        <h1>{titleText}</h1>
        <ul>{this.props.children}</ul>
      </div>
    );
  }
});

module.exports = List;

//getDefaultProps
// A <button>{this.props.text}</button> expects this.props.text but if you don't
// have text in props, then it won't render any text on the button. You can 
// change this by writing a function named getDefaultProps
var Example = React.createClass({
    getDefaultProps: function() {
    // returns an object
    return { text: 'yo'};
},
    render: function() {
        return <h1>{this.props.text}</h1>;
    }
});

//Button.js
var React = require('react');
var ReactDOM = require('react-dom');

var Button = React.createClass({
  getDefaultProps: function() {
    return {text: 'I am a button'};
  },
  render: function () {
    return (
      <button>
        {this.props.text}
      </button>
    );
  }
});

ReactDOM.render(
  <Button text="" />, 
  document.getElementById('app')
);

//==============================================================================
// this.state
// Unlike props, a component's state is not passed in from the outside. A 
// component decides its own state

var Example = React.createClass({
    getInitialState: function() {
        return {mood: 'decent'};
    },
    render: function() {
        return <div></div>;
    }
});

<Example />

// To read a component's state, use the expression this.state.name-of-property
var TodayImFeeling = React.createClass({
    getInitialState: function() {
        return {mood: 'decent'};
    },
    render: function() {
        return (
            <h1> 
            I'm feeling {this.state.mood}!
            </h1>
        );
    }
});
// Another example
var React = require('react');
var ReactDOM = require('react-dom');

var App = React.createClass({
  getInitialState: function() {
    return { title: 'Best App'};
  },
  render: function () {
    return (
      <h1>
        {this.state.title}
      </h1>
    );
  }
});

ReactDOM.render(<App />,
        document.getElementById('app'));

// A component can also change its own state by calling the function this.setState
var Example = React.createClass({
  getInitialState: function () {
    return {
      mood:   'great',
      hungry: false
    };
  },

  render: function () {
    return <div></div>;
  }
});

<Example />

// The most common way to call this.setState is to call a custom function that
// wraps a this.setState call 

var Example = React.createClass({
    getInitialState: function() {
        return { weather: 'sunny' };
    },
    makeSomeFog: function() {
        this.setState({
            weather: 'foggy'
        });
    }
});

// Another Example
// 1. User triggers an event 
// 2. The event from step 1 is being listened for 
// 3. When this listened-for event occurs, it calls an event handler function 
// In this case it is toggleMood()
// 4. Inside of the body of the event handler, this.setState is called 
// 5. The component's state changes!
var React = require('react');
var ReactDOM = require('react-dom');

var Mood = React.createClass({
  getInitialState: function () {
    return {
      mood: 'good'    
    };
  },

  toggleMood: function () {
    // newMood equals the opposite of this.state.mood
    // if this.state.mood is good then newMood would be bad and vice versa
    var newMood = this.state.mood == 'good' ? 'bad' : 'good';
    // this event handler is called once the button is pressed
    this.setState({ mood: newMood });
  },

  render: function () {
    return (
      <div>
        <h1>I'm feeling {this.state.mood}!</h1>
        // user clicks the button
        <button onClick={this.toggleMood}>
          Click Me
        </button>
      </div>
    );
  }
});

ReactDOM.render(<Mood />, document.getElementById('app'));

// Another Example
var React = require('react');
var ReactDOM = require('react-dom');

var green = '#39D1B4';
var yellow = '#FFD712';

var Toggle = React.createClass({
  getInitialState: function() {
    return { color: green };
  },
  changeColor: function() {
    var newColor = this.state.color == green ? yellow : green;
    this.setState({ color: newColor });
  },
  render: function () {
    return (
      <div style={{background: this.state.color}}>
        <h1>
          Change my color
        </h1>
        <button onClick={this.changeColor}>
          Change color
        </button>
      </div>
    );
  }
});

ReactDOM.render(<Toggle />,
               document.getElementById('app'));

// Any time that you call this.setState, this.setState automatically calls 
// render as soon as the state has changed

//==============================================================================
// REACT Part II 
//==============================================================================
// Stateless components inherit from stateful components
// Stateful describes any component that has a getInitialState function
// Stateless describes any component that does not have a getInitial function

// Stateful component class
var React = require('react');
var ReactDOM = require('react-dom');
var Child = require('./Child');

var Parent = React.createClass({
  getInitialState: function() {
    return {name: 'Frarthur'};
  },
  render: function() {
    return <Child name={this.state.name} />;
  }
})

ReactDOM.render(<Parent />,
               document.getElementById('app'));
// Stateless component class
var React = require('react');

var Child = React.createClass({
  render: function() {
    return <h1>Hey, my name is {this.props.name}!</h1>;
  }
})
// Since Parent is going to render a Child, you need module.exports at the bottom
// of Child.js
module.exports = Child;

//==============================================================================
// Child components update their parents' state
// 1. The parent component class defines a functin that calls this.setState
var React = require('react');
var ReactDOM = require('react-dom');
var ChildClass = require('./ChildClass');

var ParentClass = React.createClass({
  getInitialState: function () {
    return { totalClicks: 0 };
  },

  handleClick: function () {
    var total = this.state.totalClicks;

    // calling handleClick will 
    // result in a state change:
    this.setState(
      { totalClicks: total + 1 }
    );
  }
});

// 2. Once the parent has defined a function that updates its state, the parent 
// then pass that function down to a child. 

var React = require('react');
var ReactDOM = require('react-dom');
var ChildClass = require('./ChildClass');

var ParentClass = React.createClass({
  getInitialState: function () {
    return { totalClicks: 0 };
  },

  handleClick: function () {
    var total = this.state.totalClicks;
    this.setState(
      { totalClicks: total + 1 }
    );
  },

  // The stateful component class passes down
  // handleClick to a stateless component class:
  render: function () {
    return (
      <ChildClass onClick={this.handleClick} />
    );
  }
});

// 3. The child receives the passed-down function, and uses it as an event 
// handler 
var React = require('react');
var ReactDOM = require('react-dom');

var ChildClass = React.createClass({
  render: function () {
    return (

      // The stateless component class uses 
      // the passed-down handleClick function, 
      // accessed here as this.props.onClick,
      // as an event handler:
      <button onClick={this.props.onClick}>
        Click Me!
      </button>
    );
  }
});

module.exports = ChildClass;

// Parent.js When you click on the select, the name will change in the <h1></h1>
var React = require('react');
var ReactDOM = require('react-dom');
var Child = require('./Child');

var Parent = React.createClass({
  getInitialState: function () {
    return { name: 'Frarthur' };
  },
  
  changeName: function (newName) {
    this.setState({
      name: newName
    });
  },

  render: function () {
    return (
        <Child 
            name={this.state.name} 
        onChange={this.changeName} />
    );
  }
});

ReactDOM.render(
    <Parent />, 
    document.getElementById('app')
);
// Child.js
var React = require('react');

var Child = React.createClass({
    // this function is needed to update the view to the this.props.name
  handleChange: function (e) {
    var name = e.target.value;
    this.props.onChange(name);
  },
  
  render: function () {
    return (
      <div>
        <h1>
          Hey my name is {this.props.name}!
        </h1>
        <select 
          id="great-names" 
          onChange={this.handleChange} >
          <option value="Frarthur">
            Frarthur
          </option>

          <option value="Gromulus">
            Gromulus
          </option>

          <option value="Thinkpiece">
            Thinkpiece
          </option>
        </select>
      </div>
    );
  }
});

module.exports = Child;

//==============================================================================
// Child components update their sibling components

// You will have one stateless component display information, and a diffrent 
// stateless component offer the ability to change that information

// Parent.js Child.js Sibling.js

// Parent.js
var React = require('react');
var ReactDOM = require('react-dom');
var Child = require('./Child');
var Sibling = require('./Sibling');

var Parent = React.createClass({
  getInitialState: function () {
    return { name: 'Frarthur' };
  },
  // Stateful component class that defines a function that calls this.setState
  changeName: function (newName) {
    this.setState({
      name: newName
    });
  },

  render: function () {
    return (
      <div>
      // passes the stateful component to a stateless component
        <Child onChange={this.changeName} />
        <Sibling name={this.state.name}/>
      </div>
    );
  }
});

ReactDOM.render(
  <Parent />,
  document.getElementById('app')
);
// Child.js
var React = require('react');

var Child = React.createClass({
  // the stateless component class that calls the passed-down function and can 
  // take an event object as an argument 
  handleChange: function (e) {
    var name = e.target.value;
    this.props.onChange(name);
  },
  
  render: function () {
    return (
      <div>
        <select 
          id="great-names" 
          // uses it as an event handler  
          onChange={this.handleChange}>
          
          <option value="Frarthur">Frarthur</option>
          <option value="Gromulus">Gromulus</option>
          <option value="Thinkpiece">Thinkpiece</option>
        </select>
      </div>
    );
  }
});

module.exports = Child;
//Sibling.js
var React = require('react');

var Sibling = React.createClass({
  render: function () {
    // stateless component class takes the name from Parent and displays the way
    // the change it
    var name = this.props.name;
    return (
      <div>
        <h1>Hey, my name is {name}!</h1>
        <h2>Don't you think {name} is the prettiest name ever?</h2>
        <h2>Sure am glad that my parents picked {name}!</h2>
      </div>
    );
  }
});

module.exports = Sibling;

//==============================================================================
// Style in React
// Dividing components into presentational components and container components

// Inline styles, the {{ }} 
// - the outer {} inject Javascript into JSX 
// - the inner {} create a Javascript object literal
<h1 style={{ color: 'red' }}> Hello world </h1>

// Another example 
var React = require('react');
var ReactDOM = require('react-dom');

var styleMe = <h1 style={{ background: 'lightblue', color: 'darkred' }}>Please style me!  I am so bland!</h1>;

ReactDOM.render(
    styleMe, 
    document.getElementById('app')
);

// An alternative to inline styling is to store a style object in a variable, 
// and then inject that variable into JSX


var styles = {
  color: 'darkcyan',
  background: 'mintcream'
};

// A full example
var React = require('react');
var ReactDOM = require('react-dom');
var styles = {
  background: 'lightblue',
  color: 'darkred',
  // px is assumed so the numbers don't have to be in strings
  marginTop: 100,
  fontSize: 50
};

// the attribute is no longer double curly braces!
var styleMe = <h1 style={styles}>Please style me!  I am so bland!</h1>;

ReactDOM.render(
    styleMe, 
    document.getElementById('app')
);

// In React, if you want to write a style value as a number, then the unit "px" 
// is assumed

// If you want to reuse styles for several different components, you can use
// module.exports

// Long example facebookStyles.js, FacebookColorThief.js, styles.js, Home.js, AttentionGrabber.js
// facebookStyles.js
var h1Style = {
  color:      styles.color,
  fontSize:   styles.fontSize,
  fontFamily: styles.fontFamily,
  padding:    styles.padding,
  margin:     0
};
// FacebookColorThief.js
var React = require('react');
var ReactDOM = require('react-dom');
var styles = require('./facebookStyles');

var divStyle = {
  backgroundColor: styles.darkBlue,
  color:           styles.white
};

var Wow = React.createClass({
  render: function () {
    return (
      <div style={divStyle}>
        Wow, I stole these colors from Facebook!
      </div>
    );
  }
});

ReactDOM.render(
    <Wow />, 
    document.getElementById('app')
);
// styles.js
var fontFamily = 'Comic Sans MS, Lucida Handwriting, cursive';
var background = 'pink url("https://media.giphy.com/media/oyr89uTOBNVbG/giphy.gif") fixed';
var fontSize   = '4em';
var padding = '45px 0';
var color  = 'green';

module.exports = {
  fontFamily: fontFamily,
  background: background,
  fontSize:   fontSize,
  padding:    padding,
  color:      color
};
// Home.js
var React = require('react');
var ReactDOM = require('react-dom');
var AttentionGrabber = require('./AttentionGrabber');
var styles = require('./styles');
var divStyle = {
  background: styles.background,
  height: '100%'
};
var Home = React.createClass({
  render: function () {
    return (
      <div style={divStyle}>
        <AttentionGrabber />
        <footer>THANK YOU FOR VISITING MY HOMEPAGE!</footer>
      </div>
    );
  }
});

ReactDOM.render(
    <Home />, 
    document.getElementById('app')
);
// AttentionGrabber.js
var React = require('react');
var styles = require('./styles');
var h1Style = {
  color:      styles.color,
  fontSize:   styles.fontSize,
  fontFamily: styles.fontFamily,
  padding:    styles.padding,
  margin:     0
};
var AttentionGrabber = React.createClass({
    render: function () {
        return <h1 style={h1Style}>WELCOME TO MY HOMEPAGE!</h1>;
    }
});

module.exports = AttentionGrabber;

//==============================================================================
// Container Components From Presentational Components

