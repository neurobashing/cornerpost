# Meals

requires python and gunicorn ... and love.

requires python 3 for runtime and python 2 to run supervisor
(you'll need to install supervisor)

## TODO:

* we want to eventually have season, so we don't get risotto in August
* probably weights, so that we don't get hamburger-like things twice in a week
* better UI
* Editor? 
* something else?

## MySQL

```sql
mysqladmin root password 'goldcoin'
CREATE USER 'meals'@'localhost' IDENTIFIED BY 'f00dtastesg00d';
GRANT ALL ON *.* TO 'meals'@'localhost';
create database 'meals';
```
