from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticSitemap(Sitemap):
    priority = 1.0
    changefreq = "daily"

    def items(self):
        return ['home', 'main_home', 'report', 'sos', 'safety', 'guide', 'nearby_help']

    def location(self, item):
        return reverse(item)