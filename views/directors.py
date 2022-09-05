from flask_restx import Resource, Namespace
from flask import request
from dao.model.director import DirectorSchema
from helpers.decorators import auth_required, admin_required
from implemented import director_service

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        rs = director_service.get_all()
        res = directors_schema.dump(rs)
        return res, 200

    @admin_required
    def post(self):
        req_json = request.json
        director_service.create(req_json)
        return "", 201


@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    @auth_required
    def get(self, rid):
        r = director_service.get_one(rid)
        sm_d = director_schema.dump(r)
        return sm_d, 200

    @admin_required
    def put(self, rid: int):
        req_json = request.json
        req_json["id"] = rid
        director_service.update(req_json)
        return "", 204

    @admin_required
    def patch(self, rid: int):
        req_json = request.json
        req_json["id"] = rid
        director_service.update_partial(req_json)
        return "", 204

    @admin_required
    def delete(self, rid: int):
        director_service.delete(rid)
        return "", 204
