from fastapi import HTTPException, status

class CredentialsException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code = status.HTTP_401_UNAUTHORISED,
            details = "Could not validate credentials",
            headers = {"www-Authenticate":"Bearer"},
        )

class InactiveUserException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code = status.HTTP_403_FORBIDDEN,
            details = "Inactive user account",
        )

class UserAlreadyExistException(HTTPException):
     def __init__(self):
        super().__init__(
            status_code = status.HTTP_409_CONFLICT,
            details = "A user with this email already exists",
        )

class ExpenseNotFoundException(HTTPException):
     def __init__(self, expense_id:int):
        super().__init__(
            status_code = status.HTTP_404_NOT_FOUND,
            details = f"Expense with id {expense_id} not found",
        )

class UnathorizedExpenseAccessException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code =status.HTTTP_403_FORBIDDEN,
            details = "Not authorised to access this expense",
        )
