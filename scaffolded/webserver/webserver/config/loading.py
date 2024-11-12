from omegaconf import OmegaConf

from webserver import CONFIG_LOCATION
from webserver.app_settings import APP_SETTINGS

default_conf = OmegaConf.load(CONFIG_LOCATION / "{}.yml".format("default"))
env_conf = OmegaConf.load(CONFIG_LOCATION / "{}.yml".format(APP_SETTINGS.environment))

config = OmegaConf.merge(default_conf, env_conf)
