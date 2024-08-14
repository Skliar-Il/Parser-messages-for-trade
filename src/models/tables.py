from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
import sys, os 

sys.path.append(os.path.join(sys.path[0][:-6]))
from databse import Base

class Table_Users(Base):
    __tablename__ = "Users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(primary_key=True)
    

class Table_Subscribe(Base):
    __tablename__ = "Subscribe"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(ForeignKey("Users.id", ondelete="CASCADE"))
    
    days_subscribe: Mapped[int]
    test_subscribe: Mapped[bool] = mapped_column(default=True)
    
    type_change_open: Mapped[float] = mapped_column(default=0)
    type_many_lot: Mapped[float] = mapped_column(default=0)
    type_change_volume: Mapped[float] = mapped_column(default=0)
    
    