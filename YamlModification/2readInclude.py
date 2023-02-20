import os

import yaml
import pdb

class Loader(yaml.SafeLoader):

    def __init__(self, stream):

        self._root = os.path.split(stream.name)[0]

        super(Loader, self).__init__(stream)

    def include(self, node):
        pdb.set_trace()

        #filename = os.path.join(self._root, self.construct_scalar(node))
        filename = r'C:\\Users\\pawarp\\PycharmProjects\\MyGit\\prakashpawar4u\\AdvancedPython\\YamlModification\\BW.yml'
        with open(filename, 'r') as f:
            return yaml.load(f, Loader)


def load_yaml_file(file_path):
    Loader.add_constructor('!include', Loader.include)
    with open(file_path) as fr:
        yaml_tl = yaml.load(fr, Loader=Loader)
    fr.close()
    return yaml_tl

fp = r"C:\Users\pawarp\PycharmProjects\MyGit\prakashpawar4u\AdvancedPython\YamlModification\1basic.yaml"
cont = load_yaml_file(fp)
print(f"Content of Yaml file : {cont}")