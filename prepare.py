import unicodedata
import re
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
from acquire import Acquire
from nltk.stem import WordNetLemmatizer

class Prepare:

    def basic_clean(self, string):
        """basic_clean [summary]

        Args:
            string ([type]): [description]

        Returns:
            [type]: [description]
        """

        string = string.lower()
        string = unicodedata.normalize('NFKD', string).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        string = re.sub(r"[^a-z0-9'\s]", "", string)
        return string

    def tokenize(self, string):
        """tokenize [summary]

        Args:
            string ([type]): [description]

        Returns:
            [type]: [description]
        """

        tokenizer = ToktokTokenizer()

        return tokenizer.tokenize(string, return_str=True)

    def stem(self, string):
        """stem [summary]

        Args:
            string ([type]): [description]

        Returns:
            [type]: [description]
        """

        ps = nltk.porter.PorterStemmer()
        # ps = PorterStemmer()
        stems = [ps.stem(word) for word in string.split()]
        return  ' '.join(stems)

    def lemmatize(self, string):
        """lemmatize [summary]

        Args:
            string ([type]): [description]

        Returns:
            [type]: [description]
        """

        wnl = WordNetLemmatizer()
        lemmas = [wnl.lemmatize(word) for word in string.split()]
        return  ' '.join(lemmas)

    def remove_stopwords(self, string, extra_words=None, exclude_words=None):
        """remove_stopwords [summary]

        Args:
            string ([type]): [description]
            extra_words ([type], optional): [description]. Defaults to None.
            exclude_words ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """

        stopw = stopwords.words('english')

        if extra_words:
            stopw.append(word for word in extra_words)

        elif exclude_words:
            stopw.remove(word for word in exclude_words)

        words = string.split()
        filtered_words = [word for word in words if word not in stopw]

        return ' '.join(filtered_words)