""" Interfaces for content types. """"""http://plone.org/products/collective.blogging/issues/7In the uninstall code you can probably repeat over all content with that marker, using the object_provides index, and call noLongerProvides on it."""# Zopefrom zope.interface import Interface#===============================================================================# content types#===============================================================================class IAudio(Interface):    """ Audio content type. """class IPublication(Interface):    """ Publication content type """    #===============================================================================# markers#===============================================================================   class IGalleryContainerMarker(Interface):    """ Marker interface for gallery folders. """    class IHomepageHeroMarker(Interface):    """ Marker interface for items with homepage hero. """    class IHomepageBoxMarker(Interface):    """ Marker interface for items enabled for homepage boxes. """#===============================================================================# extenders#===============================================================================   class IBannerAware(Interface):    """ For all items with with banner image. """class ICategoriesAware(Interface):    """ For all items with with additional keywords fields. """class IGalleryReferenceAware(Interface):    """ For all items with gallery reference field. """    class IGalleryContainerAware(Interface):    """ For all gallery folders. """    class IHomepageHeroAware(Interface):    """ For all items displayed on homepage photo rotator. """    class IHomepageBoxAware(Interface):    """ For all items with content displayed in homepage middle section boxes. """    class IQuoteAware(Interface):    """ Adds a field and displays it at the footer as a quote. """    class ISortableAware(Interface):    """ For all items with sortable content. """