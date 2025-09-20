from prometheus_client import Counter, Summary

CRAWLER_FETCH_TOTAL = Counter('crawler_fetch_total',
                            'Total number of crawler fetches.')

CRAWLER_SUCCESS_TOTAL = Counter('crawler_success_total',
                            'Number of successful crawler fetches.')

CRAWLER_ERROR_TOTAL = Counter('crawler_error_total',
                            'Number of failed crawler fetches.')
