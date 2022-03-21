import shutil
import os
import yaml
import re


def read_config(config_file):
    """ Read the configuration YAML file and return its content as JSON"""
    #  Load configuration file
    with open(config_file,'r') as file:
        config_data = yaml.safe_load(file)

    return config_data

def read_template(template_file):
    """Reads the template files and return its content as list"""
    with open(template_file,'r') as file:
        return file.readlines()

def substitute_template(config_object, config_name, template_content):
    """Subtitutes place holders in template from config file"""
    place_holders = config_object.keys() # Available keys in config file
    template_out = [] #List to hold substituted values
    for line in template_content:
        search_result = re.search('{{(.*)}}', line) # Check for place holder
        if search_result is None:
            template_out.append(line)
        else:
            key = search_result.group(1) # Extract the place holder name
            # If place holder name not found in config, throw an error
            if key not in place_holders:
                raise SystemExit(f'{key} in {config_name} not exists')
            line = line.replace(f'{{{{{key}}}}}',config_object[key]) # Substitute the placeholder
            template_out.append(line)

    return template_out


def transform_template(config_file):
    """Read the config file, and transform all templates found in it"""
    # Read the config file
    config_data = read_config(config_file)

    curr_folder = os.getcwd() # Current path to get absolute path
    main_tf = [] # To hold all contents of final main.tf
    for config_object in config_data:
        file_path = config_data[config_object]['file_path']
        file_path = curr_folder + file_path
        template_content = read_template(file_path) # Read the template from the file path
        # Substitue the content
        main_tf.extend(substitute_template(config_data[config_object], config_object, template_content))
        main_tf.extend(['\n','\n']) # Add space after each template

    return main_tf

def write_main_tf(main_tf):
    """Write to main.tf"""
    # Destination path for main.tf
    curr_folder = os.getcwd()
    main_dest = curr_folder + '/source_code/terraform/main.tf'   

    # Write to main.tf
    with open(main_dest,'w') as file:
        for line in main_tf:
            file.write(line)


def write_provider():
    """Copy the provider from template to source code"""
    # Paths of template and source file
    curr_folder = os.getcwd()
    src_provider = curr_folder + '/template/terraform/provider.tf'
    dst_provider = curr_folder + '/source_code/terraform/provider.tf'

    # Write the provider file to source code
    shutil.copyfile(src_provider, dst_provider)

if __name__ == "__main__":
    
    # Config file path
    config_file = 'data-fusion-pipeline.yml'

    # Transform templates and extract values for main.tf
    main_terraform = transform_template(config_file)

    ## Write to the source code
    write_main_tf(main_terraform)
    write_provider()
    
    
