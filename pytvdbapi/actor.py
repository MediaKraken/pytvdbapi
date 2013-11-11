# -*- coding: utf-8 -*-

# Copyright 2011 - 2013 Björn Larsson

# This file is part of pytvdbapi.
#
# pytvdbapi is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pytvdbapi is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pytvdbapi.  If not, see <http://www.gnu.org/licenses/>.

"""A module for actor related functionality."""

from pytvdbapi.error import TVDBAttributeError
from pytvdbapi._compat import implements_to_string

__all__ = ['Actor']


@implements_to_string
class Actor(object):
    """
    Representing an Actor as provided by `thetvdb.com <http://thetvdb.com>`_.
    It Will contain all attributes as delivered from
    `thetvdb.com <http://thetvdb.com>`_, the attributes are described in
    more detail `here <http://www.thetvdb.com/wiki/index.php/API:actors.xml>`_.

    It will also contain the attribute *image_url* that will be the full URL
    to the image of the actor.

    Example::

        >>> from pytvdbapi import api
        >>> db = api.TVDB("B43FF87DE395DF56")
        >>> result = db.search("dexter", "en")
        >>> show = result[0]

        >>> show.load_actors()

        >>> actor = show.actor_objects[0]
        >>> print(actor.image_url)
        http://thetvdb.com/banners/actors/70947.jpg

        >>> for actor in show.actor_objects: #doctest: +ELLIPSIS
        ...     print(u"{0} - {1}".format(actor.Name, actor.Role))
        ...
        Michael C. Hall - Dexter Morgan
        Jennifer Carpenter - Debra Morgan
        James Remar - Harry Morgan
        ...
        Jimmy Smits - Miguel Prado
        Jaime Murray - Lila Tournay
        John Lithgow - Arthur Mitchell
    """

    def __init__(self, mirror, data, show):
        self.mirror, self.data, self.show = mirror, data, show

    def __getattr__(self, item):
        if item == 'image_url':
            return self.mirror + u"/banners/" + self.Image
        else:
            try:
                return self.data[item]
            except KeyError:
                raise TVDBAttributeError(u"Actor has no {0} attribute".format(item))

    def __dir__(self):
        return list(self.data.keys()) + ['image_url']

    def __str__(self):
        return u'<{0} - {1}>'.format(self.__class__.__name__, self.Name)

    def __repr__(self):
        return self.__str__()
