variable "project_id" {
  type        = string
  description = "The ID of the GCP project to use."
  default     = "summative1"
}

variable "region" {
  type        = string
  description = "Region to deploy resources into."
  default     = "us-central1"
}

variable "firestore_db_name" {
  type        = string
  description = "Name of the firestore database."
  default     = "firestore-project-definitions-table"
}
