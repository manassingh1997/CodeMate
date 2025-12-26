import "../styles/dashboard.css";
import UserProfile from "../components/UserProfile";

function Dashboard() {
    return (
        <div className="dashboard-container">
            <UserProfile />

            {/* Future cards */}
            {/*
              <CodingLogs />
              <Recommendations />
            */}
        </div>
    );
}

export default Dashboard;
