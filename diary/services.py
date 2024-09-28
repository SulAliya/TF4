from django.core.cache import cache

from config.settings import CACHE_ENABLED
from diary.models import DiaryEntry


def get_from_cache():
    """
    Получает данные по записям из кэша, если кэш пуст, получает данные из БД.
    :return:
    """
    if not CACHE_ENABLED:
        return DiaryEntry.objects.all()
    key = 'diaryentry_list'
    diary = cache.get(key)
    if diary is not None:
        return diary
    diary = DiaryEntry.objects.all()
    cache.set(key, diary)
    return diary
