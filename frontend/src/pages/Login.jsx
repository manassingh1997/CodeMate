import { useState } from 'react';
import { loginUser } from '../api/auth';

function Login() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");

    const handleLogin = async() => {
        try {
            const data = await loginUser(email, password);
            localStorage.setItem("access", data.access);
            localStorage.setItem("refresh", data.refresh);
            alert("Login Successful");
        } catch (err) {
            setError("Invalid credentials");
        }
    };

    return (
        <div>
            <h2>Login</h2>

            <input 
                type="email"
                placeholder="Email" 
                value={email}
                onChange={(e)=> setEmail(e.target.value)}
            />
            <br /><br />
            <input 
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)} 
            />
            <br /><br />

            <button onClick={handleLogin}>Login</button>
            {error && <p style={{ color: "red" }}>{error}</p>}
        </div>
    )
}

export default Login;