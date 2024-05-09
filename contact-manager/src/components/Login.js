import './login_style.css';
import React from 'react';



const submitLoginForm=(e)=>{
  e.preventDefault();
}


const Login = () => {

  return (
   <div className='container'>
    <h2>Hello Login</h2>
    <form onSubmit={submitLoginForm}>
    <input  type='text' name='email' placeholder='enter email' />
    <br />
    <br />
    <input  type='password' name='password' placeholder='enter password' />
    <br />
    <br />
        <button type='submit'>Sign in</button>
   
    </form>

    </div>

 );
};

export default Login;
