// creating an array and passing the number, questions, options, and answers
let questions = let questions = [
  {
    numb: 1,
    question: "What is JSX in React?",
    answer: "A. JavaScript XML",
    options: [
      "A. JavaScript XML",
      "B. JavaScript HTML",
      "C. JavaScript Extension",
      "D. JavaScript Syntax"
    ]
  },
  {
    numb: 2,
    question: "What is the purpose of virtual DOM in React?",
    answer: "A. To speed up the rendering process",
    options: [
      "A. To speed up the rendering process",
      "B. To manipulate the DOM directly",
      "C. To keep track of component state changes",
      "D. To reconcile changes before updating the actual DOM"
    ]
  },
  {
    numb: 3,
    question: "How can you pass data from a parent component to a child component in React?",
    answer: "A. Using props",
    options: [
      "A. Using props",
      "B. Using state",
      "C. Using context",
      "D. Using refs"
    ]
  },
  {
    numb: 4,
    question: "What is the role of setState() method in React?",
    answer: "A. To update the component's state",
    options: [
      "A. To update the component's state",
      "B. To render a component",
      "C. To define component structure",
      "D. To fetch data from an API"
    ]
  },
  {
    numb: 5,
    question: "What is a React component lifecycle method that is called after a component is rendered for the first time?",
    answer: "A. componentDidMount()",
    options: [
      "A. componentDidMount()",
      "B. componentDidUpdate()",
      "C. componentWillMount()",
      "D. componentWillUnmount()"
    ]
  },
  {
    numb: 6,
    question: "What is Node.js?",
    answer: "A. A JavaScript runtime built on Chrome's V8 JavaScript engine",
    options: [
      "A. A JavaScript runtime built on Chrome's V8 JavaScript engine",
      "B. A front-end framework for building user interfaces",
      "C. A database management system",
      "D. A CSS preprocessor"
    ]
  },
  {
    numb: 7,
    question: "What is npm?",
    answer: "A. Node Package Manager",
    options: [
      "A. Node Package Manager",
      "B. Node Process Manager",
      "C. Node Page Manager",
      "D. Node Plugin Manager"
    ]
  },
  {
    numb: 8,
    question: "What is Express.js?",
    answer: "A. A web application framework for Node.js",
    options: [
      "A. A web application framework for Node.js",
      "B. A front-end library for building user interfaces",
      "C. A CSS framework",
      "D. A database management system"
    ]
  },
  {
    numb: 9,
    question: "What is MongoDB?",
    answer: "A. A NoSQL database",
    options: [
      "A. A NoSQL database",
      "B. A front-end framework",
      "C. A programming language",
      "D. A relational database management system"
    ]
  },
  {
    numb: 10,
    question: "What is Mongoose?",
    answer: "A. An ODM library for MongoDB and Node.js",
    options: [
      "A. An ODM library for MongoDB and Node.js",
      "B. A front-end framework",
      "C. A CSS framework",
      "D. A testing framework"
    ]
  },
  {
    numb: 11,
    question: "What is the purpose of package.json in a Node.js project?",
    answer: "A. To manage project dependencies and scripts",
    options: [
      "A. To manage project dependencies and scripts",
      "B. To define HTML structure",
      "C. To store database configurations",
      "D. To define CSS styles"
    ]
  },
  {
    numb: 12,
    question: "What command is used to install dependencies listed in package.json?",
    answer: "A. npm install",
    options: [
      "A. npm install",
      "B. npm start",
      "C. npm run build",
      "D. npm run dev"
    ]
  },
  {
    numb: 13,
    question: "What is the role of middleware in Express.js?",
    answer: "A. To handle requests and responses between the client and server",
    options: [
      "A. To handle requests and responses between the client and server",
      "B. To store data in the database",
      "C. To define routes",
      "D. To style the user interface"
    ]
  },
  {
    numb: 14,
    question: "What is the purpose of CORS in web development?",
    answer: "A. To enable cross-origin resource sharing",
    options: [
      "A. To enable cross-origin resource sharing",
      "B. To style the user interface",
      "C. To manage project dependencies",
      "D. To store data in the database"
    ]
  },
  {
    numb: 15,
    question: "What is RESTful API?",
    answer: "A. An architectural style for designing networked applications",
    options: [
      "A. An architectural style for designing networked applications",
      "B. A front-end framework",
      "C. A database management system",
      "D. A CSS framework"
    ]
  },
  {
    numb: 16,
    question: "What HTTP method is used to retrieve data from a server in a RESTful API?",
    answer: "A. GET",
    options: [
      "A. GET",
      "B. POST",
      "C. PUT",
      "D. DELETE"
    ]
  },
  {
    numb: 17,
    question: "What is JWT?",
    answer: "A. JSON Web Token",
    options: [
      "A. JSON Web Token",
      "B. JavaScript Web Technology",
      "C. JavaScript Web Token",
      "D. Java Web Token"
    ]
  },
  {
    numb: 18,
    question: "What is the purpose of JWT in authentication?",
    answer: "A. To securely transmit information between parties",
    options: [
      "A. To securely transmit information between parties",
      "B. To handle requests and responses",
      "C. To define routes",
      "D. To store data in the database"
    ]
  },
  {
    numb: 19,
    question: "What is the purpose of React Router?",
    answer: "A. To enable client-side routing in a React application",
    options: [
      "A. To enable client-side routing in a React application",
      "B. To manage project dependencies",
      "C. To define routes in Express.js",
      "D. To style the user interface"
    ]
  },
  {
    numb: 20,
    question: "What is the role of Redux in a React application?",
    answer: "A. To manage global state",
    options: [
      "A. To manage global state",
      "B. To define HTML structure",
      "C. To enable server-side rendering",
      "D. To handle requests and responses"
    ]
  }
];
