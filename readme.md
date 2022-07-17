# Autograding Example: Python
This example project is written in Python, and tested with pytest.

### The assignment
This is an assignment: `cinema ticket price`. The software should ask the relevant information to compute the price of a ticket of cinema. There are some conditions that give the client some discount:

-   ` -5 ` during the weekend, from Friday to Sunday.
-   ` -7 ` if the client is a child or a thrid age person.
-   ` -10 ` if the client want to book a morning session.

The normal price is 30. You must choice a currency.


The tests are failing right now because you have to implement the methods to make the program work. Fixing this up will make the tests green.

### Setup command
#### Linux
`sudo -H pip3 install -qI pytest`
#### Windows
`pip3 install -qI pytest`

### Run command
`pytest`

### Notes
- pip's install path is not included in the PATH var by default, so without installing via `sudo -H`, pytest would be unaccessible.