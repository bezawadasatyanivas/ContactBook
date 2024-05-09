import './home_style.css';
import React from 'react';
import {Link} from "react-router-dom";



function Home() {
  return (
   <div>
    <h1>Welcome to Contact Book..!</h1>

    <h5>Already a user?</h5>
    <Link to="/login">
        <button>Sign in</button>
    </Link>
    
    <h5>New to our website?</h5>
    <Link to="/register">
        <button>Sign up</button>
    </Link>
    
   </div>

  
  );
}

export default Home;
