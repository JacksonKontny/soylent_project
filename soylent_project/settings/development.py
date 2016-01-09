from soylent_project.settings import setup
from soylent_project.settings.base import *

config = setup(__name__, filenames=['/etc/soylent_project/config.ini'],
		sections=['soylent_project'])
SR27 = config.to_dict('sr27')
SECRET_KEY = SOYLENT_PROJECT_SECRET_KEY
DATABASES = {
    'default': SR27
}
