CREATE INDEX ix_prices_asset_date
ON market.prices_daily(asset_id, trade_date DESC);

CREATE INDEX ix_assets_ticker
ON core.assets(ticker);
