from flask import Blueprint, jsonify, current_app

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    cfg = current_app.config
    return jsonify(
        {
            "message": "Anime Lists API is running!",
            "env": cfg.get("ENV"),
            "db_uri": cfg.get("SQLALCHEMY_DATABASE_URI"),
            "jwt_secret_length": len(cfg.get("JWT_SECRET", "")),
        }
    )