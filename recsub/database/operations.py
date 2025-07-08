import asyncpg
from datetime import date
from typing import List, Optional, Dict
from .connection import DB_URL
from .models import User, Subscription, PaymentFrequency, SubscriptionStatus


class UserOperations:
    """CRUD operations for users."""

    @staticmethod
    async def create_user(clerk_user_id: str, email: str) -> User:
        """Create a new user."""
        conn = await asyncpg.connect(DB_URL)
        try:
            query = """
                INSERT INTO users (clerk_user_id, email)
                VALUES ($1, $2)
                RETURNING id, clerk_user_id, email, created_at, updated_at
            """
            row = await conn.fetchrow(query, clerk_user_id, email)
            return User(
                id=str(row["id"]),
                clerk_user_id=row["clerk_user_id"],
                email=row["email"],
                created_at=row["created_at"],
                updated_at=row["updated_at"],
            )
        finally:
            await conn.close()

    @staticmethod
    async def get_user_by_clerk_id(clerk_user_id: str) -> Optional[User]:
        """Get user by Clerk user ID."""
        conn = await asyncpg.connect(DB_URL)
        try:
            query = """
                SELECT id, clerk_user_id, email, created_at, updated_at
                FROM users
                WHERE clerk_user_id = $1
            """
            row = await conn.fetchrow(query, clerk_user_id)
            if row:
                return User(
                    id=str(row["id"]),
                    clerk_user_id=row["clerk_user_id"],
                    email=row["email"],
                    created_at=row["created_at"],
                    updated_at=row["updated_at"],
                )
            return None
        finally:
            await conn.close()

    @staticmethod
    async def get_user_by_id(user_id: str) -> Optional[User]:
        """Get user by user ID."""
        conn = await asyncpg.connect(DB_URL)
        try:
            query = """
                SELECT id, clerk_user_id, email, created_at, updated_at
                FROM users
                WHERE id = $1
            """
            row = await conn.fetchrow(query, user_id)
            if row:
                return User(
                    id=str(row["id"]),
                    clerk_user_id=row["clerk_user_id"],
                    email=row["email"],
                    created_at=row["created_at"],
                    updated_at=row["updated_at"],
                )
            return None
        finally:
            await conn.close()

    @staticmethod
    async def update_user_email(user_id: str, email: str) -> Optional[User]:
        """Update user email."""
        conn = await asyncpg.connect(DB_URL)
        try:
            query = """
                UPDATE users
                SET email = $2
                WHERE id = $1
                RETURNING id, clerk_user_id, email, created_at, updated_at
            """
            row = await conn.fetchrow(query, user_id, email)
            if row:
                return User(
                    id=str(row["id"]),
                    clerk_user_id=row["clerk_user_id"],
                    email=row["email"],
                    created_at=row["created_at"],
                    updated_at=row["updated_at"],
                )
            return None
        finally:
            await conn.close()

    @staticmethod
    async def delete_user(user_id: str) -> bool:
        """Delete user and all associated subscriptions."""
        conn = await asyncpg.connect(DB_URL)
        try:
            query = "DELETE FROM users WHERE id = $1"
            result = await conn.execute(query, user_id)
            return result == "DELETE 1"
        finally:
            await conn.close()


