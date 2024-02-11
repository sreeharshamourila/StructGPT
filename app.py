from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
from OpenAIClientInterface.OpenAIModelFactory import ModelFactory
from DataCrafting.DataCraftingFactory import DataCraftingFactory
import json
from Models.Models import setup_database
from DataCrafting.FileValidatorAndExtractor import allowed_file, process_file

app = Flask(__name__)
CORS(app)


#DataBase and Upload Folder settings
UPLOAD_FOLDER = '/Uploads'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'MydatabaseNew.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#importing DataBase Models
db=setup_database(app)

#Creating Folder for uploading unstrctured data
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


#controllers for both upload and process apis
@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the request has the file part

    if 'file' not in request.files:
        return jsonify(error="No file part in the request"), 400
    file = request.files['file']
    # If the user does not select a file, the browser submits an empty part without a filename
    if file.filename == '':
        return jsonify(error="No file selected"), 402
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        paragraphs = process_file(filepath)

        frontend_response = []
        for paragraph in paragraphs:
            messages = ModelFactory.generate_messages(paragraph)

            completion = ModelFactory.create_model(
                model_name="gpt-3.5-turbo",
                max_tokens=300,
                messages=messages,
                temperature=0,
            )

            json_string = completion.choices[0].message.content

            # Parse the JSON string into a Python dictionary
            try:
                # Attempt to load the JSON string
                parsed_json = json.loads(json_string)
            except json.decoder.JSONDecodeError as e:
                parsed_json = {'type': "NA"}
            app.logger.info(parsed_json)
            if len(parsed_json)>1:
                    crafter = DataCraftingFactory.get_crafter(parsed_json['type'])
                    frontend_data = crafter.craft_for_frontend(parsed_json)
                    frontend_response.append(frontend_data)
            else:
                frontend_response = [{'type': "NA"}]
                return jsonify({"tableData": frontend_response}), 400


        return jsonify({"tableData": frontend_response}),200

@app.route('/process', methods=['POST'])
def process_input():
    data = request.json
    text_input = data['text']

    messages = ModelFactory.generate_messages(text_input)

    completion = ModelFactory.create_model(
        model_name="gpt-3.5-turbo",
        max_tokens=300,
        messages=messages,
        temperature=0,
    )

    json_string = completion.choices[0].message.content
    try:
        # Attempt to load the JSON string
        parsed_json = json.loads(json_string)
    except json.decoder.JSONDecodeError as e:
        parsed_json = {'type':"None"}
    # Parse the JSON string into a Python dictionary


    # Crafting for database
    crafter = DataCraftingFactory.get_crafter(parsed_json['type'])
    if(len(parsed_json)>1):
        model_instance = crafter.craft_for_database(parsed_json)
    # Now, you can add `model_instance` to your database session
        db.session.add(model_instance)
        db.session.commit()
    # Crafting for frontend
        frontend_data = crafter.craft_for_frontend(parsed_json)
    # `frontend_data` is ready to be sent to the frontend
        frontend_response= [frontend_data]
        return jsonify({"tableData": frontend_response}),200
    frontend_response = [{'type':"NA"}]
    return jsonify({"tableData": frontend_response}),400

if __name__ == '__main__':
    app.run(debug=True)
