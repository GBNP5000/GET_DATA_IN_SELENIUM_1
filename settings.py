from shutil import which

BOT_NAME = 'gp'
SPIDER_MODULES = ['gp.spiders']
NEWSPIDER_MODULE = 'gp.spiders'
ROBOTSTXT_OBEY = False
SPLASH_URL = 'https://localhost:8050'
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
    'scrapy_selenium.SeleniumMiddleware': 800,

}
SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'


SELENIUM_DRIVER_NAME = 'ChromeDriver'
SELENIUM_DRIVER_EXECUTABLE_PATH = which('E:/PYTHONS/DRIVER/')
# '--headless' if using chrome instead of firefox
# SELENIUM_DRIVER_ARGUMENTS = ['-headless']
