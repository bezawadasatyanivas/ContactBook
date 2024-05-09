
import {React,useState} from 'react';
import {  useNavigate } from 'react-router-dom';


const LoginPage = ({verifyLogin}) => {

    const [email, setEmail]=useState('');
    const [password,setPassword]=useState('');

    const navigate=useNavigate();

    const submitLoginForm=(e)=>{
       
       e.preventDefault();
       console.log(email,password);

       const uselogin={
        email,
        password
       }

       console.log(uselogin);
       verifyLogin(uselogin);
       return navigate('/user');     
     
     }
     

   

  return (
   <div className='container'>
    <h2>Hello Login</h2>
    <form onSubmit={submitLoginForm}>
    <input  type='text' name='email' placeholder='enter email' 
    required value={email} onChange={(e)=>setEmail(e.target.value)}/>
    <br />
    <br />
    <input  type='password' name='password' placeholder='enter password' 
    required value={password} onChange={(e)=>setPassword(e.target.value)}/>
    <br />
    <br />
        <button type='submit'>Sign in</button>
   
    </form>

    </div>

 );
};

export default LoginPage;
