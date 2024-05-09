import './register_style.css';
import React from 'react';

class Register extends React.Component {
 
  render(){
    
    return(
      <div class="user_page">
      <h2>Register</h2>

       <form>
      <input type='text' name='username' placeholder='enter username' />
      <br />
      <br />
      <input type='text' name='email' placeholder='enter email' />
      <br />
      <br />
      <input type='password' name='password' placeholder='enter password' />
      <br />
      <br />
    
        <button>Sign up</button>
  
      </form>
      </div>
    );
  }
}

export default Register;
