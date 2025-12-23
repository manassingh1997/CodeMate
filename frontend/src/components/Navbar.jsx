import { Link, useNavigate } from "react-router-dom";

function Navbar() {
    const navigate = useNavigate();
    const isAuthenticated = !!localStorage.getItem("access");

    const logout = () => {
        localStorage.removeItem("access");
        localStorage.removeItem("refresh");
        navigate("/login");
    };

    return (
        <nav style={{ padding: "10px", borderBottom: "1 px solid #ddd" }}>
            <Link to="/">CodeMate</Link> 

            <span style={{float: "right"}}>
                {isAuthenticated ? (
                    <button onClick={logout}>Logout</button>
                ) : (
                    <Link to="/login">Login</Link>
                )}
            </span>
        </nav>
    );
}

export default Navbar;