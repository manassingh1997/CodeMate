import { useEffect, useState } from "react";
import { getMe, updateUserProfile } from "../api/profile";
import "../styles/dashboard.css";

function UserProfile() {
  const [profile, setProfile] = useState(null);
  const [username, setUsername] = useState("");
  const [originalUsername, setOriginalUsername] = useState("");
  const [errors, setErrors] = useState({});
  const [loading, setLoading] = useState(false);
  const [isEditing, setIsEditing] = useState(false);

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const data = await getMe();
        setProfile(data);

        const lcUsername = data.leetcode_username || "";
        setUsername(lcUsername);
        setOriginalUsername(lcUsername);
      } catch {
        setErrors({ general: "Failed to load profile" });
      }
    };

    fetchProfile();
  }, []);

  const handleSave = async () => {
    setErrors({});
    setLoading(true);

    try {
      const updated = await updateUserProfile({
        leetcode_username: username,
      });

      setProfile(updated);
      setOriginalUsername(username);
      setIsEditing(false);
    } catch (err) {
      if (err.response?.data) {
        setErrors(err.response.data);
      } else {
        setErrors({ general: "Something went wrong" });
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="dashboard-card">
      <div className="dashboard-card-header">
        <h2>User Profile</h2>
        <p>Manage your LeetCode identity & stats</p>
      </div>

      {errors.general && (
        <p className="dashboard-error">{errors.general}</p>
      )}

      {!profile ? (
        <p className="dashboard-loading">Loading...</p>
      ) : (
        <>
          {/* Email */}
          <div className="dashboard-field">
            <label>Email</label>
            <input
              type="email"
              value={profile.email}
              disabled
              className="dashboard-input"
            />
          </div>

          {/* View Mode */}
          {!isEditing && (
            <>
              <div className="dashboard-field">
                <label>LeetCode Username</label>
                <p className="dashboard-value">
                  {originalUsername || "Not set"}
                </p>
              </div>

              <button
                className="dashboard-btn"
                onClick={() => setIsEditing(true)}
              >
                Update Username
              </button>
            </>
          )}

          {/* Edit Mode */}
          {isEditing && (
            <>
              <div className="dashboard-field">
                <label>LeetCode Username</label>
                <input
                  type="text"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  className="dashboard-input"
                  placeholder="Enter LeetCode username"
                />
              </div>

              {errors.leetcode_username && (
                <p className="dashboard-error">
                  {errors.leetcode_username[0]}
                </p>
              )}

              <button
                className="dashboard-btn"
                onClick={handleSave}
                disabled={
                  loading ||
                  !username.trim() ||
                  username === originalUsername
                }
              >
                {loading ? "Saving..." : "Save"}
              </button>
            </>
          )}

          {/* Stats */}
          <div className="dashboard-stats">
            <div className="stat-box">
              <span className="stat-label">LeetCode Solved</span>
              <span className="stat-value">
                {profile.leetcode_total_solved}
              </span>
            </div>

            {/* Difficulty lines */}
            <div className="leetcode-difficulty-lines">
              <div className="difficulty-line easy">
                Easy: {profile.leetcode_easy_solved}
              </div>
              <div className="difficulty-line medium">
                Medium: {profile.leetcode_medium_solved}
              </div>
              <div className="difficulty-line hard">
                Hard: {profile.leetcode_hard_solved}
              </div>
            </div>

            {profile.last_stats_updated && (
              <p className="stat-updated">
                Last updated:{" "}
                {new Date(profile.last_stats_updated).toLocaleString()}
              </p>
            )}
          </div>



        </>
      )}
    </div>
  );
}

export default UserProfile;
