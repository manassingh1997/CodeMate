import "../styles/auth.css"

function AuthLayout({ subtitle, children }) {
    return (
        <div className="auth-page">
            <div className="auth-card">
                <div className="auth-brand">
                    <h1>CodeMate</h1>
                    <p>{subtitle}</p>
                </div>

                {children}
            </div>
        </div>
    );
}

export default AuthLayout