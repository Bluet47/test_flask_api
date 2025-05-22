# db.py
import firebase_admin
from firebase_admin import firestore


class Database:
    def __init__(self, collection_name):
        firebase_admin.initialize_app()
        self.db = firestore.client()
        self.collection_name = collection_name

    def get_all_projects(self):
        projects_ref = self.db.collection(self.collection_name)
        docs = projects_ref.stream()
        projects = []

        for doc in docs:
            project_data = doc.to_dict()
            project_data["project_name"] = doc.id
            projects.append(project_data)

        return projects

    def get_project(self, project_name):
        project = self.db.collection(self.collection_name).document(project_name).get()
        return project

    def add_project(self, project_name, project_data):
        self.db.collection(self.collection_name).document(project_name).set(
            project_data
        )

    def update_project(self, project_name, project_data):
        self.db.collection(self.collection_name).document(project_name).update(
            project_data
        )

    def delete_project(self, project_name):
        self.db.collection(self.collection_name).document(project_name).delete()
