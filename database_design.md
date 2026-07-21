# 1) Cíl
Databáze slouží jako centrální úložiště historických i referenčních dat o obchodovatelných aktivech. Musí být nezávislá na zdroji dat i klientské aplikaci.

# 2) Architektonické principy
   - PostgreSQL jako jediný datastore, ukládá pouze data
   - Zdrojová data se nepřepisují
   - Interní ID místo tickerů jako PK
   - Python obsahuje obchodní logiku

# 3) Schémata
   core    -  Referenční data
   market	-  Tržní data
   system	-  Technické tabulky

# 5) Tabulky
   core.assets  -  seznam obchodovatelných instrumentů
     PK: asset_id
     Referencuje: market.prices_daily

     Sloupce:
      Název	          Typ	          Null	  Poznámka
      asset_id	       BIGINT	       ❌	  PK
      symbol	       VARCHAR(32)	 ❌	  Symbol aktiva
      name	          TEXT	          ❌	  Název
      exchange_id	    BIGINT	       ❌	  FK
      asset_type_id	 SMALLINT	    ❌	  FK
      currency_id	    SMALLINT	    ❌	  FK
      active	       BOOLEAN	       ❌	  Aktivní instrument
      created_at	    TIMESTAMPTZ	 ❌	  Automaticky
      updated_at	    TIMESTAMPTZ	 ❌	  Automaticky

# 5) Vazby
   markets > exchanges > assets > prices_daily

# 6) Indexy
   Tabulka	      Index
   assets	        symbol
   prices_daily   asset_id, trade_date

# 7) Future
   - analytics
   - dividends
   - splits
   - financials
   - watchlists
   - portfolio
   - strategies

