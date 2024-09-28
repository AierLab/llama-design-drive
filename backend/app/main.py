from app.dao.configDataManager import ConfigManager
from app.view.appView import AppView


def main():
    config_path = 'storage/config/main_config.yaml'
    config_manager = ConfigManager(config_path)
    flask_app = AppView(config_manager)

    flask_config_model = config_manager.config.flask
    flask_app.run(
        host=flask_config_model.host,
        port=flask_config_model.port,
        debug=flask_config_model.debug
    )
    