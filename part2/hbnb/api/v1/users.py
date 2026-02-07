from flask_restx import Namespace, Resource, fields
from hbnb.services.facade import HBnBFacade

api = Namespace("users", description="User endpoints")
facade = HBnBFacade()

user_model = api.model("User", {
    "id": fields.String,
    "first_name": fields.String,
    "last_name": fields.String,
    "email": fields.String
})

@api.route("/")
class UserList(Resource):
    @api.marshal_list_with(user_model)
    def get(self):
        return facade.get_all_users()

    @api.expect(user_model)
    @api.marshal_with(user_model)
    def post(self):
        return facade.create_user(api.payload)