class SubscriptionOperations:
    """CRUD operations for subscriptions."""

    @staticmethod
    async def create_subscription(
        user_id: str,
        service_name: str,
        category: str,
        price: float,
        payment_frequency: PaymentFrequency,
        first_payment_date: date,
        next_payment_date: date,
        logo_url: Optional[str] = None,
        status: SubscriptionStatus = SubscriptionStatus.ACTIVE,
    ) -> Subscription:
        """Create a new subscription."""
        conn = await asyncpg.connect(DB_URL)
        try:
            query = """
                INSERT INTO subscriptions (
                    user_id, service_name, category, price, payment_frequency,
                    first_payment_date, next_payment_date, logo_url, status
                )
                VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9)
                RETURNING id, user_id, service_name, category, price, payment_frequency,
                         first_payment_date, next_payment_date, logo_url, status,
                         created_at, updated_at
            """
            row = await conn.fetchrow(
                query,
                user_id,
                service_name,
                category,
                price,
                payment_frequency.value,
                first_payment_date,
                next_payment_date,
                logo_url,
                status.value,
            )
            return Subscription(
                id=str(row["id"]),
                user_id=str(row["user_id"]),
                service_name=row["service_name"],
                category=row["category"],
                price=float(row["price"]),
                payment_frequency=PaymentFrequency(row["payment_frequency"]),
                first_payment_date=row["first_payment_date"],
                next_payment_date=row["next_payment_date"],
                status=SubscriptionStatus(row["status"]),
                logo_url=row["logo_url"],
                created_at=row["created_at"],
                updated_at=row["updated_at"],
            )
        finally:
            await conn.close()

    @staticmethod
    async def get_subscription_by_id(subscription_id: str) -> Optional[Subscription]:
        """Get subscription by ID."""
        conn = await asyncpg.connect(DB_URL)
        try:
            query = """
                SELECT id, user_id, service_name, category, price, payment_frequency,
                       first_payment_date, next_payment_date, logo_url, status,
                       created_at, updated_at
                FROM subscriptions
                WHERE id = $1
            """
            row = await conn.fetchrow(query, subscription_id)
            if row:
                return Subscription(
                    id=str(row["id"]),
                    user_id=str(row["user_id"]),
                    service_name=row["service_name"],
                    category=row["category"],
                    price=float(row["price"]),
                    payment_frequency=PaymentFrequency(row["payment_frequency"]),
                    first_payment_date=row["first_payment_date"],
                    next_payment_date=row["next_payment_date"],
                    status=SubscriptionStatus(row["status"]),
                    logo_url=row["logo_url"],
                    created_at=row["created_at"],
                    updated_at=row["updated_at"],
                )
            return None
        finally:
            await conn.close()

    @staticmethod
    async def get_user_subscriptions(
        user_id: str, status: Optional[SubscriptionStatus] = None
    ) -> List[Subscription]:
        """Get all subscriptions for a user, optionally filtered by status."""
        conn = await asyncpg.connect(DB_URL)
        try:
            if status:
                query = """
                    SELECT id, user_id, service_name, category, price, payment_frequency,
                           first_payment_date, next_payment_date, logo_url, status,
                           created_at, updated_at
                    FROM subscriptions
                    WHERE user_id = $1 AND status = $2
                    ORDER BY created_at DESC
                """
                rows = await conn.fetch(query, user_id, status.value)
            else:
                query = """
                    SELECT id, user_id, service_name, category, price, payment_frequency,
                           first_payment_date, next_payment_date, logo_url, status,
                           created_at, updated_at
                    FROM subscriptions
                    WHERE user_id = $1
                    ORDER BY created_at DESC
                """
                rows = await conn.fetch(query, user_id)

            return [
                Subscription(
                    id=str(row["id"]),
                    user_id=str(row["user_id"]),
                    service_name=row["service_name"],
                    category=row["category"],
                    price=float(row["price"]),
                    payment_frequency=PaymentFrequency(row["payment_frequency"]),
                    first_payment_date=row["first_payment_date"],
                    next_payment_date=row["next_payment_date"],
                    status=SubscriptionStatus(row["status"]),
                    logo_url=row["logo_url"],
                    created_at=row["created_at"],
                    updated_at=row["updated_at"],
                )
                for row in rows
            ]
        finally:
            await conn.close()

    @staticmethod
    async def update_subscription(
        subscription_id: str,
        service_name: Optional[str] = None,
        category: Optional[str] = None,
        price: Optional[float] = None,
        payment_frequency: Optional[PaymentFrequency] = None,
        first_payment_date: Optional[date] = None,
        next_payment_date: Optional[date] = None,
        logo_url: Optional[str] = None,
        status: Optional[SubscriptionStatus] = None,
    ) -> Optional[Subscription]:
        """Update subscription fields."""
        conn = await asyncpg.connect(DB_URL)
        try:
            updates = []
            values = []
            param_count = 1

            if service_name is not None:
                updates.append(f"service_name = ${param_count}")
                values.append(service_name)
                param_count += 1

            if category is not None:
                updates.append(f"category = ${param_count}")
                values.append(category)
                param_count += 1

            if price is not None:
                updates.append(f"price = ${param_count}")
                values.append(price)
                param_count += 1

            if payment_frequency is not None:
                updates.append(f"payment_frequency = ${param_count}")
                values.append(payment_frequency.value)
                param_count += 1

            if first_payment_date is not None:
                updates.append(f"first_payment_date = ${param_count}")
                values.append(first_payment_date)
                param_count += 1

            if next_payment_date is not None:
                updates.append(f"next_payment_date = ${param_count}")
                values.append(next_payment_date)
                param_count += 1

            if logo_url is not None:
                updates.append(f"logo_url = ${param_count}")
                values.append(logo_url)
                param_count += 1

            if status is not None:
                updates.append(f"status = ${param_count}")
                values.append(status.value)
                param_count += 1

            if not updates:
                return None

            query = f"""
                UPDATE subscriptions
                SET {", ".join(updates)}
                WHERE id = ${param_count}
                RETURNING id, user_id, service_name, category, price, payment_frequency,
                         first_payment_date, next_payment_date, logo_url, status,
                         created_at, updated_at
            """
            values.append(subscription_id)

            row = await conn.fetchrow(query, *values)
            if row:
                return Subscription(
                    id=str(row["id"]),
                    user_id=str(row["user_id"]),
                    service_name=row["service_name"],
                    category=row["category"],
                    price=float(row["price"]),
                    payment_frequency=PaymentFrequency(row["payment_frequency"]),
                    first_payment_date=row["first_payment_date"],
                    next_payment_date=row["next_payment_date"],
                    status=SubscriptionStatus(row["status"]),
                    logo_url=row["logo_url"],
                    created_at=row["created_at"],
                    updated_at=row["updated_at"],
                )
            return None
        finally:
            await conn.close()

    @staticmethod
    async def delete_subscription(subscription_id: str) -> bool:
        """Delete subscription."""
        conn = await asyncpg.connect(DB_URL)
        try:
            query = "DELETE FROM subscriptions WHERE id = $1"
            result = await conn.execute(query, subscription_id)
            return result == "DELETE 1"
        finally:
            await conn.close()

    @staticmethod
    async def get_user_monthly_spending(user_id: str) -> float:
        """Calculate total monthly spending for a user."""
        conn = await asyncpg.connect(DB_URL)
        try:
            query = """
                SELECT
                    COALESCE(SUM(
                        CASE
                            WHEN payment_frequency = 'monthly' THEN price
                            WHEN payment_frequency = 'yearly' THEN price / 12
                            WHEN payment_frequency = 'weekly' THEN price * 4.33
                            WHEN payment_frequency = 'quarterly' THEN price / 3
                            ELSE 0
                        END
                    ), 0) as monthly_total
                FROM subscriptions
                WHERE user_id = $1 AND status = 'active'
            """
            result = await conn.fetchval(query, user_id)
            return float(result) if result else 0.0
        finally:
            await conn.close()

    @staticmethod
    async def get_user_yearly_spending(user_id: str) -> float:
        """Calculate total yearly spending for a user."""
        conn = await asyncpg.connect(DB_URL)
        try:
            query = """
                SELECT
                    COALESCE(SUM(
                        CASE
                            WHEN payment_frequency = 'monthly' THEN price * 12
                            WHEN payment_frequency = 'yearly' THEN price
                            WHEN payment_frequency = 'weekly' THEN price * 52
                            WHEN payment_frequency = 'quarterly' THEN price * 4
                            ELSE 0
                        END
                    ), 0) as yearly_total
                FROM subscriptions
                WHERE user_id = $1 AND status = 'active'
            """
            result = await conn.fetchval(query, user_id)
            return float(result) if result else 0.0
        finally:
            await conn.close()

    @staticmethod
    async def get_subscriptions_by_category(user_id: str) -> Dict[str, float]:
        """Get monthly spending by category for a user."""
        conn = await asyncpg.connect(DB_URL)
        try:
            query = """
                SELECT
                    category,
                    COALESCE(SUM(
                        CASE
                            WHEN payment_frequency = 'monthly' THEN price
                            WHEN payment_frequency = 'yearly' THEN price / 12
                            WHEN payment_frequency = 'weekly' THEN price * 4.33
                            WHEN payment_frequency = 'quarterly' THEN price / 3
                            ELSE 0
                        END
                    ), 0) as monthly_total
                FROM subscriptions
                WHERE user_id = $1 AND status = 'active'
                GROUP BY category
                ORDER BY monthly_total DESC
            """
            rows = await conn.fetch(query, user_id)
            return {row["category"]: float(row["monthly_total"]) for row in rows}
        finally:
            await conn.close()
