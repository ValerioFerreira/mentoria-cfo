-- Enum additions live in their own migration so PostgreSQL can commit the
-- new labels before the following migration uses them for legacy rows.
ALTER TYPE "BillingPaymentStatus" ADD VALUE 'PARTIALLY_REFUNDED';
ALTER TYPE "BillingPaymentStatus" ADD VALUE 'DISPUTED';
ALTER TYPE "BillingPaymentStatus" ADD VALUE 'CHARGEBACK_LOST';
ALTER TYPE "BillingPaymentStatus" ADD VALUE 'CHARGEBACK_WON';
