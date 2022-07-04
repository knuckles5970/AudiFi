"""Contains the data models created and stored by this application
    """
import os
import peewee
import config


db = peewee.SqliteDatabase(config.DBNAME)


class __BaseModel(peewee.Model):
    """
    Base model for all models in this application.
    Ensures that all models are using the same database.
    Should not create instances directly.
    """
    class Meta:
        database = db


class Track(__BaseModel):
    """
    Track information data model
    """
    title = peewee.CharField()
    writer = peewee.CharField()
    performer = peewee.CharField()

    class Meta:
        table_name = 'tracks'


with db:
    db.create_tables([Track])
