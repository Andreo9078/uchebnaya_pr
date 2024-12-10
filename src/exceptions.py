from typing import Optional, Any


class MissingEnvVar(Exception):
    def __init__(self, var_name: str) -> None:
        self.var_name = var_name

    def __str__(self) -> str:
        return f"Missing environment variable '{self.var_name}'"


class ObjectDoesNotExist(Exception):
    def __init__(
        self,
        object_id: Optional[Any] = None,
        object_class_name: Optional[str] = None,
    ) -> None:
        self.object_class_name = object_class_name
        self.object_id = object_id

    def __str__(self) -> str:
        if self.object_class_name and self.object_id:
            return f"Object {self.object_class_name} with id '{self.object_id}' does not exist."
        elif self.object_id:
            return f"Object with id '{self.object_id}' does not exist."
        else:
            return "Object does not exist."


class PermissionDenied(Exception):
    def __str__(self) -> str:
        return "Permission denied"


class RoleDoesNotExist(Exception):
    def __init__(self, role_id: int) -> None:
        self.role_id = role_id

    def __str__(self) -> str:
        return f"Роль с id \"{self.role_id}\" не существует"

class UserDoesNotExist(Exception):
    def __init__(self, user_id: int) -> None:
        self.user_id = user_id

    def __str__(self) -> str:
        return f"Пользователь с {self.user_id} не существует"
