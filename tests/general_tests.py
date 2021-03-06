"""Test General Page Expectations for ic.org."""
from tests.utils import SeleniumTestCase


class OldStoreTests(SeleniumTestCase):
    """Test Expectations for the Old store.ic.org Domain."""
    def setUp(self):
        """Visit store.ic.org."""
        self.selenium.get("http://store.ic.org")

    def test_redirects_to_new_store(self):
        """It should redirect to the new Community Bookstore URL."""
        self.assert_equal(self.selenium.current_url,
                          "http://www.ic.org/community-bookstore/")
