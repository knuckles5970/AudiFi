"""Contains the data models created and stored by this application
    """
import os
import peewee


def get_app_database() -> peewee.SqliteDatabase:
    return peewee.SqliteDatabase(os.getenv('AUDIFI_DBNAME'))


class __BaseModel(peewee.Model):
    """
    Base model for all models in this application.
    Ensures that all models are using the same database.
    Should not create instances directly.
    """
    class Meta:
        database = get_app_database()


class Track(__BaseModel):
    """
    Track information data model
    """
    title = peewee.CharField()
    writer = peewee.CharField()
    performer = peewee.CharField()

    class Meta:
        table_name = 'tracks'
