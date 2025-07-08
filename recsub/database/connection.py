import asyncpg
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()
DB_URL = os.getenv("POSTGRES_URL")


async def init_db():
    """Initialize database with tables and indexes."""
    conn = await asyncpg.connect(DB_URL)

    # Create users table first (referenced by subscriptions)
    await conn.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            clerk_user_id VARCHAR(255) UNIQUE NOT NULL,
            email VARCHAR(255) NOT NULL,
            created_at TIMESTAMPTZ DEFAULT NOW(),
            updated_at TIMESTAMPTZ DEFAULT NOW()
        )
        """
    )
    print("Users Table Created")

    # Create ENUM types
    await conn.execute(
        """
        DO $$ BEGIN
            CREATE TYPE payment_frequency AS ENUM ('monthly', 'yearly', 'weekly', 'quarterly');
        EXCEPTION
            WHEN duplicate_object THEN null;
        END $$;
        """
    )

    await conn.execute(
        """
        DO $$ BEGIN
            CREATE TYPE subscription_status AS ENUM ('active', 'canceled', 'paused');
        EXCEPTION
            WHEN duplicate_object THEN null;
        END $$;
        """
    )
    print("ENUM Types Created")

    # Create subscriptions table
    await conn.execute(
        """
        CREATE TABLE IF NOT EXISTS subscriptions (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            user_id UUID NOT NULL,
            service_name VARCHAR(255) NOT NULL,
            logo_url VARCHAR(500),
            category VARCHAR(100) NOT NULL,
            price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
            payment_frequency payment_frequency NOT NULL,
            first_payment_date DATE NOT NULL,
            next_payment_date DATE NOT NULL,
            status subscription_status NOT NULL DEFAULT 'active',
            created_at TIMESTAMPTZ DEFAULT NOW(),
            updated_at TIMESTAMPTZ DEFAULT NOW(),

            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )
        """
    )
    print("Subscriptions Table Created")

    # Create indexes for performance
    await conn.execute(
        "CREATE INDEX IF NOT EXISTS idx_users_clerk_id ON users(clerk_user_id)"
    )
    await conn.execute(
        "CREATE INDEX IF NOT EXISTS idx_subscriptions_user_id ON subscriptions(user_id)"
    )
    await conn.execute(
        "CREATE INDEX IF NOT EXISTS idx_subscriptions_status ON subscriptions(status)"
    )
    await conn.execute(
        "CREATE INDEX IF NOT EXISTS idx_subscriptions_next_payment ON subscriptions(next_payment_date)"
    )
    print("Indexes Created")

    # Create trigger to update updated_at timestamp
    await conn.execute(
        """
        CREATE OR REPLACE FUNCTION update_updated_at_column()
        RETURNS TRIGGER AS $$
        BEGIN
            NEW.updated_at = NOW();
            RETURN NEW;
        END;
        $$ language 'plpgsql';
        """
    )

    await conn.execute(
        """
        DROP TRIGGER IF EXISTS update_users_updated_at ON users;
        CREATE TRIGGER update_users_updated_at
            BEFORE UPDATE ON users
            FOR EACH ROW
            EXECUTE FUNCTION update_updated_at_column();
        """
    )

    await conn.execute(
        """
        DROP TRIGGER IF EXISTS update_subscriptions_updated_at ON subscriptions;
        CREATE TRIGGER update_subscriptions_updated_at
            BEFORE UPDATE ON subscriptions
            FOR EACH ROW
            EXECUTE FUNCTION update_updated_at_column();
        """
    )
    print("Triggers Created")

    await conn.close()
    print("Database initialization complete")


if __name__ == "__main__":
    asyncio.run(init_db())
