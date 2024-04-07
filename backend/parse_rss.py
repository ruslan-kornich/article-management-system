import datetime
import feedparser
from backend.database.database import SessionLocal, engine
from backend.core.models.article import Article
from backend.database.database import Base


def article_exists(db, title: str, link: str) -> bool:
    return (
        db.query(Article).filter(Article.title == title, Article.link == link).first()
        is not None
    )


def parse_guardian_rss(url: str, db):
    # Parse RSS The Guardian Technology
    feed = feedparser.parse(url)

    for entry in feed.entries:
        if not article_exists(db, entry.title, entry.link):
            article = Article(
                title=entry.title,
                link=entry.link,
                summary=entry.summary,
                published=datetime.datetime.strptime(
                    entry.published, "%a, %d %b %Y %H:%M:%S %Z"
                ),
                author=entry.author,
            )
            db.add(article)
            print(f"Added arcticle: {article.title}")

    db.commit()
    print("Update database finish")


if __name__ == "__main__":
    rss_url = "https://www.theguardian.com/uk/technology/rss"

    # Init db
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        parse_guardian_rss(rss_url, db)
    finally:
        db.close()
