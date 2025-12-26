import Navbar from "./Navbar";
import "../styles/dashboard.css";

function Layout({ children }) {
    return (
        <>
            <Navbar />
            <main className="dashboard-page">
                {children}
            </main>
        </>
    );
}

export default Layout;
