from pydantic import BaseModel, Field, ConfigDict, EmailStr
from typing import Optional
from enum import Enum
from decimal import Decimal
from datetime import date

class BillingCycle(str,Enum):
    WEEKLY = "Weekly"
    MONTHLY = "Monthly"
    YEARLY = "Yearly"

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    
    model_config = ConfigDict(from_attributes=True)


class SubCreate(BaseModel):
    service_name : str = Field(..., description= "Add the name of the service")
    cost : Decimal = Field(..., ge=0,decimal_places=2)
    billing_cycle : BillingCycle = Field(...)
    next_billing_date : date = Field(...)

class SubResponse(BaseModel):
    id: int
    service_name: str
    cost: Decimal
    billing_cycle: str
    next_billing_date: date

    model_config = ConfigDict(from_attributes=True)

class SubUpdate(BaseModel):
    service_name: Optional[str] = Field(None, description="Update the name of the service")
    cost: Optional[Decimal] = Field(None, ge=0, decimal_places=2)
    billing_cycle: Optional[BillingCycle] = Field(None)
    next_billing_date: Optional[date] = Field(None)