import snscrape.modules.twitter as sntwitter
import pandas as pd
import ssl

# Disable SSL verification
ssl._create_default_https_context = ssl._create_unverified_context

def scrape_tweets(username, max_tweets=100):
    print(f"🔄 Scraping tweets from @{username} using snscrape...")

    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'from:{username}').get_items()):
        if i >= max_tweets:
            break
        tweets.append([tweet.date, tweet.content])

    df = pd.DataFrame(tweets, columns=['Date', 'Content'])
    output_file = f"twitter_{username}_snscrape.csv"
    df.to_csv(output_file, index=False)

    print(f"✅ Scraped {len(df)} tweets from @{username} and saved to {output_file}")

def main():
    accounts = ["DrivelineBB", "drivelinekyle", "TreadHQ", "TreadAthletics"]
    for account in accounts:
        scrape_tweets(account)

if __name__ == "__main__":
    main()

