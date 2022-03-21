py create_pipeline.py
cd source_code/terraform
terraform init -input=false
terraform plan -out=tfplan -input=false
terraform apply -input=false tfplan