-- ============================================================================
-- Stock_Platform
-- Migration: 0010_create_schemas.sql
-- Description: Initial database schemas and common objects
-- ============================================================================

-- Create schemas
CREATE SCHEMA IF NOT EXISTS core;
CREATE SCHEMA IF NOT EXISTS market;
CREATE SCHEMA IF NOT EXISTS system;

-- ============================================================================
-- Common function to automatically update updated_at
-- ============================================================================

CREATE OR REPLACE FUNCTION system.set_updated_at()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$;
