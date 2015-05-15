from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('erdenkinder')


def kotti_configure(settings):
    settings['kotti.fanstatic.view_needed'] += ' erdenkinder.fanstatic.erdenkinder_css'
    settings['kotti.fanstatic.edit_needed'] += ' erdenkinder.fanstatic.erdenkinder_css'
