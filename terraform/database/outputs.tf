output "project_id" {
  description = "The Google Cloud project ID"
  value       = var.project_id
}

output "firestore_database_id" {
  description = "The ID of the Firestore database"
  value       = google_firestore_database.default.name
}

output "firestore_region" {
  description = "The region where Firestore is deployed"
  value       = google_firestore_database.default.location_id
}
