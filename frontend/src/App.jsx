import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Login from './pages/Login.jsx';
import Register from "./pages/Register.jsx";
import Dashboard from './pages/Dashboard.jsx';
import Layout from "./components/Layout.jsx";
import PrivateRoute from "./routes/PrivateRoute.jsx"; 

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/login" element={<Login />} />
                <Route path="/register" element={<Register />} />

                <Route
                    path="/"
                    element={
                        <PrivateRoute>
                            <Layout>
                                <Dashboard />
                            </Layout>
                        </PrivateRoute>
                    }
                />
            </Routes>
        </BrowserRouter>
    );
}

export default App;
