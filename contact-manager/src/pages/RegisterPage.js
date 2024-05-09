
import React, { useState } from 'react';

import { useNavigate } from 'react-router-dom';

import { toast } from 'react-toastify';

//class RegisterPage extends React.Component {}

    
 
const RegisterPage=()=>{
    
    const [username,setUsername]=useState('');
    const [email, setEmail]=useState('');
    const [password,setPassword]=useState('');

    //const navigate=useNavigate();

    const submitRegisterForm=async(e)=>{
       
       e.preventDefault();

       try {
        const response = await fetch("/register", {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ username, email, password }),
        });
       

        const data = await response.json();
        if (response.ok) {
            toast.success(data.message); // Display success toast
            setTimeout(() => {
                window.location.href = '/login'; // Redirect to login page
            }, 5000); // Redirect after 2 seconds
        } else {
            toast.error(data.error); // Display error toast
        }
    } catch (error) {
        console.error('Error:', error);
    }
    };
       
    return(
      <div className="user_page">
      <h2>Register</h2>

       <form onSubmit={submitRegisterForm}>
      <input type='text' name='username' placeholder='enter username' 
          required value={username} onChange={(e)=>setUsername(e.target.value)}/>
         
      <br />
      <br />
      <input type='text' name='email' placeholder='enter email' 
          required value={email} onChange={(e)=>setEmail(e.target.value)}/>

      <br />
      <br />
      <input type='password' name='password' placeholder='enter password'
          required value={password} onChange={(e)=>setPassword(e.target.value)}/>

      <br />
      <br />
    
        <button type='submit'>Sign up</button>
  
      </form>
      </div>
    );
  }


export default RegisterPage;
