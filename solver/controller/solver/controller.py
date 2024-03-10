import json

import minizinc
from flask import request, Blueprint
from flask_restful import Resource, Api

from .input_model import RequestSchema
from solver.data.minizinc_service import MiniZincService


class SolveController(Resource):
    minizinc_service: MiniZincService

    def __init__(self, minizinc_service: MiniZincService = MiniZincService()):
        self.minizinc_service = minizinc_service

    def post(self):
        content = request.json
        errors = RequestSchema().validate(content)
        if errors:
            return {'error': "Validation Error"}, 400

        parameters = content['parameters']

        try:
            result = self.minizinc_service.solve(parameters)
        except minizinc.error.MiniZincError as e:
            return {'status': minizinc.Status.ERROR.name, 'message': f"{e}"}, 400

        if result.status not in [minizinc.Status.SATISFIED, minizinc.Status.ALL_SOLUTIONS, minizinc.Status.OPTIMAL_SOLUTION]:
            return {'status': result.status.name}, 400

        return {'status': result.status.name, 'result': json.loads(json.dumps(result.solution))}


solver_bp = Blueprint('solver', __name__)
api = Api(solver_bp)
api.add_resource(SolveController, '/solver')
