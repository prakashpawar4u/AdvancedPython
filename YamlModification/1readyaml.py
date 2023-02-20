import os
import yaml

def readYaml(fileName):
    '''
    Read yaml & inculude another yaml to it
    @Author: Prakash Kumar Pawar
    @param : File Name
    @return: File content
    '''
    print(f"file name passed :: {fileName}")
    fn = os.getcwd() + "\\" + fileName
    print(f"fileName with full path :: {fn}")
    with open(fn , 'r') as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)

    print(yaml_data)

if __name__ == "__main__":
    print("This is python file reading yaml")

    #call function
    #readYaml("2bw.yaml")
    #readYaml("1basic.yaml")