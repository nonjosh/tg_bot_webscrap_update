from typing import List
from urllib.parse import urlparse, urlunparse

from bs4.element import Tag

from helpers.chapter import Chapter
from helpers.checkers.base import AbstractChapterChecker


class SyosetuChecker(AbstractChapterChecker):
    """Syosetu checker class"""

    URL_SUBSTRING = "syosetu"

    def get_latest_chapter_list(self) -> List[Chapter]:
        """Get latest chapter list

        Returns:
            List[Chapter]: latest chapter list
        """
        soup = self.get_latest_soup()
        if not soup:
            return []

        dl_list: List[Tag] = list(soup.findAll("a", {"class": "p-eplist__subtitle"}))
        chapter_list = []
        for chapter_tag in dl_list:
            chapter_title = chapter_tag.text.strip()
            chapter_path = chapter_tag["href"]
            chapter_url = urlunparse(
                urlparse(self.check_url)._replace(path=chapter_path)
            )
            chapter_list.append(Chapter(title=chapter_title, url=chapter_url))

        return chapter_list
