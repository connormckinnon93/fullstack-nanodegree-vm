# Fullstack Nanodegree VM with associated projects

Common code for the Relational Databases and Full Stack Fundamentals courses

## Udacity Project Tournament Results

**Program**: Udacity Fullstack Web Developer Nanodegree
**Project 4:** Tournament Results
**Languages:** Python 2.7.x, ProstgreSQL
**Methodology:** TDD

### Dependencies

This project runs inside the Fullstack Nanodegree VM.

Libraries included in this project are:
- Source code from for Fullstack Nanodegree VM: (https://github.com/udacity/fullstack-nanodegree-vm)
- Git: (https://git-scm.com/downloads)
- VirtualBox: (https://www.virtualbox.org/wiki/Downloads)
- Vagrant: (https://www.vagrantup.com/downloads.html)

### Getting Started

The project is located under `/vagrant/tournament`.

It contains the follow files:
- tournament.sql
- tournament.py
- tournament_test.py

*tournament.sql*
Contains the sql statements used to create the tables and views used by program

*tournament.py*
Contains the python program used to interact with the PostgreSQL database using python DB-API

*tournament_test.py*
Contains the tests used to validate the methods in tournament.py

#### Using the Virtual Machine

In order to get started with the virtual machine follow these steps in your preferred BASH terminal from the root folder.

```
vagrant up
vagrant ssh
cd /vagrant/tournament
```

#### Setting up the PostgreSQL Database

In order to create the pgsql database follow the steps under *"Using the Virtual Machine"* then follow these steps in a new instance of your preferred BASH terminal from the root folder.

```
vagrant ssh
cd /vagrant/tournament
pgsql
CREATE DATABASE tournament
\c tournament
\i tournament.sql
```

You have now created the PostgreSQL Database and populated it with the tables and views from tournament.sql

#### Testing the Tournament Program

In order to test the program follow the steps under *"Using the Virtual Machine"* then follow these steps in the same instance of your preferred BASH terminal.

```
python tournament_test.py
```

All tests pass currently.