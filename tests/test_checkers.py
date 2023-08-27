"""Test webscrapping function of the checker classes,
will skip if the url is not available."""
import unittest
from helpers.chapter import Chapter
from helpers import checkers
from helpers.utils import check_url_valid


class TestCheckers(unittest.TestCase):
    """Check if can get chapter list for each Checker"""

    def validate_chapter_list(self, chapter_list: list) -> None:
        """Validate chapter list"""
        # Check if the list item is an Chapter object
        self.assertIsInstance(chapter_list[0], Chapter)

        # Check if the chapter list is not empty
        self.assertGreater(len(chapter_list), 0)

    def universal_checking(self, test_checker, check_url: str) -> None:
        """Universal checker"""
        # Pass if the website is not healthy
        if check_url_valid(url=check_url, verbose=True):
            # Initialize checker
            _checker = test_checker(check_url)

            # Check if can get chapter list
            chapter_list = _checker.get_latest_chapter_list()
            self.validate_chapter_list(chapter_list)
        else:
            self.skipTest(f"{check_url} is not healthy")

    # Novel Checkers
    def test_syosetu_checker(self) -> None:
        """Syosetu"""
        self.universal_checking(
            test_checker=checkers.SyosetuChecker,
            check_url="https://ncode.syosetu.com/n6621fl",
        )

    def test_piaotian_checker(self) -> None:
        """Piaotian"""
        self.universal_checking(
            test_checker=checkers.PiaotianChecker,
            check_url="https://www.piaotian.com/html/14/14565/",
        )

    # FIXME: Need JS cookies but postman can access?
    def test_wx_checker(self) -> None:
        """99wx"""
        self.universal_checking(
            test_checker=checkers.WxChecker,
            check_url="https://www.99wx.cc/wanxiangzhiwang/",
        )

    def test_69shuba_checker(self) -> None:
        """69shu"""
        self.universal_checking(
            test_checker=checkers.SixNineShuBaChecker,
            check_url="https://www.69shuba.com/book/43616.htm",
        )

    # Comic Checkers
    def test_manhuagui_checker(self) -> None:
        """Manhuagui"""
        self.universal_checking(
            test_checker=checkers.ManhuaguiChecker,
            check_url="https://m.manhuagui.com/comic/17165/",
        )

    def test_qiman_checker(self) -> None:
        """Qiman"""
        self.universal_checking(
            test_checker=checkers.QimanChecker,
            check_url="http://qiman51.com/19827/",
        )

    def test_baozimh_checker(self) -> None:
        """Baozimh"""
        self.universal_checking(
            test_checker=checkers.BaozimhChecker,
            check_url="https://www.baozimh.com/comic/fangkainagenuwu-yuewenmanhua_e",
        )

    def test_xbiquge_checker(self) -> None:
        """Xbiquge"""
        self.universal_checking(
            test_checker=checkers.XbiqugeChecker,
            # check_url="https://www.xbiquge.la/55/55945/",
            check_url="https://www.xbiquge.so/book/53099/",
        )

    # FIXME: Need JS cookies but postman can access?
    def test_dashuhuwai_checker(self) -> None:
        """Dashuhuwai"""
        self.universal_checking(
            test_checker=checkers.DashuhuwaiChecker,
            check_url="https://www.dashuhuwai.com/comic/fangkainagenvwu/",
        )

    def test_mn4u_checker(self) -> None:
        """Mn4u"""
        self.universal_checking(
            test_checker=checkers.Mn4uChecker,
            check_url="https://mn4u.net/zgm-2149/",
        )

    def test_klmanga_checker(self) -> None:
        """Klmanga"""
        self.universal_checking(
            test_checker=checkers.KlmanagaChecker,
            check_url="https://klmanga.top/tensei-shitara-dai-nana-ouji-dattanode-kimamani-majutsu-o-kiwamemasu-raw",
        )
