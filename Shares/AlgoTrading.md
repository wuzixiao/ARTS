
# Algo Trading Essential Training

## Basics of Security Markets

### Basics of stocks

* Price
* Market cap
* Dividend
* Standard deviation or volatility
* PE (price to earning ratio) price/earningpershare
* PB (price to book ratio) is accounting point of view

### Basics of stock markets

* The shrinking stock market
    * Fewer companies means mroe efficent markets (market efficency)
    * It gotten harder to pick stocks
    * Disappearing Alpha (mutual fund performance is worse and worse than market)

### Basic of trading stock

* Stocks: NYSE
* BATS
* Bonds
* ETFs(derivetives)

* Bid is the most someone what to pay
* Ask is the most someone will sell for
* Bid-Ask spread (large spread mean low liqu)

* Market orders
* Limit orders

### Algorithm oand financial industry

* Algo trading
    * Humans still play a role in trading
    * market making(Gaosheng) and data mining(fund)

### Excel Algo

* 5 columns : Date Open High Low Close

### Data analystics and algo

* RenTech is hedge fund using algo trading
* Think apple, and ome of the small vendors it uses
    * earning report of vendors come out may tell Apple will have a good report as well

### Stock and the Fed

* Fed plays a role in market on shot term basis
* Taylor Rule and Fed interference

### Big data in finance

* Intuition and data(Quantitative)
* Smart beta vs fundamentals vs technicals
* Avoid HiPPO(highest paied persons's opinion)

    1. Gather and clean data
    2. Analyze data
    3. Test choices with data
    4. Make decision

### Predicting values with regressions

* Regression analysis -> business tool
* Regressions: y = ax + b
* Predictions and Errors
    1. Run regressions
    2. Save coefficients(a is coefficient)
    3. Use coefficients and expected values for the future to get prediction

## Investing and Securities

### Stationarity and the VIX

* Moving average
    * =AVERAGE()

### ETF paris trading with algo

* 3 Columns 
    * Oil price
    * ETF of Oil company
    * ETF of Oil producers
* Correlation
    * =correl()
* Ratio
    * =PriceA/PriceB
* Buy or sell
    * Assume they should be close to each other, if the cap is large, buy or sell
    * =if(Ratio<0.65,1,0)

### Dual share class pairs trading

* VIA and VIA.B
* Return -Long only
    * Return is the profit of yesterday
    * Long : Just buy A?
    * BuyA * ((PriceOfDay-PriceOfYesterday)/PriceOfYesterday) + BuyB * ((PriceOfDay-PriceOfYesterday)/PriceOfYesterday)
* Return -Long/Short
    * Long/Short strategy : BuyA and SellB ??
    * BuyA * ((PriceAofToday-PriceAOfYesterday)/PriceAOfYesterday - ((PriceBofToday-PriceBofYesterday)/PriceBOfYesterday)) + BuyB * ((PriceBOfDay-PriceBOfYesterday)/PriceBOfYesterday - ((PriceAOfToday-PriceAOfYesterday)/PriceAOfYesterday))

### Common quantitative rules and strategies

* Mean Reversion
    * simply
    * Pairs trades: Walgreens and CVS, Ford and GM

* Four-Factor Model
    * Four-factor model of FAma and French
    * identifier chars of firms that do well on average over time
    * Use portfolios of companies with these chars
    * Too much noise in individual stocks
      1. Size: market of firm (Better  for small firms)
      2. Bookpto-market value : proxy for firm valuation(firms with Higher B/M has higher return)
      3. Beta: measures valatility of a stock
      4. Monentum: related to the concept of a "hot hand"
        * Companies do well will continue to do well in future

## Building Algo

### Gather data for an algo

* FRED : federal reserve economic data

### Test algo accuracy

* BigBuy = If(StandDiviation + Close < MovingAvarage, 1, 0)
* StandDiviation is =STDEV.S(E2:E121)
* 1DayReturn = If(yesterdaybuy, (PriceOfToday-PriceOfYesterday)/PriceOfYesterday, (PriceOfYesterday-PriceOfToday)/PriceOfYesterday)   I don't understand the else part
  
### Algo profitablitlity and trading decisions



