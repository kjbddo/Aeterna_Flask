from flask import Blueprint
from routes.food_analysis import food_analysis_bp

api_bp = Blueprint('api', __name__)

# 하위 블루프린트 등록
api_bp.register_blueprint(food_analysis_bp, url_prefix='/food')
