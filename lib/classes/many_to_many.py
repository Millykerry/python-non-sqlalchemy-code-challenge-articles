class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author class")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be an instance of Magazine class")
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        if len(title) < 5 or len(title) > 50:
            raise Exception("Title must be between 5 and 50 characters")
        
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        raise AttributeError("Title cannot be changed after initialization")
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be an instance of Author class")
        self._author = value
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("Magazine must be an instance of Magazine class")
        self._magazine = value


class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if len(name) == 0:
            raise Exception("Name must be longer than 0 characters")
        
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        raise AttributeError("Name cannot be changed after initialization")
    
    def articles(self):
        return [article for article in Article.all if article.author == self]
    
    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))
    
    def add_article(self, magazine, title):
        return Article(self, magazine, title)
    
    def topic_areas(self):
        topics = list(set([article.magazine.category for article in self.articles()]))
        return topics if topics else None


class Magazine:
    all = []
    
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if len(name) < 2 or len(name) > 16:
            raise Exception("Name must be between 2 and 16 characters")
        if not isinstance(category, str):
            raise Exception("Category must be a string")
        if len(category) == 0:
            raise Exception("Category must be longer than 0 characters")

        self._name = name
        self._category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
    
    def articles(self):
        return [article for article in Article.all if article.magazine == self]
    
    def contributors(self):
        return list(set([article.author for article in self.articles()]))
    
    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None
    
    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        result = [author for author, count in author_counts.items() if count > 2]
        return result if result else None