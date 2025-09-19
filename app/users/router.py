from fastapi import APIRouter, Depends, HTTPException, Query, status
from app.users.schemas import UserAddSchema, UserFilterSchema, UserGetSchema, UserUpdateSchema
from app.users.service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Пользователи"]
)

@router.get(
    "",
    summary="Список пользователей",
    description="Возвращает список всех пользователей. Можно фильтровать по параметрам."
)
async def get_list_users(filters: UserFilterSchema = Depends()) -> list[UserGetSchema]:
    result = await UserService.get_list(filters)
    return result

@router.get(
    "/{user_id}",
    summary="Получить пользователя по ID",
    description="Возвращает пользователя по ID. Если пользователя нет, возвращает 404.",
    responses={404: {"description": "Пользователь не найден"}}
)
async def get_user(user_id: int) -> UserGetSchema:
    result = await UserService.get_by_id(user_id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return result

@router.post(
    "/create",
    response_model=dict,
    summary="Создать пользователя",
    description="Создаёт нового пользователя. Возвращает статус операции.",
    responses={409: {"description": "Не удалось создать пользователя"}}
)
async def create_user(user: UserAddSchema):
    created = await UserService.create_user(user)
    if not created:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Can not create user")
    return {"status": "success", "message": "User created"}

@router.delete(
    "/delete/{user_id}",
    response_model=dict,
    summary="Удалить пользователя",
    description="Удаляет пользователя по ID. Если пользователя нет, возвращает 404.",
    responses={404: {"description": "Пользователь не найден"}}
)
async def delete_user(user_id: int):
    deleted = await UserService.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return {"status": "success", "message": f"User {user_id} deleted"}

@router.put(
    "/update/{user_id}",
    response_model=dict,
    summary="Обновить пользователя",
    description="Обновляет данные пользователя по ID. Если пользователя нет, возвращает 404.",
    responses={404: {"description": "Пользователь не найден"}}
)
async def update_user(user_id: int, user: UserUpdateSchema):
    updated = await UserService.update_user(user_id, user)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return {"status": "success", "message": f"User {user_id} updated"}