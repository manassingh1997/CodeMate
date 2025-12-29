import { useEffect, useState } from "react";
import {
  getCodingLogs,
  createCodingLog,
  updateCodingLog,
} from "../api/codingLogs";
import "../styles/dashboard.css";

function CodingLogs() {
  const [logs, setLogs] = useState([]);
  const [page, setPage] = useState(1);
  const [next, setNext] = useState(null);
  const [prev, setPrev] = useState(null);

  const [problemLink, setProblemLink] = useState("");
  const [createError, setCreateError] = useState("");

  const [editingId, setEditingId] = useState(null);
  const [notes, setNotes] = useState("");

  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchLogs(page);
  }, [page]);

  const fetchLogs = async (pageNum) => {
    setLoading(true);
    try {
      const data = await getCodingLogs(pageNum);
      setLogs(data.results);
      setNext(data.next);
      setPrev(data.previous);
    } finally {
      setLoading(false);
    }
  };

  /* ---------------- CREATE LOG ---------------- */

  const handleCreate = async () => {
    setCreateError("");
    try {
      await createCodingLog(problemLink);
      setProblemLink("");
      fetchLogs(page);
    } catch (err) {
      setCreateError(
        err.response?.data?.error || "Failed to log problem"
      );
    }
  };

  /* ---------------- UPDATE NOTES ---------------- */

  const handleSaveNotes = async (id) => {
    try {
      await updateCodingLog(id, notes);
      setEditingId(null);
      setNotes("");
      fetchLogs(page);
    } catch {
      // silent fail for now
    }
  };

  return (
    <div className="dashboard-card">
      <div className="dashboard-card-header">
        <h2>Coding Logs</h2>
        <p>Your recent solved problems</p>
      </div>

      {/* ----------- CREATE LOG ----------- */}
      <div className="dashboard-field">
        <label>Log New Problem</label>
        <input
          className="dashboard-input"
          placeholder="Paste LeetCode problem link"
          value={problemLink}
          onChange={(e) => setProblemLink(e.target.value)}
        />
      </div>

      {createError && (
        <p className="dashboard-error">{createError}</p>
      )}

      <button
        className="dashboard-btn"
        onClick={handleCreate}
        disabled={!problemLink.trim()}
      >
        Log Problem
      </button>

      {/* ----------- LIST LOGS ----------- */}
      {loading ? (
        <p className="dashboard-loading">Loading logs...</p>
      ) : logs.length === 0 ? (
        <p className="dashboard-value">No logs yet.</p>
      ) : (
        <>
          {logs.map((log) => (
            <div key={log.id} className="dashboard-field">
              <p className="dashboard-value">
                {log.problem_title}
              </p>

              <p style={{ fontSize: "13px", color: "#94a3b8" }}>
                {log.difficulty} • {log.topics.join(", ")}
              </p>

              {/* Notes view */}
              {editingId === log.id ? (
                <>
                  <textarea
                    className="dashboard-input"
                    placeholder="Add notes"
                    value={notes}
                    onChange={(e) => setNotes(e.target.value)}
                    style={{ marginTop: "8px" }}
                  />

                  <button
                    className="dashboard-btn"
                    onClick={() => handleSaveNotes(log.id)}
                  >
                    Save Notes
                  </button>
                </>
              ) : (
                <>
                  <p
                    style={{
                      fontSize: "13px",
                      color: "#94a3b8",
                      marginTop: "6px",
                    }}
                  >
                    {log.notes || "No notes added"}
                  </p>

                  <button
                    className="dashboard-btn"
                    onClick={() => {
                      setEditingId(log.id);
                      setNotes(log.notes || "");
                    }}
                  >
                    Add / Edit Notes
                  </button>
                </>
              )}
            </div>
          ))}

          {/* ----------- PAGINATION ----------- */}
          <div style={{ display: "flex", gap: "10px", marginTop: "16px" }}>
            <button
              className="dashboard-btn"
              disabled={!prev}
              onClick={() => setPage((p) => p - 1)}
            >
              Prev
            </button>

            <button
              className="dashboard-btn"
              disabled={!next}
              onClick={() => setPage((p) => p + 1)}
            >
              Next
            </button>
          </div>
        </>
      )}
    </div>
  );
}

export default CodingLogs;
