resource "google_data_fusion_instance" "basic_instance" {
  name = {{instance_name}}
  project = {{project_id}}
  region = "us-central1"
  type = "BASIC"
}