data "google_client_config" "current" {}
provider "cdap" {
  host  = "${google_data_fusion_instance.basic_instance.service_endpoint}/api/"
  token = data.google_client_config.current.access_token
}