# services/users/project/api/ping.py


from flask_restx import Namespace, Resource

sample_namespace = Namespace("sample")


class Sample(Resource):
    def get(self):
        return {"SAMPLE": "TEST", "message": "AWS!"}


sample_namespace.add_resource(Sample, "")
