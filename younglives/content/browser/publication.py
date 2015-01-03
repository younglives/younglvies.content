import re

from Products.CMFCore.utils import getToolByName
from Products.Five import BrowserView
from plone.memoize import view
from zope.interface import implements

from younglives.content.interfaces.browser import IPublicationView

MIME_TYPES = [
    {'title': 'Word document',
     'regex': ('.*officedocument.word',)},
    {'title': 'Excel spreadsheet',
     'regex': ('.*officedocument.spreadsheet',)},
    {'title': 'PowerPoint presentation',
     'regex': ('.*officedocument.presentation',)},
    ]


class PublicationView(BrowserView):
    implements(IPublicationView)

    @view.memoize
    def files(self):
        results = []
        files = self.context.getFiles()
        ltool = getToolByName(self.context, 'portal_languages')
        for file in files:
            lang = file.Language() or 'en'
            type_field = file.getField('documentType')
            type = type_field and type_field.get(file)
            results.append(dict(title=file.Title(),
                                size='%s KB' % (file.get_size() / 1024),
                                url=file.absolute_url(),
                                css='',
                                type=(type and type[0]) or 'file',
                                language=ltool.getNameForLanguageCode(lang),
                                content_type=self._get_file_mimetype(file)))

        return results

    def _get_file_mimetype(self, file):
        mimetype = self.context.lookupMime(file.getContentType())
        for MIME_TYPE in MIME_TYPES:
            regexs = MIME_TYPE['regex']
            for regex in regexs:
                if re.search(regex, mimetype):
                    mimetype = MIME_TYPE['title']
                    break
        return mimetype
