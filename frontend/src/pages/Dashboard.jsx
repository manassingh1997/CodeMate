import UserProfile from "../components/UserProfile";
import Recommendations from "../components/Recommendations";
import CodingLogs from "../components/CodingLogs";
import "../styles/dashboard.css";

function Dashboard() {
  return (
    <div className="dashboard-container">
      <section id="profile">
        <UserProfile />
      </section>

      <section id="recommendations">
        <Recommendations />
      </section>

      <section id="logs">
        <CodingLogs />
      </section>
    </div>
  );
}

export default Dashboard;
