from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, UniqueConstraint, insert, text


import sys, os, asyncio, datetime

sys.path.append(os.path.join(sys.path[0][:-6]))
from database import Base, async_session_factory

class Table_Users(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(unique=True)
    detail_subscribe: Mapped["Table_Subscribe"] = relationship(
        back_populates="user", uselist=False
    )
    date_register: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    

class Table_Subscribe(Base):
    __tablename__ = "subscribe"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(ForeignKey("users.tg_id", ondelete="CASCADE"), unique=True)
    user: Mapped["Table_Users"] = relationship(
        back_populates="detail_subscribe", uselist=False
    )
    
    days_subscribe: Mapped[int] = mapped_column(default=0)
    test_subscribe: Mapped[bool] = mapped_column(default=True)
    
    type_change_open: Mapped[float] = mapped_column(default=0)
    type_many_lot: Mapped[float] = mapped_column(default=0)
    type_change_volume: Mapped[float] = mapped_column(default=0)
    
    MSNG: Mapped[bool] = mapped_column(default=True)
    POSI: Mapped[bool] = mapped_column(default=True) 
    YNDX: Mapped[bool] = mapped_column(default=True) 
    ALRS: Mapped[bool] = mapped_column(default=True) 
    AFLT: Mapped[bool] = mapped_column(default=True) 
    BSPB: Mapped[bool] = mapped_column(default=True) 
    VTBR: Mapped[bool] = mapped_column(default=True) 
    GAZP: Mapped[bool] = mapped_column(default=True) 
    GMKN: Mapped[bool] = mapped_column(default=True) 
    LEAS: Mapped[bool] = mapped_column(default=True) 
    EUTR: Mapped[bool] = mapped_column(default=True) 
    AQUA: Mapped[bool] = mapped_column(default=True) 
    IRAO: Mapped[bool] = mapped_column(default=True) 
    LENT: Mapped[bool] = mapped_column(default=True) 
    LSRG: Mapped[bool] = mapped_column(default=True) 
    LKOH: Mapped[bool] = mapped_column(default=True) 
    MVID: Mapped[bool] = mapped_column(default=True) 
    MTLR: Mapped[bool] = mapped_column(default=True) 
    CBOM: Mapped[bool] = mapped_column(default=True) 
    VKCO: Mapped[bool] = mapped_column(default=True) 
    GEMC: Mapped[bool] = mapped_column(default=True) 
    MAGN: Mapped[bool] = mapped_column(default=True) 
    MOEX: Mapped[bool] = mapped_column(default=True) 
    MBNK: Mapped[bool] = mapped_column(default=True) 
    MTSS: Mapped[bool] = mapped_column(default=True) 
    NLMK: Mapped[bool] = mapped_column(default=True) 
    BELU: Mapped[bool] = mapped_column(default=True) 
    NVTK: Mapped[bool] = mapped_column(default=True) 
    PIKK: Mapped[bool] = mapped_column(default=True) 
    PLZL: Mapped[bool] = mapped_column(default=True) 
    RENI: Mapped[bool] = mapped_column(default=True) 
    ROSN: Mapped[bool] = mapped_column(default=True) 
    FEES: Mapped[bool] = mapped_column(default=True) 
    RTKM: Mapped[bool] = mapped_column(default=True) 
    RUAL: Mapped[bool] = mapped_column(default=True)     
    HYDR: Mapped[bool] = mapped_column(default=True) 
    RNFT: Mapped[bool] = mapped_column(default=True) 
    SMLT: Mapped[bool] = mapped_column(default=True) 
    SBER: Mapped[bool] = mapped_column(default=True) 
    CHMF: Mapped[bool] = mapped_column(default=True) 
    SGZH: Mapped[bool] = mapped_column(default=True) 
    SELG: Mapped[bool] = mapped_column(default=True) 
    AFKS: Mapped[bool] = mapped_column(default=True) 
    SVCB: Mapped[bool] = mapped_column(default=True) 
    FLOT: Mapped[bool] = mapped_column(default=True) 
    TATN: Mapped[bool] = mapped_column(default=True) 
    TGKA: Mapped[bool] = mapped_column(default=True) 
    TCSG: Mapped[bool] = mapped_column(default=True) 
    PHOR: Mapped[bool] = mapped_column(default=True) 
    ELFV: Mapped[bool] = mapped_column(default=True) 
    ENPG: Mapped[bool] = mapped_column(default=True) 
    SFIN: Mapped[bool] = mapped_column(default=True) 
    UPRO: Mapped[bool] = mapped_column(default=True)
    MTLRP: Mapped[bool] = mapped_column(default=True)
    TRNFP: Mapped[bool] = mapped_column(default=True)
    TATNP: Mapped[bool] = mapped_column(default=True)
    SBERP: Mapped[bool] = mapped_column(default=True)
    RTKMP: Mapped[bool] = mapped_column(default=True)
    
    
    
      