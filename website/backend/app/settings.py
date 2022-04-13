from garpixcms.settings import *  # noqa
INSTALLED_APPS += [
    "show",
    "global",
    "home",
    "hotels",
]
#
# COMMENT_EVENT = 1
#
# NOTIFY_EVENTS = {
#     COMMENT_EVENT: {
#         'title': 'Новый Комментарий',
#     },
# }
# svwvmjcnhbnizwmh
BOOKING_EVENT = 1

NOTIFY_EVENTS = {
    BOOKING_EVENT: {
        'title': 'Новое Бронирование гостиницы',
    },
}



CHOICES_NOTIFY_EVENT = [(k, v['title']) for k, v in NOTIFY_EVENTS.items()]

# GARPIX_PAGE_GLOBAL_CONTEXT = "app.global_context.global_context_2"