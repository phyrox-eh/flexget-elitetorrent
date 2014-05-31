from __future__ import unicode_literals, division, absolute_import
import logging
import re
from flexget import plugin
from flexget import validator
from flexget.entry import Entry
from flexget.event import event
from flexget.utils.soup import get_soup
from flexget.utils.search import torrent_availability, normalize_unicode, clean_title
from flexget.utils.requests import Session

log = logging.getLogger('search_elitetorrent')


class ETSearch(object):
    """ Elitetorrent Search plugin"""

    def search(self, entry, config):

        session = Session()
        entries = set()
        for search_string in entry.get('search_strings', [entry['title']]): #[entry['series_name']]:#
            search_string_normalized = normalize_unicode(clean_title(search_string)).encode('utf8')
            search_string_normalized = search_string_normalized.replace(' ','+')
            url = 'http://www.elitetorrent.net/busqueda/'+search_string_normalized
            
            log.debug('Fetching URL for `%s`: %s' % (search_string, url))

            page = session.get(url).content
            soup = get_soup(page)

            for result in soup.findAll('a', 'nombre'):
                entry = Entry()
                entry['title'] = result['title']
                entry['url'] = 'http://www.elitetorrent.net/get-torrent/'+result['href'].split('/')[2]
                log.debug('Adding entry `%s`: %s' % (entry['title'], entry['url']))
                entries.add(entry)

        return entries

@event('plugin.register')
def register_plugin():
    plugin.register(ETSearch, 'ET', groups=['search'], api_ver=2)
