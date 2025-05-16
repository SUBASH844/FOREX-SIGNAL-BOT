# FOREX-SIGNAL-BOT
# Forex Signal Telegram Bot

यो प्रोजेक्टले Forex trading को लागि Telegram मा automatic signals पठाउने Bot बनाउँछ।  
TradingView बाट आउने alert लाई webhook मार्फत receive गरी, Entry, SL, TP हरु Telegram मा पठाउँछ।

## विशेषता (Features)

- XAUUSD, USDJPY, EURUSD जस्ता multiple currency pairs support गर्छ।  
- TradingView alerts बाट automatic signal पठाउँछ।  
- Entry, Stop Loss, Take Profit (TP1-TP4) सहित signal पठाउँछ।  
- व्यक्तिगत प्रयोगका लागि सजिलो deployment।

## आवश्यक सामग्री (Requirements)

- Python 3.x  
- Flask library  
- requests library  
- Telegram Bot Token र Chat ID (तिम्रो Telegram बाट लिने)

## कसरी चलाउने (Setup)

1. `main.py` मा तिम्रो Telegram Bot Token र Chat ID राख।
2. GitHub मा project upload गर।  
3. Railway मा project बनाएर GitHub repo connect गर।  
4. Deploy गरेपछि, Telegram Bot चल्न थाल्छ।  
5. TradingView मा webhook URL सेट गर:  
   `https://तिम्रो-railway-project-url/signal`  

## प्रयोग (Usage)

TradingView बाट alert JSON format मा signal पठाउँछ जसमा यी fields हुनेछन्:  
`pair`, `entry`, `sl`, `tp1`, `tp2`, `tp3`, `tp4`  

Bot ले Telegram मा यो जानकारी पठाउनेछ।

---

## Author

तिम्रो नाम यहाँ राख्न सकिन्छ।

---

**नोट:** यो Bot automatic trading गर्दैन, signal matra पठाउँछ।  
Personal use का लागि मात्र बनाइएको हो।
