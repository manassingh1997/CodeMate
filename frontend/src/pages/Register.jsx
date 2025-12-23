import { useState } from "react";
import { Link } from "react-router-dom";
import AuthLayout from "../components/AuthLayout";
import { registerUser } from "../api/auth";

function Register() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");

    const handleRegister = async () => {
        console.log({
            email,
            password
        });
        try {
            await registerUser(email, password);
            window.location.href = "/login";
        } catch {
            setError("Registration failed");
        }
    };

    return (
        <AuthLayout subtitle="Build consistency. Crack interviews with CodeMate.">
            {error && <p className="auth-error">{error}</p>}

            <input
                className="auth-input"
                type="email"
                placeholder="Email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
            />

            <input
                className="auth-input"
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
            />

            <button className="auth-btn" onClick={handleRegister}>
                Create Account
            </button>

            <div className="auth-footer">
                Already registered? <Link to="/login">Login</Link>
            </div>
        </AuthLayout>
    );
}

export default Register;
