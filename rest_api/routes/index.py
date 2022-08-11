from fastapi import APIRouter

router: APIRouter = APIRouter()


@router.get("/")
def index() -> str:
    return "hello, world!"
