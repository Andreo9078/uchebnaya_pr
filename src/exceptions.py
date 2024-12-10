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


class ServiceError(Exception):
    pass


class PermissionDenied(ServiceError):
    def __str__(self) -> str:
        return "Permission denied"


class RoleDoesNotExist(ServiceError):
    def __init__(self, role_id: int) -> None:
        self.role_id = role_id

    def __str__(self) -> str:
        return f"Роль с id \"{self.role_id}\" не существует"


class UserDoesNotExist(ServiceError):
    def __init__(self, user_id: int) -> None:
        self.user_id = user_id

    def __str__(self) -> str:
        return f"Пользователь с \"{self.user_id}\" не существует"


class CommentDoesNotExist(ServiceError):
    def __init__(self, comment_id: int) -> None:
        self.comment_id = comment_id

    def __str__(self) -> str:
        return f"Комментарий с id \"{self.comment_id}\" не существует"


class RequestDoesNotExist(ServiceError):
    def __init__(self, request_id: int) -> None:
        self.request_id = request_id

    def __str__(self) -> str:
        return f"Заявка с id \"{self.request_id}\" не существует"


class DetailDoesNotExist(ServiceError):
    def __init__(self, detail_id: int) -> None:
        self.detail_id = detail_id

    def __str__(self) -> str:
        return f"Деталь с id \"{self.detail_id}\" не существует"


class TechTypeDoesNotExist(ServiceError):
    def __init__(self, tech_type_id: int) -> None:
        self.tech_type_id = tech_type_id

    def __str__(self) -> str:
        return f"Типа техники с id \"{self.tech_type_id}\" не существует"


class RequestStatusDoesNotExist(ServiceError):
    def __init__(self, request_id: int) -> None:
        self.request_id = request_id

    def __str__(self) -> str:
        return f"Статуса заявки с id\"{self.request_id}\" не существует"


class RequestDoesNotExists(ServiceError):
    def __init__(self, request_id: int) -> None:
        self.request_id = request_id

    def __str__(self) -> str:
        return f"Заявка с id \"{self.request_id}\" не существует"


class UsedDetailDoesNotExist(ServiceError):
    def __init__(self, detail_id: int) -> None:
        self.detail_id = detail_id

    def __str__(self) -> str:
        return f"Деталь с id \"{self.detail_id}\" не существует"


class RolesMismatch(Exception):
    pass
