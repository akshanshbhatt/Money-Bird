import React from 'react';
// import useHistory, {Link} from 'use-history'
import { useNavigate } from 'react-router-dom';
import './navbar.css';

function Navbar() {
    let navigate = useNavigate();
  return (
    <div className="navbar">
        <div className="logo" onClick={() =>{navigate("/")}}>
            <img src="./images/logo1.png" alt="Company_Logo"></img>
        </div>
        <div className="inner_block">      
            <h2 onClick={() =>{navigate("/profile")}}>Home</h2>
            <h2 onClick={() =>{navigate("/login")}}>Login</h2>
            <h2 onClick={() =>{navigate("/signup")}}>Sign Up</h2>
        </div>
    </div>
  )
}

export default Navbar

// 37526E broad
// 5BD8E0 font
// #d4f4f7 background
