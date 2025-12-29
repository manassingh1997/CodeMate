import { useEffect, useState } from "react";
import { getRecommendations } from "../api/genai";
import "../styles/dashboard.css";

function Recommendations() {
  const [data, setData] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchRecommendations = async () => {
      try {
        const res = await getRecommendations();
        // IMPORTANT: normalize response here
        setData(res.recommendations);
      } catch {
        setError("Failed to generate recommendations");
      } finally {
        setLoading(false);
      }
    };

    fetchRecommendations();
  }, []);

  return (
    <div className="dashboard-card">
      <div className="dashboard-card-header">
        <h2>AI Recommendations</h2>
        <p>What you should focus on next</p>
      </div>

      {error && <p className="dashboard-error">{error}</p>}

      {loading || !data || !data.today_plan ? (
        <p className="dashboard-loading">Analyzing your progress...</p>
      ) : (
        <>
          {/* Focus summary */}
          {data.focus_summary && (
            <p className="dashboard-value" style={{ marginBottom: "16px" }}>
              {data.focus_summary}
            </p>
          )}

          {/* Today plan */}
          <div className="dashboard-field">
            <label>Today’s Plan</label>
            <p className="dashboard-value">
              🎯 Solve{" "}
              <strong>{data.today_plan.daily_problem_target}</strong>{" "}
              problems <br />
              🔥 Focus:{" "}
              <strong>{data.today_plan.difficulty_focus}</strong>
            </p>
          </div>

          {/* Recommended problems */}
          <div className="dashboard-field">
            <label>Recommended Problems</label>

            <div className="recommendation-list">
              {data.recommended_problems.map((prob, idx) => (
                <div key={idx} className="recommendation-item">
                  <div className="recommendation-header">
                    <span
                      className={`difficulty-tag ${prob.difficulty.toLowerCase()}`}
                    >
                      {prob.difficulty}
                    </span>

                    <span className="recommendation-title">
                      {prob.title}
                    </span>
                  </div>

                  <p className="recommendation-reason">
                    {prob.reason}
                  </p>
                </div>
              ))}
            </div>
          </div>
        </>
      )}
    </div>
  );
}

export default Recommendations;
