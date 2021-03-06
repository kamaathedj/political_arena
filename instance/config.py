
class BaseConfig:
    DEBUG=False

class DevelopmentConfig(BaseConfig):
    DEBUG=True
    
class TestingConfig():
    DEBUG=True
class ProductionConfig(BaseConfig):
    DEBUG=False

app_configurations = {
    "development":DevelopmentConfig,
    "testing":TestingConfig,
    "production":ProductionConfig

}