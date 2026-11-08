from flask import Flask, render_template
from db import get_conn, init_db

app = Flask(__name__)


@app.route("/")
def index():
    conn = get_conn()
    lead_count = conn.execute("SELECT COUNT(*) FROM leads").fetchone()[0]
    proposal_count = conn.execute("SELECT COUNT(*) FROM proposals").fetchone()[0]
    conn.close()
    return render_template(
        "index.html", lead_count=lead_count, proposal_count=proposal_count
    )


if __name__ == "__main__":
    init_db()
    app.run(debug=True)