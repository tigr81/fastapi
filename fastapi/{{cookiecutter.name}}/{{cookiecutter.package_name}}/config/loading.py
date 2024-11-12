from omegaconf import OmegaConf

from {{cookiecutter.package_name}} import CONFIG_LOCATION
from {{cookiecutter.package_name}}.app_settings import APP_SETTINGS

default_conf = OmegaConf.load(CONFIG_LOCATION / "{}.yml".format("default"))
env_conf = OmegaConf.load(CONFIG_LOCATION / "{}.yml".format(APP_SETTINGS.environment))

config = OmegaConf.merge(default_conf, env_conf)
