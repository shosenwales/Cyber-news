import feedparser
import webbrowser



def main():
    print("+++++++++++++++++++++++++++++++++")
    print("Daily CyberSecurity News Websites")
    print("++++++++++++++++++++++++++++++++++")
    print("[0]: TheHackerNews")
    print("[1]: Threatpost")
    print("[2]: Darkreading")
    print("[3]: Bleeping Computer")
    print("[4]: Theregister")
    print("[5]: Naked Security")
    print("[6]: CSO online")
    print("[7]: Cybernews")


    websites = (
        "https://feeds.feedburner.com/TheHackersNews",
        "https://threatpost.com/feed",
        "https://www.darkreading.com/rss.xml",
        "https://www.bleepingcomputer.com/feed/",
        "https://www.theregister.com/security/headlines.atom",
        "https://nakedsecurity.sophos.com/feed",
        "https://www.csoonline.com/uk/index.rss",
        "http://createfeed.fivefilters.org/extract.php?url=https%3A%2F%2Fcybernews.com%2F&max=5&order=document&guid=0"
    )

    website_input = int(input("Enter website number (0-7): "))

    NewsFeed = feedparser.parse(websites[website_input])
    article_list = []
    article_link = []
    for i in range(5):
        article = NewsFeed.entries[i]
        titles = article.title
        link = article.link
        article_link.append(link)
        article_list.append(titles)

    article_num = 1
    for article in article_list:
        print('[{}] {}'.format(str(article_num), article))
        article_num += 1

    article_link_click = False
    while not article_link_click:
        user_click = int(input("Choose the link you want to open (1-5): "))
        webbrowser.open(article_link[user_click-1])
        article_link_click = True

main()