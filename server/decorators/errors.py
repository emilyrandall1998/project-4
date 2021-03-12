from app import app
from flask import Flask, jsonify
from marshmallow.exceptions import ValidationError

# ! This is our error handler. It handles form validation errors and generic errors. Both will pass
# ! whatever error is generated by SQLAlchemy or marshmallow, as well as a string to help us
# ! identify which kind of error has been created.

@app.errorhandler(ValidationError)
def validation_error(e):
    return { "errors": e.messages, "Message": "Something went wrong in validation" }, 404

@app.errorhandler(Exception)
def generic_error(e):
    return { "errors": str(e), "Message": "Generic Error"}, 404