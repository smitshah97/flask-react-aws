# services/users/project/api/sample.py


from flask_restx import Namespace, Resource

sample_namespace = Namespace("sample")


class Sample(Resource):
    def get(self):
        return {"status": "success", "message": "pong!"}


sample_namespace.add_resource(Sample, "")
