terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.63.1"
    }
  }
  # Adding GCS backend for state storage
  backend "gcs" {
    bucket      = "terraform-state-bucket-summative-1"
    prefix      = "summative1/terraform/state"
    credentials = "./credentials.json"
  }
}
provider "google" {
  project     = "summative1"
  region      = "us-central1"
  zone        = "us-central1-a"
  credentials = "./credentials.json"
}

