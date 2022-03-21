import shutil
import os
import yaml


if __name__ == "__main__":
    curr_folder = os.getcwd()

    # Paths of template file
    src_provider = curr_folder + '/template/terraform/provider.tf'
    dst_provider = curr_folder + '/source_code/terraform/provider.tf'
    src_project = curr_folder + '/template/terraform/project_create.tf' 
    config_file = 'data-fusion-pipeline.yml'


    #  Load configuration file
    with open(config_file,'r') as file:
        config_data = yaml.safe_load(file)


    # List to hold contents of output file
    main_terraform = []
    project_create = []

    with open(src_project,'r') as file:
        project_create.extend(file.readlines())






    ## Write to the source code
    # Write the provider file to source code
    shutil.copyfile(src_provider, dst_provider)
