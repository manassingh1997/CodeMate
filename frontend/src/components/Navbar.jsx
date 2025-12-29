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
      {/* Left: Brand */}
      <Link to="/" className="navbar-brand">
        CodeMate
      </Link>

      {/* Center: Dashboard section links */}
      {isAuthenticated && (
        <div className="navbar-links">
          <a href="#profile" className="navbar-link">
            Profile
          </a>
          <a href="#recommendations" className="navbar-link">
            AI Plan
          </a>
          <a href="#logs" className="navbar-link">
            Coding Logs
          </a>
        </div>
      )}

      {/* Right: Auth actions */}
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
