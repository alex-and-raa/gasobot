import datetime
import sqlite3

from exceptions import NotFoundInDatabase


def view_contract(contract_number: str) -> dict[str, str]:
    with sqlite3.connect("database.sqlite3") as connection:
        cursor = connection.cursor()
        cursor.execute(
            f'SELECT c.contract_number, s.status, cl.client_name, c.sign_date, c.expire_date '
            f'FROM contract c, contract_status s, client cl '
            f'WHERE contract_number="{contract_number}"'
            f'AND c.status_id=s.id '
            f'AND c.client_id=cl.id')
        contract = cursor.fetchone()
        if contract:
            contract_info = {
                "contract_number": contract[0],
                "status": contract[1],
                "contract_client": contract[2],
                "sign_date": contract[3],
                "expire_date": contract[4]
            }
            return contract_info
        else:
            raise NotFoundInDatabase


def add_contact(contract_number, status_id, client_id, sign_date, expire_date) -> None:
    with sqlite3.connect("database.sqlite3") as connection:
        cursor = connection.cursor()
        cursor.execute(
            f'INSERT OR IGNORE INTO contract (contract_number, status_id, client_id, sign_date, expire_date)'
            f'VALUES ("{contract_number}", "{status_id}", "{client_id}", "{sign_date}", "{expire_date}")')


def change_contract():
    pass


def add_client(client_name) -> None:
    with sqlite3.connect("database.sqlite3") as connection:
        cursor = connection.cursor()
        cursor.execute(f'INSERT OR IGNORE INTO client (client_name) '
                       f'VALUES ("{client_name}")')


if __name__ == '__main__':
    pass
    # add_client("Rosneft")
    # add_contact("2341-63", 1, 1, datetime.date.today().isoformat(),
    #             datetime.date(2023, 10, 20).isoformat())
    # contract_ = view_contract("2341-63")
    # print(contract_)
