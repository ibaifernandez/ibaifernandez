# SQLAlchemy

1. ## [SQLAlchemy](https://www.sqlalchemy.org/)

2. ## [Declaring Models](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/)

Generally Flask-SQLAlchemy behaves like a properly configured declarative base from the declarative extension. As such we recommend reading the SQLAlchemy docs for a full reference. However the most common use cases are also documented here.

Things to keep in mind:

-   The baseclass for all your models is called db.Model. It’s stored on the SQLAlchemy instance you have to create. See Quickstart for more details.

-   Some parts that are required in SQLAlchemy are optional in Flask-SQLAlchemy. For instance the table name is automatically set for you unless overridden. It’s derived from the class name converted to lowercase and with “CamelCase” converted to “camel_case”. To override the table name, set the **tablename** class attribute.
