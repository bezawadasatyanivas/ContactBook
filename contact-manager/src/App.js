import React from 'react';
import './App.css';
import {BrowserRouter,Routes,Route} from "react-router-dom";

import HomePage from './pages/HomePage';
import MainLayout from './layout/MainLayout';
import UserPage from './pages/UserPage';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';


const App=()=> {


  return (
    <BrowserRouter>
    <Routes>
      <Route path='/' element={<MainLayout/>}>

      <Route index element={<HomePage />} />
      <Route  path='/login' element={<LoginPage />} />
      <Route  path='/register' element={<RegisterPage />} />
      
      <Route path='/user' element={<UserPage/>} />   

      </Route>
    </Routes>
    
    </BrowserRouter>
  
  );


}

export default App;
