from flask import Flask, request, jsonify
from firestoreDB import Database

COLLECTION_NAME = "project_definitions"

app = Flask(__name__)

db_instance = Database(COLLECTION_NAME)


@app.route("/", methods=["GET"])
def test():
    return "App is running! Access /projects for project details. "


# Route to get all projects
@app.route("/projects", methods=["GET"])
def get_all_projects():
    projects = db_instance.get_all_projects()
    return jsonify(projects)


# Route to get details of a specifc project
@app.route("/project/<project_name>", methods=["GET"])
def get_project(project_name):
    project = db_instance.get_project(project_name)
    if project.exists:
        return jsonify(project.to_dict())
    else:
        return jsonify({"error": "Project not found"}), 404


# Route to add a new projectt
@app.route("/project", methods=["POST"])
def add_project():
    data = request.get_json()
    project_name = data.get("project_name")
    project_data = {
        "description": data.get("description"),
        "cost_centre": data.get("cost_centre"),
        "business_area": data.get("business_area"),
        "owner_name": data.get("owner_name"),
        "owner_email": data.get("owner_email"),
    }
    db_instance.add_project(project_name, project_data)
    return jsonify({"status": "Project added successfully!"}), 201


# Route to update an existing project
@app.route("/project/<project_name>", methods=["PUT"])
def update_project(project_name):
    data = request.get_json()
    db_instance.update_project(project_name, data)
    return jsonify({"status": "Project updated successfully!"})


# Route to delete a project
@app.route("/project/<project_name>", methods=["DELETE"])
def delete_project(project_name):
    db_instance.delete_project(project_name)
    return jsonify({"status": "Project deleted successfully!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
