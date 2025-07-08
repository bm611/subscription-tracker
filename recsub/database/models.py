from datetime import datetime, date
from enum import Enum
from typing import Optional, Dict, Any
from dataclasses import dataclass


class PaymentFrequency(Enum):
    MONTHLY = "monthly"
    YEARLY = "yearly"
    WEEKLY = "weekly"
    QUARTERLY = "quarterly"


class SubscriptionStatus(Enum):
    ACTIVE = "active"
    CANCELED = "canceled"
    PAUSED = "paused"


@dataclass
class User:
    id: str
    clerk_user_id: str
    email: str
    created_at: datetime
    updated_at: datetime


@dataclass
class Subscription:
    id: str
    user_id: str
    service_name: str
    category: str
    price: float
    payment_frequency: PaymentFrequency
    first_payment_date: date
    next_payment_date: date
    status: SubscriptionStatus
    logo_url: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert subscription to dictionary for JSON serialization."""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "service_name": self.service_name,
            "category": self.category,
            "price": self.price,
            "payment_frequency": self.payment_frequency.value,
            "first_payment_date": self.first_payment_date.isoformat(),
            "next_payment_date": self.next_payment_date.isoformat(),
            "status": self.status.value,
            "logo_url": self.logo_url,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
