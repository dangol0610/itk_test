from sqlalchemy import delete, insert, select, update
from app.database import async_session_maker
from app.users.models import Users
from app.users.schemas import UserAddSchema, UserFilterSchema, UserUpdateSchema

class UserService:
    
    @classmethod
    async def get_by_id(cls, user_id: int):
        async with async_session_maker() as session:
            query = select(Users).filter_by(id=user_id)
            user = await session.execute(query)
            return user.scalar_one_or_none()
    
    @classmethod
    async def get_list(cls, filters: UserFilterSchema):
        async with async_session_maker() as session:
            filters_dict = filters.model_dump(exclude_none=True)
            query = select(Users).filter_by(**filters_dict)
            users = await session.execute(query)
            return users.scalars().all()
        
    @classmethod
    async def create_user(cls, user_data: UserAddSchema):
        async with async_session_maker() as session:
            add_data = user_data.model_dump()
            query = insert(Users).values(**add_data).returning(Users)
            result = await session.execute(query)
            await session.commit()
            return result.scalar_one_or_none()
        
    @classmethod
    async def delete_user(cls, user_id: int):
        async with async_session_maker() as session:
            query = delete(Users).where(Users.id==user_id).returning(Users.id)
            result = await session.execute(query)
            await session.commit()
            return result.scalar_one_or_none()
        
    @classmethod
    async def update_user(cls, user_id: int, user_data: UserUpdateSchema):
        async with async_session_maker() as session:
            update_data = user_data.model_dump(exclude_unset=True)
            query = update(Users).where(Users.id==user_id).values(**update_data).returning(Users)
            result = await session.execute(query)
            await session.commit()
            return result.scalar_one_or_none()
            