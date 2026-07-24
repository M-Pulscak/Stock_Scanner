# Stock Platform

## 1) Purpose
Stock Platform is a Python/PostgreSQL platform for collecting and managing **raw financial market data**.
The database is the single source of truth. All calculations (Power BI, Python, backtesting, trading logic) are performed outside the database.


# 2) Vision
Build a reliable, extensible platform for collecting raw market data.

V1 includes:
- Reference data
- Asset metadata
- Daily prices max. 5 year ago
- Fundamental snapshots
- Macro data
- Index membership (stock only in S&P 500, Dow Jones Industrial, Russell 2000 and base indexes)
- Sectors and industries

V1 excludes:
- Technical indicators
- Trading strategies
- External ratings (architecture only)

# Architecture
Data Providers -> Importers -> Repositories -> PostgreSQL -> Analytics (Power BI, Python, Backtesting)

# 3) Project Structure
src/
  config/
  db/
  models/
  providers/
  services/
  mappers/
  repositories/
  lookups/
  importers/
  utils/

# 4) Coding Standards
dataclass(slots=True) for models    
dependency injection    
repository only access to DB    
provider only communication with API    
mapper only model conversion    
no business logic in repository    
no SQL outside repository    

# 4) Database Model
core: assets, exchanges, markets, currencies, countries, sectors, industries, indexes, asset_index_membership    
market: prices_daily    
fundamentals: fundamental_snapshots    
macro: macro_assets, macro_prices

# 5) Roadmap
1. Asset metadata
2. Historical prices
3. Fundamentals
4. Macro data
5. Power BI integration

Future: Breadth indicators, External ratings, Trading engine

# 6) Decision Log