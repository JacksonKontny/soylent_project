# methods copied from far more talented programmer at CallOne
from os import environ
import sys
from ConfigParser import ConfigParser


def setup(module_name, filenames=[], sections=[], environment=None):           
    config = Config(module_name)                                               
    config.read(filenames)                                                     
    config.apply_sections(*sections)                                           
    config.apply_environment(environment)                                      
    return config                                                              


def settings_dictionary(settings_module, prefix, lower=False):                 
    prefix = prefix.upper() + '_'                                              
    dictionary = {}                                                            
    for name in dir(settings_module):                                          
        if name.startswith(prefix):                                            
            _, setting_name = name.split('_', 1)                               
            if lower:                                                          
                setting_name = setting_name.lower()                            
            dictionary[setting_name] = getattr(settings_module, name)          
    return dictionary                                                          


class Config(ConfigParser):                                                    
    def __init__(self, module_name):                                           
        ConfigParser.__init__(self)                                            
        self.module_name = module_name                                         
        self.settings_module = sys.modules[module_name]                        

    def apply_sections(self, *sections):                                       
        for section in sections:                                               
            for key, value in self.items(section):                             
                setting_name = '{}_{}'.format(section.upper(), key.upper())    
                setattr(self.settings_module, setting_name, value)             

    def apply_environment(self, environment):                                  
        if environment:                                                        
            env_module = __import__('.'.join([self.module_name, environment]), 
                globals(), locals(), ['*'], -1)                                
            for attr in dir(env_module):                                       
                if attr == attr.upper():                                       
                    setattr(self.settings_module, attr, getattr(env_module,    
                        attr))                                                 

    def to_dict(self, section, lower=False):                                   
        if lower:                                                              
            return dict(self.items(section))                                   
        return dict(map(lambda item: (item[0].upper(), item[1]),               
            self.items(section)))                                              
