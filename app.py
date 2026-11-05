import json
import os
import uuid
from datetime import datetime, timezone

from flask import Flask, Response

app = Flask(__name__)

ID_INSTANCE = uuid.uuid4().hex[:8]
jumlah_permintaan = 0


@app.route("/")
def portal():
    global jumlah_permintaan
    jumlah_permintaan += 1

    data = {
        "layanan": "Portal PMB Universitas Teknologi Muhammadiyah",
        "nama": "Zaidan Syahbana",
        "nim": "2401600003",
        "gelombang": os.environ.get("GELOMBANG", "Gelombang 1"),
        "pengumuman": os.environ.get("PENGUMUMAN", "Pendaftaran gelombang 1 dibuka"),
        "versi": os.environ.get("VERSI", "v1"),
        "lingkungan": os.environ.get("VERCEL_ENV", "development"),
        "region": os.environ.get("VERCEL_REGION", "lokal"),
        "commit": os.environ.get("VERCEL_GIT_COMMIT_SHA", "lokal")[:7],
        "id_instance": ID_INSTANCE,
        "permintaan_ke": jumlah_permintaan,
        "waktu_utc": datetime.now(timezone.utc).isoformat(),
    }

    isi = json.dumps(data, separators=(",", ":"), sort_keys=True)
    return Response(isi, mimetype="application/json")


if __name__ == "__main__":
    app.run(debug=True)