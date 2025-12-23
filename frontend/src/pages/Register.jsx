import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import AuthLayout from "../components/AuthLayout";
import { registerUser } from "../api/auth";

function Register() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [errors, setErrors] = useState({});
    const [passwordError, setPasswordError] = useState("");

    const navigate = useNavigate();

    const validatePassword = (value) => {
        if (value.length < 8) {
            return "Password must be at least 8 characters";
        }
        if (!/[A-Za-z]/.test(value)) {
            return "Password must contain a letter";
        }
        if (!/[0-9]/.test(value)) {
            return "Password must contain a number";
        }
        return "";
    };

    const handleRegister = async () => {
        setErrors({}); // reset old errors

        try {
            await registerUser(email, password);
            navigate("/login");
        } catch (err) {
            if (err.response && err.response.data) {
                setErrors(err.response.data);
            } else {
                setErrors({ general: "Something went wrong" });
            }
        }
    };

    return (
        <AuthLayout subtitle="Build consistency. Crack interviews with CodeMate.">

            {errors.general && (
                <p className="auth-error">{errors.general}</p>
            )}

            <input
                className="auth-input"
                type="email"
                placeholder="Email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
            />
            {errors.email && (
                <p className="auth-error">{errors.email[0]}</p>
            )}

            <input
                className="auth-input"
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => {
                    const val = e.target.value;
                    setPassword(val);
                    setPasswordError(validatePassword(val));
                }}
            />

            {passwordError && (
                <p className="auth-error">{passwordError}</p>
            )}

            {errors.password && (
                <p className="auth-error">{errors.password[0]}</p>
            )}

            <button
                className="auth-btn"
                onClick={handleRegister}
                disabled={passwordError !== ""}
            >
                Create Account
            </button>

            <div className="auth-footer">
                Already registered? <Link to="/login">Login</Link>
            </div>

        </AuthLayout>
    );
}

export default Register;
