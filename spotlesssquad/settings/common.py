import sqlalchemy

from spotlesssquad.settings import models
from spotlesssquad.sql import tables


def user_exists(email: str, con: sqlalchemy.Connection) -> bool:
    """
    Check if user exists.
    """
    stmt = sqlalchemy.select(tables.ClientUsers).where(
        tables.ClientUsers.email == email
    )
    result = con.execute(stmt).fetchone()
    return result is not None


def update_user(
    email: str,
    values: tuple[sqlalchemy.Column, str],
    con: sqlalchemy.Connection,
) -> bool:
    """
    Update user for the given email.
    """

    # check if user exists
    if not user_exists(email, con):
        return False

    stmt = (
        sqlalchemy.update(tables.ClientUsers)
        .where(tables.ClientUsers.email == email)
        .values(values)
    )

    res = con.execute(stmt)

    return res.rowcount == 1


def update_name(
    email: str,
    new_name: str,
    con: sqlalchemy.Connection,
) -> models.UpdateStatus:
    """
    Update user for the given email.
    """

    # check if user exists
    if not user_exists(email, con):
        return models.UpdateStatus.USER_NOT_FOUND

    res = update_user(
        email=email,
        values={tables.ClientUsers.name: new_name},
        con=con,
    )

    if res:
        return models.UpdateStatus.SUCCESS
    else:
        return models.UpdateStatus.FAILURE


def check_password_validity(password: str) -> bool:
    """
    Check if password is valid.
    """
    return len(password) >= 8


def update_password(
    email: str,
    new_password: str,
    con: sqlalchemy.Connection,
) -> models.UpdatePasswordStatus:
    """
    Update user for the given email.
    """

    if not check_password_validity(new_password):
        return models.UpdatePasswordStatus.PASSWORD_TOO_SHORT

    # check if user exists
    if not user_exists(email, con):
        return models.UpdateStatus.USER_NOT_FOUND

    res = update_user(
        email=email,
        values={tables.ClientUsers.password: new_password},
        con=con,
    )

    if res:
        return models.UpdatePasswordStatus.SUCCESS
    else:
        return models.UpdatePasswordStatus.FAILURE


def check_phone_validity(phone: str) -> models.UpdatePhoneStatus:
    """
    Check if phone is valid.
    """
    if len(phone) < 10:
        return models.UpdatePhoneStatus.NUMBER_TOO_SHORT
    elif len(phone) > 10:
        return models.UpdatePhoneStatus.NUMBER_TOO_LONG

    return models.UpdatePhoneStatus.SUCCESS


def update_phone(
    email: str,
    new_phone: str,
    con: sqlalchemy.Connection,
) -> models.UpdatePhoneStatus:
    """
    Update user for the given email.
    """

    # check if user exists
    if not user_exists(email, con):
        return models.UpdatePhoneStatus.USER_NOT_FOUND

    validity_res = check_phone_validity(new_phone)
    if validity_res != models.UpdatePhoneStatus.SUCCESS:
        return validity_res

    res = update_user(
        email=email,
        values={tables.ClientUsers.phone: new_phone},
        con=con,
    )

    if res:
        return models.UpdatePhoneStatus.SUCCESS
    else:
        return models.UpdatePhoneStatus.FAILURE


def check_address_validity(address: str) -> bool:
    """
    Check if address is valid.
    """
    return len(address) <= 0


def update_address(
    email: str,
    new_address: str,
    con: sqlalchemy.Connection,
) -> models.UpdateAddressStatus:
    """
    Update user for the given email.
    """

    # check if user exists
    if not user_exists(email, con):
        return models.UpdateAddressStatus.USER_NOT_FOUND

    if not check_address_validity(new_address):
        return models.UpdateAddressStatus.ADDRESS_IS_NONE

    res = update_user(
        email=email,
        values={tables.ClientUsers.address: new_address},
        con=con,
    )

    if res:
        return models.UpdateAddressStatus.SUCCESS
    else:
        return models.UpdateAddressStatus.FAILURE


def update_city(
    email: str,
    new_city: str,
    con: sqlalchemy.Connection,
) -> models.UpdateStatus:
    """
    Update user for the given email.
    """

    # check if user exists
    if not user_exists(email, con):
        return models.UpdateStatus.USER_NOT_FOUND

    res = update_user(
        email=email,
        values={tables.ClientUsers.city: new_city},
        con=con,
    )

    if res:
        return models.UpdateStatus.SUCCESS
    else:
        return models.UpdateStatus.FAILURE


def update_zip(
    email: str,
    new_zip: str,
    con: sqlalchemy.Connection,
) -> models.UpdateStatus:
    """
    Update user for the given email.
    """

    # check if user exists
    if not user_exists(email, con):
        return models.UpdateStatus.USER_NOT_FOUND

    res = update_user(
        email=email,
        values={tables.ClientUsers.zip: new_zip},
        con=con,
    )

    if res:
        return models.UpdateStatus.SUCCESS
    else:
        return models.UpdateStatus.FAILURE


def update_country(
    email: str,
    new_country: str,
    con: sqlalchemy.Connection,
) -> models.UpdateStatus:
    """
    Update user for the given email.
    """

    # check if user exists
    if not user_exists(email, con):
        return models.UpdateStatus.USER_NOT_FOUND

    res = update_user(
        email=email,
        values={tables.ClientUsers.country: new_country},
        con=con,
    )

    if res == 1:
        return models.UpdateStatus.SUCCESS
    else:
        return models.UpdateStatus.FAILURE


def update_imgBase64(
    email: str,
    new_imgBase64: str,
    con: sqlalchemy.Connection,
) -> models.UpdateStatus:
    """
    Update user for the given email.
    """

    # check if user exists
    if not user_exists(email, con):
        return models.UpdateStatus.USER_NOT_FOUND

    res = update_user(
        email=email,
        values={tables.ClientUsers.imgBase64: new_imgBase64},
        con=con,
    )

    if res:
        return models.UpdateStatus.SUCCESS
    else:
        return models.UpdateStatus.FAILURE
