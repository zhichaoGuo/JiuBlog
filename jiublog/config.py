class Config(object):
    pass


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    pass


config_dict = {
    'Development': DevelopmentConfig,
    'Production': ProductionConfig
}
