from src.database import get_session
from src.model.auth.repos.role_repo import RoleRepo
from src.model.auth.repos.user_repo import UserRepo
from src.model.auth.schemes import RoleCreate, UserCreate
from src.model.auth.services.role_service import RoleService
from src.model.auth.services.user_service import UserService
from src.state import state

session = get_session()

role_repo = RoleRepo(session)
user_repo = UserRepo(session)

role_service = RoleService(role_repo)
user_service = UserService(user_repo, role_repo, state)

role = role_service.create(
    RoleCreate(name="test")
)

user = user_service.create(
    UserCreate(
        username="test_username",
        password="test_password",
        phone_number="89670617593",
        name="test_name",
        last_name="test_last_name",
        patronymic="test_patronymic",
        role_id=1
    )
)

print(role)
print(user)
