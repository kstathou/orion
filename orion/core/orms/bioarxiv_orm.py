from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import TEXT, VARCHAR, TSVECTOR
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, Date, Boolean

Base = declarative_base()


class Article(Base):
    """BioarXiv article."""

    __tablename__ = "articles"
    id = Column(Integer, primary_key=True)
    url = Column(TEXT)
    title = Column(TEXT)
    abstract = Column(TEXT)
    doi = Column(VARCHAR(200))
    collection = Column(TEXT)
    title_vector = Column(TSVECTOR)
    abstract_vector = Column(TSVECTOR)
    last_crawled = Column(Date)
    posted = Column(Date)
    author_vector = Column(TSVECTOR)


class ArticleAuthor(Base):
    """Article and its authors."""

    __tablename__ = "article_authors"
    id = Column(Integer, primary_key=True)
    article = Column(Integer)
    author = Column(Integer)
    institution = Column(TEXT)


class ArticlePublication(Base):
    """Article with DOI that has been published after peer review."""

    __tablename__ = "article_publications"
    article = Column(Integer, ForeignKey("articles.id"), primary_key=True)
    doi = Column(VARCHAR(200))
    publication = Column(TEXT)


class ArticleTraffic(Base):
    """Article traffic on bioarXiv."""

    __tablename__ = "article_traffic"
    id = Column(Integer, primary_key=True)
    article = Column(Integer, ForeignKey("articles.id"))
    month = Column(Integer)
    year = Column(Integer)
    abstract = Column(Integer)
    pdf = Column(Integer)


class AuthorRank(Base):
    """Author ranking (in terms of downloads) per category."""

    __tablename__ = "author_ranks_category"
    id = Column(Integer, primary_key=True)
    author = Column(Integer)
    category = Column(TEXT)
    rank = Column(Integer)
    tie = Column(Boolean)
    downloads = Column(Integer)


class Author(Base):
    """Author information."""

    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    name = Column(TEXT)
    institution = Column(TEXT)
    orcid = Column(TEXT)
    noperiodname = Column(TEXT)


class CrossRef(Base):
    """CrossRef information for article with DOI."""

    __tablename__ = "crossref_daily"
    id = Column(Integer, primary_key=True)
    source_date = Column(Date)
    doi = Column(TEXT)
    count = Column(Integer)
    crawled = Column(Date)


class PublicationDate(Base):
    """Publication date of an article."""

    __tablename__ = "publication_dates"
    article = Column(Integer, ForeignKey("articles.id"), primary_key=True)
    date = Column(Date)
