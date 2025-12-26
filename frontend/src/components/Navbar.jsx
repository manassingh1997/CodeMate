import { Link, useNavigate } from "react-router-dom";
import "../styles/navbar.css";

function Navbar() {
    const navigate = useNavigate();
    const isAuthenticated = !!localStorage.getItem("access");

    const logout = () => {
        localStorage.removeItem("access");
        localStorage.removeItem("refresh");
        navigate("/login");
    };

    return (
        <nav className="navbar">
            <Link to="/" className="navbar-brand">
                CodeMate
            </Link>

            <div className="navbar-actions">
                {isAuthenticated ? (
                    <button className="navbar-btn" onClick={logout}>
                        Logout
                    </button>
                ) : (
                    <Link to="/login" className="navbar-btn">
                        Login
                    </Link>
                )}
            </div>
        </nav>
    );
}

export default Navbar;
