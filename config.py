class BaseConfig:
    DEBUG=False

class DevelopmentConfig(BaseConfig):
    DEBUG=True
class TestingConfig():
    DEBUG=True

app_configurations = {
    "development":DevelopmentConfig,
    "Testing":TestingConfig
}