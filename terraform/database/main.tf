resource "google_project_service" "firestore" {
  project = var.project_id
  service = "firestore.googleapis.com"
}

resource "google_firestore_database" "default" {
  project     = var.project_id
  name        = "(default)"
  location_id = var.region
  type        = "FIRESTORE_NATIVE"
}
