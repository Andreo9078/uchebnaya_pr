from src.exceptions import CommentDoesNotExist, RequestDoesNotExist
from src.model.requests.domain import Comment
from src.model.requests.repo.commet_repo import CommentRepo
from src.model.requests.repo.request_repo import RequestRepo
from src.model.requests.schemes import CommentCreate, CommentUpdate


class CommentService:
    def __init__(
        self, comment_repo: CommentRepo,
        request_repo: RequestRepo
    ):
        self.comment_repo = comment_repo
        self.request_repo = request_repo

    def get(self, obj_id: int) -> Comment:
        comment = self.comment_repo.get(obj_id)
        if comment is None:
            raise CommentDoesNotExist(obj_id)

    def get_all(self) -> list[Comment]:
        comments = self.comment_repo.get_all()
        return comments

    def create(
        self, comment_create: CommentCreate
    ) -> Comment:
        request = self.request_repo.get(comment_create.request_id)
        if request is None:
            raise RequestDoesNotExist(comment_create.request_id)

        comment = self.comment_repo.create(comment_create.model_dump())

        return comment

    def update(
        self, obj_id: int, comment_update: CommentUpdate
    ) -> Comment:
        comment = self.comment_repo.get(obj_id)
        if comment is None:
            raise CommentDoesNotExist(obj_id)

        updated_comment = self.comment_repo.update(
            obj_id, comment_update.model_dump(exclude_none=True)
        )

        return updated_comment

    def delete(self, obj_id: int) -> None:
        comment = self.comment_repo.get(obj_id)
        if comment is None:
            raise CommentDoesNotExist(obj_id)

        self.comment_repo.delete(obj_id)
