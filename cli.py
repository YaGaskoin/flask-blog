import fire
import flask_migrate
from app import app
import view


def run_server():
    app.run()


def migrate_init():
    """Инициализировать папку миграций"""
    with app.app_context():
        return flask_migrate.init('migrates')


def migrate(msg):
    """Автоматически создать начальную миграцию, то есть upgrade - скрипт создания таблицы , а downgrade - drop table"""
    with app.app_context():
        return flask_migrate.migrate('migrates', message=msg)


def revision(msg):
    """Создать миграцию с пустыми функциями downgrade и upgrade для ручного заполнения"""

    with app.app_context():
        return flask_migrate.revision('migrates', message=msg)


def upgrade(revision='head'):
    """Перевести таблицы на версию выше"""
    with app.app_context():
        return flask_migrate.upgrade('migrates', revision)


def downgrade(revision='-1'):
    """Перевести таблицы на версию ниже"""
    with app.app_context():
        return flask_migrate.downgrade('migrates', revision)


if __name__ =='__main__':
    fire.Fire({
        'run_server': run_server,
        'migrate_init': migrate_init,
        'migrate': migrate,
        'revision': revision,
        'upgrade': upgrade,
        'downgrade': downgrade

    })