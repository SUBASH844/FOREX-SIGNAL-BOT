# FOREX-SIGNAL-BOT
# Forex Signal Telegram Bot

यो प्रोजेक्टले Forex trading का लागि Telegram मा automatic signals पठाउने Bot बनाउँछ।  
यसले TradingView बाट आउने webhook signals लाई receive गरेर Telegram मा तपाईँलाई Entry, SL, TP हरु पठाउँछ।

## Features

- Multiple currency pairs support (जस्तै: XAUUSD, USDJPY, EURUSD)
- Automatic signal sending based on TradingView alerts
- Entry, Stop Loss, Take Profit levels सहित signal पठाउने
- Personal use का लागि सजिलो र छिटो deploy गर्ने तरिका

## Requirements

- Python 3.x
- Flask
- requests library
- Telegram Bot Token र Chat ID (तपाईँको Telegram बाट लिने)

## Setup

1. `main.py` फाइलमा आफ्नो Telegram Bot Token र Chat ID राख्नुहोस्।
2. GitHub मा आफ्नो code upload गर्नुहोस्।
3. Railway मा project बनाउनुहोस् र GitHub repo जोड्नुहोस्।
4. Deploy गरेपछि, Telegram Bot चलिरहेको हुन्छ।
5. TradingView मा alert सेट गरेर webhook URL दिनुहोस्:  
   `https://your-railway-project-url/signal`

## Usage

TradingView बाट alert JSON format मा पठाउनुहोस् जसमा यी fields हुनेछन्:  
`pair`, `entry`, `sl`, `tp1`, `tp2`, `tp3`, `tp4`

Bot ले त्यो message Telegram मा पठाउनेछ।

---

## Author

तपाईँको नाम वा ID यहाँ राख्न सक्नुहुन्छ।

---

**Note:** यो प्रोजेक्ट व्यक्तिगत प्रयोगका लागि बनाइएको हो।  
यो Bot ले automatic trading गर्दैन, signal matra पठाउँछ।
