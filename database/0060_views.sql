CREATE VIEW market.vw_prices AS
SELECT
    a.ticker,
    a.display_name,
    p.trade_date,
    p.close,
    p.volume
FROM market.prices_daily p
JOIN core.assets a
    ON a.asset_id = p.asset_id;